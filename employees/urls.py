from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('register/', views.EmployeeRegistrationView.as_view(), name='employee_registration'), 
]