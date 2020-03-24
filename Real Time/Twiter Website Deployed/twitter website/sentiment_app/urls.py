from django.contrib import admin
from django.urls import path
from . import views

app_name = "Sentiment"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:terms>/<keyword>', views.show, name='show'),
    path('show/', views.show1, name='show1'),
]
