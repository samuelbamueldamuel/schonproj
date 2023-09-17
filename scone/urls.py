from django.urls import path
from . import views

# app_name = 'scone'

urlpatterns = [
    path('fakeurl/', views.fakeurl, name='fakeurl'),
    path('work/', views.work, name = 'work'),
    # path('givenSymbol/<str:symbol>')
]


