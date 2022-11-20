from django.urls import path
from .views import *
urlpatterns = [
    # path('',reg.as_view(),name="home"),
    # path('register/',register,name='register'),
    # path('customer_register/',customer_register.as_view(),name='customer_register'),
    # path('employee_register/',employee_register.as_view(),name='employee_register'),
    # path('login/',login_request,name='login'),
    # path('logout/',logout_view,name='logout'),
    # path('index/',index,name='index'),
    # path('',home,name='home')
    # path('login',login.as_view()),


 path('',register,name='register'),
 path('login',login,name='login'),
 path('home',home,name="home"),

#  path('<int:pk>',update_user_details.as_view()),
#   path('detail/<int:pk>',user_details.as_view()),
#    path('delete/<int:pk>',delete_account.as_view()),
]