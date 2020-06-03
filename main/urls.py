from django.urls import path     
from . import views


urlpatterns = [
    # loading views
    path('', views.index),
    path('dashboard/', views.load_dashboard),

    # function urls
    path('process_login/', views.process_login),
    path('process_register/', views.process_register),
]