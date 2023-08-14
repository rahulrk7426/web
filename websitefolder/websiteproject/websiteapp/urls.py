from .import views
from django.urls import path

urlpatterns = [
    path('',views.website,name='website'),


]
