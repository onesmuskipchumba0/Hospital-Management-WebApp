import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Patient,Doctor,Medicine

# Create your views here.
doctors = Doctor.objects.all()
current_hour= datetime.datetime.now().hour
current_minute= datetime.datetime.now().minute
current_second= datetime.datetime.now().second

def index(request):
    return render(request,'home/index.html')
def search_inventory(request):
    if request.method == 'POST':
        search_data = request.POST['search_inventory']
        drugs = Medicine.objects.filter(name=search_data).all()
        if not search_data == '':
            return render(request,'home/view_inventory.html',{'drugs':drugs})
        else:
            return render(request,'home/view_inventory.html',{'drugs':Medicine.objects.all()})
    else:
        patients = Medicine.objects.all()
        return render(request,'home/view_patients.html',{'drugs':patients})
def edit_inventory(request,drug_id):
    drug = Medicine.objects.get(pk=drug_id)
    return render(request,'home/edit_inventory.html',{'drug':drug})
def edit_inventory_logic(request,drug_id):
    drug = Medicine.objects.get(pk=drug_id)
    if request.method == 'POST':
        name=request.POST['name']
        amount = request.POST['amount']
        drug_to_edit = Medicine.objects.get(id=drug_id)
        if Medicine.objects.filter(id=drug_id).exists():
            drug_to_edit.name = name 
            drug_to_edit.amount = int(amount)#
            drug_to_edit.save()
            return HttpResponseRedirect(reverse('view_inventory'))
        else:
            return HttpResponseRedirect(reverse('edit_inventory',{'drug':drug}))
    return HttpResponseRedirect(reverse('edit_inventory'))
def remove_inventory(request,drug_id):
    drug_to_del = Medicine.objects.get(id=drug_id)
    if Medicine.objects.filter(id=drug_id).exists():
        drug_to_del.delete()
        return render(request,'home/view_inventory.html',{'drugs':Medicine.objects.all()})
    else:
        return render(request,'home/view_inventory.html')
def view_inventory(request):
    return render(request,'home/view_inventory.html',{'drugs':Medicine.objects.all()})
def new_inventory(request):
    return render(request,'home/new_inventory.html')
def new_inventory_handler(request):
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        if not name =='' or amount == '':#Aadd to database
            drug_exists = Medicine.objects.filter(name=name).exists()
            if not drug_exists:
                new_drug = Medicine(name=name,amount=int(amount))
                new_drug.save()
                return render(request,'home/view_inventory.html',{'drugs':Medicine.objects.all()})
            else:
                return render(request,'home/new_inventory.html')
        else:
            return render(request,'home/view_inventory.html',{'drugs':Medicine.objects.all()})
        
def available_doctors(request):
    doctors = Doctor.objects.filter(time_ends_working__hour__gt=current_hour,time_starts_working__hour__lte=current_hour).all()
    return render(request,'home/available_doctors.html',{'doctors':doctors})
def delete_patient(request,patient_id):
    
    patient_exists  = Patient.objects.filter(id=patient_id).exists()
    if patient_exists:
        patient_to_be_deleted = Patient.objects.get(id=patient_id)
        patient_to_be_deleted.delete()
        return render(request,'home/view_patients.html',{'patients':Patient.objects.all()})
    else:
        return render(request,'home/view_patients.html',{'patients':Patient.objects.all()})
def delete_doctor(request,doctor_id):
    
    doctor_exists = Doctor.objects.filter(id=doctor_id).exists()
    if doctor_exists:
        doctor_to_be_deleted = Doctor.objects.get(id=doctor_id)
        doctor_to_be_deleted.delete()
        return render(request,'home/view_doctors.html',{'doctors':Doctor.objects.all()})
    else:
         return render(request,'home/view_doctors.html',{'doctors':Doctor.objects.all()})
def edit_doctor(request,doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request,'home/edit_doctor.html',{'doctor':doctor})#
def edit_doctor_logic(request,doctor_id):
    current_date = datetime.datetime.now().date()
    time_start_working = request.POST.get('time_start_work')#
    time_end_working = request.POST.get('time_end_work')
    datetime_string = f'{current_date}{time_start_working}'
    formated_time_start_working = datetime.datetime.strptime(datetime_string,"%Y-%m-%d%H:%M")
    datetime_string_end = f'{current_date}{time_end_working}'
    formated_time_end_working = datetime.datetime.strptime(datetime_string_end,"%Y-%m-%d%H:%M")
    fullname = request.POST['fullname']
    email = request.POST['email']
    specialty = request.POST['specialty']
    contact = request.POST['contact']
    if fullname == '' or email == '' or specialty == '' or contact == '':
        return HttpResponse('Doctor Not added to database')
    else:
        #Handle signup logic
        doctor_exists = Doctor.objects.filter(id=doctor_id).exists()
        if doctor_exists:
            doctor = Doctor.objects.get(id=doctor_id)
            doctor.fullname = fullname
            doctor.email = email
            doctor.specialty = specialty
            doctor.contact = contact
            doctor.time_starts_working = formated_time_start_working
            doctor.time_ends_working = formated_time_end_working
            doctor.save()
            return HttpResponseRedirect(reverse('view_doctors'))            
        else:
            return render(request, 'new_doctor_view.html',{'error':'Doctor ALREADY Exists'})
            
