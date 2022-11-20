from django.urls import path
from .views import *

urlpatterns=[
    path('create',createPost,name='create'),
    path('home',AllPost.as_view(),name='home'),
]