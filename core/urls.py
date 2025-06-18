from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('partners/', views.partners, name='partners'),
    path('proposal/', views.proposal, name='proposal'),
    path('success/', views.success, name='success')
]