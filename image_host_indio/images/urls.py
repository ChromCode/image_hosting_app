from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

# app_name = 'images'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:img_width>/<int:img_height>/', views.specific_image, name=''),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
]