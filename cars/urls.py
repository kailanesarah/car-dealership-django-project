from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('listCars/', views.ListViewCars.as_view(), name='ListViewCars'),
    path('detailCars/<int:pk>/',views.DetailViewsCar.as_view(), name='DetailViewsCar'),
    path('registerCars/', views.CreateViewCars.as_view(), name='CreateViewCars'),
    path('updateCars/<int:pk>/update',views.UpdateViewCars.as_view(), name="UpdateViewCars"),
    path('deleteCars/<int:pk>/delete',views.DeleteViewCars.as_view(), name="DeleteViewCars"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
