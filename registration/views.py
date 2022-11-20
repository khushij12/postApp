from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView
# from .models import userInfo
from django.urls import reverse_lazy
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from .views import *
from django.contrib import messages
from django.shortcuts import redirect
# from django.form import modelformset_factory

# Create your views here.

username_=None
# class reg(CreateView):
#     model = userInfo
#     fields = ('username','first_name','last_name','email_id','phone_no','gender','password')
#     template_name = 'registration.html'
#     success_url = reverse_lazy('home')

# class login(CreateView):
#     model = userInfo
#     fields = ('username','password')
#     template_name = 'registration.html'
#     success_url = reverse_lazy('home')

# class user_details(DetailView):
#     model = userInfo
#     template_name='userDetails.html'

# class update_user_details(UpdateView):
#     model = userInfo
#     fields='__all__'
#     template_name='updateUser.html'
#     success_url=reverse_lazy('home')

# class delete_account(DeleteView):
#     model = userInfo
#     template_name='userDelete.html'
#     success_url=reverse_lazy('home')

##########################
    
# def register(request):
#     return render(request, 'registration.html')
    
# def home(request):
#     return render(request, 'home.html')

# def index(request):
#     return render(request, 'index.html')

# class customer_register(CreateView):
#     model = User
#     form_class = CustomerSignUpForm
#     template_name='customer_register.html'

#     def form_valid(self,form):
#         user = form.save()
#         login(self.request,user)
#         return render(self.request,'index.html')


# class employee_register(CreateView):
#     model = User
#     form_class = EmployeeSignUpForm
#     template_name = 'employee_register.html'
#     def form_valid(self,form):
#         user = form.save()
#         login(self.request,user)
#         return render(self.request,'index.html')

# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST) 
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password) 
#             if user is not None :
#                 login(request,user)
#                 return render(request,'index.html') 
#             else:
#                 messages.error(request,"Invalid username or password")
#     else:
#         messages.error(request,"Invalid username or password") 
#     return render(request, 'login.html',
#     context={'form':AuthenticationForm()})


# def logout_view(request): 
#     logout(request)
#     # form = AuthenticationForm()
#     return render(request,'home.html')


##########

def register(request):
    if request.method == 'POST':
        form = reg(request.POST)

        if form.is_valid():
            p1 = form.cleaned_data.get('password')
            p2 = form.cleaned_data.get('password2')
            u1 = form.cleaned_data.get('username')

            if(p1 == p2):
                u = User.objects.filter(username = u1)
                if( u is not None or len(u)==0):  
                    form.save()
                    return redirect('/login')
                else:
                    messages.error(request, "username already exist.")
            else:
                messages.error(request,"Both Password is not matching")
    else:
        form = reg()
    
    return render(request,'registration.html',{'form':form})


def login(request):
    if request.method == 'POST':
        form = log(request.POST)

        if form.is_valid():
            un = form.cleaned_data.get('username')
            p1 = form.cleaned_data.get('password')
            user_ = User.objects.filter(username = un)
            # print(user_.count())
            # print(User.objects.none())
            if user_.count()==0:
                messages.error(request,"Username does not exist")
            elif(p1 == user_.values_list('password', flat=True).get(pk=1)):
                username_= user_
                return redirect('/home')
            else:
                messages.error(request,"Password is incorrect. Again try.")
    else:
        form = log()
    
    return render(request,'login1.html',{'form':form})

def home(request):
    return render(request, 'home1.html')

def logout(request):
    return render(request,'login.html')