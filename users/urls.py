from django.urls import path
from . import views

app_name='users'
urlpatterns=[
    path('', views.index, name='index'),
    path('error/', views.error, name='error'),
    path('users/',views.recommendationPage,name='recommend'),
    path('form/',views.form,name='form')
]