def edit_patient(request,patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request,'home/edit_patient.html',{'patient':patient})#
def edit_patient_logic(request,patient_id):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        disease = request.POST['disease']
        patient_to_be_edited = Patient.objects.get(id=patient_id)
        patient_to_be_edited.fullname = fullname
        patient_to_be_edited.email = email
        patient_to_be_edited.contact = contact
        patient_to_be_edited.disease = disease
        patient_to_be_edited.save()
        return HttpResponseRedirect(reverse('view_patients'))
    patient = Patient.objects.get(id=patient_id)
    return render(request,'home/edit_patient.html',{'patient':patient})

def search_patients(request):
    if request.method == 'POST':
        search_data = request.POST['search_patient']
        if not search_data  == '':
            fullname,contact  = search_data.split(':')
            fullname = fullname.strip()
            contact = contact.strip()
            patients = Patient.objects.filter(fullname=fullname,contact=contact).all()
            return render(request,'home/view_patients.html',{'patients':patients})
        else:
            patients = Patient.objects.all()
            return render(request,'home/view_patients.html',{'patients':patients})
def view_patients(request):
    return render(request,'home/view_patients.html',{'patients':Patient.objects.all()})
def search(request):
    if request.method == 'POST':#
        search_data = request.POST['search_doctor']
        if not search_data  == '':
            fullname,specialty  = search_data.split(':')
            fullname = fullname.strip()
            specialty = specialty.strip()
            doctor = Doctor.objects.filter(fullname=fullname,specialty=specialty).all()
            return render(request,'home/view_doctors.html',{'doctors':doctor})
        else:
            doctor = Doctor.objects.all()
            return render(request,'home/view_doctors.html',{'doctors':doctor})
def view_doctors(request):
    return render(request,'home/view_doctors.html',{'doctors':Doctor.objects.all()})
def new_doctor_view(request):
    return render(request,'home/new_doctor_view.html')
def new_doctor(request):
    current_date = datetime.datetime.now().date()
    time_start_working = request.POST.get('time_start_work')#
    time_end_working = request.POST.get('time_end_work')
    datetime_string = f'{current_date}{time_start_working}'
    formated_time_start_working = datetime.datetime.strptime(datetime_string,"%Y-%m-%d%H:%M")
    datetime_string_end = f'{current_date}{time_end_working}'
    formated_time_end_working = datetime.datetime.strptime(datetime_string_end,"%Y-%m-%d%H:%M")
    fullname = request.POST['fullname']
    email = request.POST['email']
    specialty = request.POST['specialty']
    contact = request.POST['contact']
    if fullname == '' or email == '' or specialty == '' or contact == '':
        return HttpResponse('Doctor Added Successfully')
    else:
        #Handle signup logic
        doctor_exists = Doctor.objects.filter(fullname=fullname, email=email).exists()
        if doctor_exists:
            return render(request, 'new_doctor_view.html',{'error':'Doctor ALREADY Exists'})
        else:
            new_doctor = Doctor(fullname=fullname,email=email,specialty=specialty,contact=contact,time_starts_working=formated_time_start_working,time_ends_working=formated_time_end_working)
            new_doctor.save()
            return render(request, 'home/new_doctor_view.html',{'error':'The doctor has been successfully added to database!'})
def new_patient_view(request):
    return render(request,'home/new_patient.html',{'doctors':doctors})
def new_patient(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        disease = request.POST['disease']
        location = request.POST['location']
        contact = request.POST['contact']
        if fullname =='' or  email =='' or disease=='' or  location ==''or  contact=='':
            return render(request,'home/new_patient.html',{'error':'Values have to be filled'})
        else:
            docs = Doctor.objects.filter(specialty__contains=disease)
            if docs.exists():
                for doc in docs:
                    if doc.time_starts_working.hour >= current_hour and doc.time_ends_working.hour <= current_hour:
                        new_patient = Patient(doctor=doc,fullname=fullname,email=email,disease=disease,location=location,contact=contact)
                new_patient.save()
            else:
                #Replace with a nice error message
                return HttpResponse('No doctor available currently')
    return render(request,'home/new_patient.html',{'doctors':doctors})
        