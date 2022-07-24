from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
#Django Codemy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import PaymentForm, PatientForm, CreateUserForm
from .filters import PaymentFilter, PatientFilter, DoctorFilter


#Django Codemy
class AddPatientView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'add_patient.html'


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Reseption')
            user.groups.add(group)

            messages.success(request, 'Аккаунт был успешно создан для ' + username)

            return redirect('login')
            
    context = {'form':form}
    return render(request, 'accounts/register.html', context)    

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Имя пользователя и/или Пароль, не верны!')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    patients = Patient.objects.all()
    payments = Payment.objects.all()
    doctors = Doctor.objects.all()
    total_patients = patients.count()
    total_payments = payments.count()
    total_doctors = doctors.count()

    context = {'patients':patients,
            'payments':payments,
            'doctors':doctors,
            'total_patients':total_patients,
            'total_payments':total_payments,
            'total_doctors':total_doctors}

    return render(request, 'accounts/dashboard.html', context)

def userPage(request):
    context = {}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def database_patients(request):
    patients = Patient.objects.all()

    patientfilter = PatientFilter(request.GET, queryset=patients)
    patients = patientfilter.qs

    context = {'patientfilter':patientfilter,
                'patients':patients,
                }
    return render(request, 'accounts/database_patients.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def database_payments(request):
    payments = Payment.objects.all()

    paymentfilter = PaymentFilter(request.GET, queryset=payments)
    payments = paymentfilter.qs

    context = {'paymentfilter':paymentfilter,
                'payments':payments,
                }
    return render(request, 'accounts/database_payments.html', context)
                    

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def database_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'accounts/database_doctors.html', {'doctors': doctors})



@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def personal_page_patient(request, pk):
    patients = Patient.objects.get(id=pk)

    payments = patients.payment_set.all()

    context = {'patients':patients,
                }
    return render(request, 'accounts/personal_page_patient.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def personal_page_doctor(request, pk):
    doctors = Doctor.objects.get(id=pk)

    payments = doctors.payment_set.all()
    payment_count = payments.count()

    doctorfilter = DoctorFilter(request.GET, queryset=payments)
    payments = doctorfilter.qs

    context = {'doctors':doctors,
                'payments':payments,
                'payment_count':payment_count,
                'payments':payments,
                'doctorfilter':doctorfilter,
                }
    return render(request, 'accounts/personal_page_doctor.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Reseption'])
def createPayment(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form,}
    return render(request, 'accounts/payment_form.html',
                    context,
                    )

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def updatePayment(request, pk):

    payment = Payment.objects.get(id=pk)
    form = PaymentForm(instance=payment)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form,}
    return render(request, 'accounts/payment_form.html',
                    context,
                    )

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def deletePayment(request, pk):
    payment = Payment.objects.get(id=pk)
    if request.method == "POST":
        payment.delete()
        return redirect('/')

    context = {'item':payment,}

    return render(request, 'accounts/payment_delete.html',
                    context,
                    )




@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def createPatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form,}
    return render(request, 'accounts/patient_form.html',
                    context,
                    )

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def updatePatient(request, pk):

    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form,}
    return render(request, 'accounts/patient_form.html',
                    context,
                    )


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('/')

    context = {'item':patient,}

    return render(request, 'accounts/patient_delete.html',
                    context,
                    )