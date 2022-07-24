from django.urls import path
from . import views
from . views import AddPatientView

urlpatterns = [
#Django Codemy
    path('add_patient/', AddPatientView.as_view(), name="add_patient"),


    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('database_patients/', views.database_patients, name="database_patients"),
    path('database_doctors/', views.database_doctors, name="database_doctors"),
    path('database_payments/', views.database_payments, name="database_payments"),

    path('personal_page_patient/<str:pk>/', views.personal_page_patient, name="patient"),
    path('personal_page_doctor/<str:pk>/', views.personal_page_doctor, name="doctor"),

    path('payment_create/', views.createPayment, name="payment_create"),
    path('payment_update/<str:pk>/', views.updatePayment, name="payment_update"),
    path('payment_delete/<str:pk>/', views.deletePayment, name="payment_delete"),

    path('patient_create/', views.createPatient, name="patient_create"),
    path('patient_update/<str:pk>/', views.updatePatient, name="patient_update"),
    path('patient_delete/<str:pk>/', views.deletePatient, name="patient_delete"),
]
