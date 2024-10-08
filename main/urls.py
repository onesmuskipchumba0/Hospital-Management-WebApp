from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('view_inventory/',views.view_inventory,name='view_inventory'),
    path('<int:drug_id>/remove_inventory/',views.remove_inventory,name='remove_inventory'),
    path('<int:drug_id>/edit_inventory/',views.edit_inventory,name='edit_inventory'),
    path('<int:drug_id>/edit_inventory_logic/',views.edit_inventory_logic,name='edit_inventory_logic'),
    path('new_inventory/',views.new_inventory,name='new_inventory'),
    path('new_inventory_handler/',views.new_inventory_handler,name='new_inventory_handler'),
    path('available_doctors/',views.available_doctors,name='available_doctors'),
    path('<int:doctor_id>/delete_doctor/',views.delete_doctor,name='delete_doctor'),
    path('<int:doctor_id>/edit_doctor/',views.edit_doctor,name='edit_doctor'),
    path('<int:doctor_id>/edit_doctor_logic/',views.edit_doctor_logic,name='edit_doctor_logic'),
    path('<int:patient_id>/edit_patient/',views.edit_patient,name='edit_patient'),
    path('<int:patient_id>/edit_patient_logic/',views.edit_patient_logic,name='edit_patient_logic'),
    path('search_patients/',views.search_patients,name='search_patients'),
    path('view_patients/',views.view_patients,name='view_patients'),
    path('search_doctor/',views.search,name='search_doctor'),
    path('search_inventory/',views.search_inventory,name='search_inventory'),
    path('view_doctors/',views.view_doctors,name='view_doctors'),
    path('new_patient_view/',views.new_patient_view,name='new_patient_view'),
    path('new_patient/',views.new_patient,name='new_patient'),
    path('new_doctor/',views.new_doctor,name='new_doctor'),
    path('new_doctor_view/',views.new_doctor_view,name='new_doctor_view'),
]