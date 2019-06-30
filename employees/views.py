from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login 
 
class EmployeeRegistrationView(CreateView): 
    template_name = 'employees/employee/registration.html' 
    form_class = UserCreationForm 
    success_url = reverse_lazy('employee_accident_list') 
 
    def form_valid(self, form): 
        result = super(EmployeeRegistrationView, self).form_valid(form) 
        cd = form.cleaned_data 
        user = authenticate(username=cd['username'], password=cd['password1']) 
        login(self.request, user) 
        return result