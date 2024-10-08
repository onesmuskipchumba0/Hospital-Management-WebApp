from django.contrib import admin
from .models import Doctor,Patient
# Register your models here.
class DoctorInfo(admin.ModelAdmin):
    list_display=('id','fullname','email','contact','specialty')
class PatientInfo(admin.ModelAdmin):
    list_display=('id','fullname','doctor','email','contact','disease')
admin.site.register(Doctor,DoctorInfo)
admin.site.register(Patient,PatientInfo)