from django.urls import path
from .views import *
urlpatterns=[
    path('',contactList.as_view(),name='contact_display'),
    path('create',contactCreate.as_view(),name='contact_create'),
    path('<int:pk>/update',contactUpdate.as_view(),name='contact_update'),
    path('<int:pk>/delete',contactDelete.as_view(),name='contact_delete'),
    path('<int:pk>',contactDetail.as_view(),name='contact_detail'),
    path('login',login)
]