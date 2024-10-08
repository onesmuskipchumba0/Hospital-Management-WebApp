import datetime
from django.db import models

# Create your models here.
class Doctor(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=15)
    specialty = models.CharField(max_length=200)
    time_starts_working = models.DateTimeField(default=datetime.datetime.combine(datetime.datetime.today(),datetime.time(8,0)))
    time_ends_working = models.DateTimeField(default=datetime.datetime.combine(datetime.datetime.today(),datetime.time(11,0)))
    date_added = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self) -> str:
        return f'{self.id}: {self.fullname}'
class Patient(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,null=True)
    disease = models.CharField(max_length=200)
    location = models.CharField(max_length=64)
    contact = models.CharField(max_length=15)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self) -> str:
        return f'{self.id}: {self.fullname} {self.doctor}'
class Medicine(models.Model):
    name = models.CharField(max_length=70)
    amount = models.IntegerField(default=0)
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.amount}'