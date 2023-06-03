from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courier/', views.courier, name='courier'),
    path('branch/', views.branch, name='branch'),
    path('costumer/', views.costumer, name='costumer')

]
