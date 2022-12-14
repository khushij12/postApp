

from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.db import transaction

from .models import *

# # class CustomerSignUpForm(UserCreationForm): 
# #     first_name = forms.CharField(required=True) 
# #     last_name = forms.CharField(required=True) 
# #     phone_number = forms.CharField(required=True) 
# #     location = forms.CharField(required=True)
    
# #     class Meta(UserCreationForm.Meta): 
# #         model = User

# #     @transaction.atomic # for saving records in both the models user and customer
# #     def save(self):
# #         user = super().save(commit=False)
# #         user.is_customer = True
# #         user.first_name = self.cleaned_data.get('first_name') 
# #         user.last_name = self.cleaned_data.get('last_name') 
# #         user.save() # for saving record in Database
# #         customer = Customer.objects.create(user=user) 
# #         customer.phone_number=self.cleaned_data.get('phone_number')
# #         customer.location=self.cleaned_data.get('location') 
# #         customer.save()
# #         return user

# # class EmployeeSignUpForm(UserCreationForm): 
# #     first_name = forms.CharField(required=True) 
# #     last_name = forms.CharField(required=True) 
# #     phone_number = forms.CharField(required=True) 
# #     designation = forms.CharField(required=True)

# #     class Meta(UserCreationForm.Meta):
# #         model = User
# #     @transaction.atomic
# #     def save(self):
# #         user = super().save(commit=False)
# #         user.is_employee = True
# #         user.is_staff = True
# #         user.first_name = self.cleaned_data.get('first_name') 
# #         user.last_name = self.cleaned_data.get('last_name') 
# #         user.save()
# #         employee = Employee.objects.create(user=user) 
# #         employee.phone_number=self.cleaned_data.get('phone_number') 
# #         employee.designation=self.cleaned_data.get('designation') 
# #         employee.save()
# #         return user


# ###################

class log(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['full_name','address','age','phone_number','birth_date','email','password2']
    
class reg(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
