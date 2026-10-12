# form_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_form, name='feedback_form'),
]