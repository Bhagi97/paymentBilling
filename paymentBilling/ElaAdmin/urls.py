from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login.html', views.login_request, name='login_request'),
    url(r'^logout.html', views.logout_request, name='logout_request'),

    url(r'^add_profile.html', views.add_profile),

    url(r'^exportCustomer.html', views.exportCustomer),
    url(r'^form_submit_Customer/', views.add_details_Customer),

    url(r'^form_submit_Invoice/', views.add_details_Invoice),

    url(r'^page-error-400.html', views.page_error_400),
    url(r'^page-error-403.html', views.page_error_403),

    url(r'^import_file/', views.import_file),

    url(r'^index.html', views.index),
    url(r'^', views.index)  # home page
    # path('form_submit_Invoice/', views.add_details_Invoice),
]
