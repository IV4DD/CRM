from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Patient(models.Model):
    first_name = models.CharField(max_length=60, verbose_name = "Имя пациента")
    surname = models.CharField(max_length=60, verbose_name = "Фамилия пациента")
    middle_name = models.CharField(max_length=60, verbose_name = "Отчество пациента")

    phone = models.CharField(max_length=11, unique=True, verbose_name = "Номер сотового")
    iin = models.PositiveBigIntegerField(verbose_name = "ИИН")

    date_created = models.DateTimeField(auto_now_add=True, verbose_name = "Дата регистрации")

    def __str__(self):
        return self.first_name  +' '+ str(self.surname)  +' '+ str(self.middle_name)
    def get_absolute_url(self):
        return reverse('home')



class Doctor(models.Model):
    first_name = models.CharField(max_length=60, verbose_name = "Имя врача")
    middle_name = models.CharField(max_length=60, verbose_name = "Отчество врача")
    surname = models.CharField(max_length=60, verbose_name = "Фамилия врача")
    departments = [
                ('DD¹', 'DD¹'),
                ('DD²', 'DD²'),
                ('DD³', 'DD³'),
                ('DD⁴', 'DD⁴'),
                ('DD⁵', 'DD⁵'),
                ('Департамент Маркетинга', 'Департамент Маркетинга'),
                ('Отдел Кадров', 'Отдел Кадров'),
                ('DT', 'DT'),
                ('DM', 'DM'),
                ]
    department = models.CharField(max_length=200, verbose_name = "Наши отделения", null=True, blank=True)

    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, verbose_name = "Номер сотового")
    email = models.EmailField(max_length=50, unique=True, verbose_name = "E-mail")
    birthday = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name = "Дата рождения")

    def __str__(self):
        return self.first_name  +' '+ str(self.middle_name) +' '+ str(self.surname)
    def get_absolute_url(self):
        return reverse('home')

class Procedur(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Наименование процедуры")
    price = models.CharField(max_length=10, verbose_name = "Стоимость")
    category = models.CharField(max_length=20, verbose_name = "Категория")
    description = models.TextField(max_length=200, blank=True, verbose_name = "Описание")

    def __str__(self):
        return self.name

class Payment(models.Model):
    income = models.PositiveIntegerField(verbose_name = "Сумма")
    methods = (
            ('Наличными', 'Наличными'),
            ('Картой', 'Картой'),
            ('Перевод', 'Перевод'),
            ('В долг', 'В долг'),
            ('Страховка', 'Страховка'),
            ('KaspiRed', 'KaspiRed'),
            ('Kaspi Рассрочка', 'Kaspi Рассрочка'),
            ('Бартер с ВВ', 'Бартер с ВВ'),
            ('Бартер без ВВ', 'Бартер без ВВ'),
            ('Private Clinic', 'Private Clinic'),
            )
    payment_method = models.CharField(max_length=200,verbose_name = "Способ оплаты", choices=methods)
    technical_cost = models.PositiveIntegerField(verbose_name = "Тех. затраты")
    evening_shift = models.BooleanField(default=False, verbose_name = "Вечерняя смена")
    patient = models.ForeignKey(Patient, verbose_name = "Пациент", null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, verbose_name = "Врач", null=True, on_delete=models.SET_NULL)
    procedurs = models.ForeignKey(Procedur, verbose_name = "Процедура", null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name = "Дата регистрации")

    def __str__(self):
        return str(self.patient) + ' ' + '"' + str(self.procedurs.name) + '"' + ' ' + str(self.income)
