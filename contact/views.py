from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from django.template import loader
from django.urls import reverse_lazy
from .models import contact
# from dataclasses import fields
from django.db.utils import OperationalError
from .forms import loginDetails

# Create your views here.
class contactCreate(CreateView):
    model = contact
    fields = ('full_name','address','age','phone_number','birth_date','email')
    template_name = 'contact_create.html'
    success_url = reverse_lazy('contact_display')

class contactList(ListView):
    try:
        model = contact
        template_name = 'contact_display.html'
        context_object_name="contacts"
    except OperationalError:
        pass


class contactDetail(DetailView):
    model = contact
    template_name = 'contact_detail.html'
    context_object_name='contacts'

class contactUpdate(UpdateView):
    model = contact
    fields = ('phone_number','email')
    template_name = "contact_update.html"
    context_object_name="contacts"
    success_url = reverse_lazy('contact_display')

class contactDelete(DeleteView):
    model = contact
    template_name="contact_delete.html"
    content_object_name="contacts"
    success_url = reverse_lazy('contact_display')

def login(request):
    form=loginDetails()
    return render(request,'forms.html',{'login_form':form})
