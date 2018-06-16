from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),  # home page
    path('index.html', views.index),
    path('exportCustomer.html', views.exportCustomer),
    path('form_submit_Customer/', views.add_details_Customer),
    path('form_submit_Invoice/', views.add_details_Invoice),
    path('page-error-400.html', views.page_error)

    # path('form_submit_Invoice/', views.add_details_Invoice),
]
