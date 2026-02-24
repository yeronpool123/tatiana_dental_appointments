from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_history, name='add_history'),
    path('view/', views.view_history, name='view_history'),
]
