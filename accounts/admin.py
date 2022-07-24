from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Procedur)
admin.site.register(Payment)

