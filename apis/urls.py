from django.urls import path, include
from . import views

urlpatterns = [
    path('photos/<int:page>/', views.PhotoList.as_view()),
    path('photos/detail/<int:pk>/', views.PhotoDetail.as_view()),
]   