from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('registerAccount/', views.RegisterAccounts, name='RegisterAccounts'),
    path('loginAccount/', views.LoginAccounts.as_view(), name='LoginAccounts'),
    path('logoutAccount/', views.LogoutAccounts, name='LogoutAccounts'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
