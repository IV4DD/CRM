import django_filters
from django_filters import DateFilter

from .models import *

class PaymentFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	class Meta:
		model = Payment
		fields = '__all__'
		exlude = ['date_created']

class PatientFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	class Meta:
		model = Patient
		fields = '__all__'
		exlude = ['date_created']

class DoctorFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	class Meta:
		model = Payment
		fields = '__all__'
		exlude = ['date_created']
