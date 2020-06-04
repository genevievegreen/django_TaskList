from django.urls import path     
from . import views


urlpatterns = [
    # loading views
    path('', views.index),
    path('dashboard/', views.load_dashboard),
    path('view_list/<int:id>/', views.view_list),

    # function urls
    path('process_login/', views.process_login),
    path('process_register/', views.process_register),

    # list
    path('create_list/', views.create_list),
    path('add_listItem/', views.add_listItem),
]