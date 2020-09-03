from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('pets',views.PetList.as_view()),
    path('pets/<int:pk>/',views.PetDetail.as_view())
]