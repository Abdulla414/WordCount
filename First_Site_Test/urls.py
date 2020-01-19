from django.urls import path
from First_Site_Test import views

urlpatterns = [
    path('', views.home),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
]
