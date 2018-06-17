from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.index),  # home page
    url(r'^index.html', views.index),
    url(r'^exportCustomer.html', views.exportCustomer),
    url(r'^form_submit_Customer/', views.add_details_Customer),
    url(r'^form_submit_Invoice/', views.add_details_Invoice),
    url(r'^page-error-400.html', views.page_error)

    # path('form_submit_Invoice/', views.add_details_Invoice),
]
