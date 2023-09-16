from django.urls import path
from . import views

urlpatterns = [
    path('fakeurl/', views.fakeurl, name='fakeurl'),
]
