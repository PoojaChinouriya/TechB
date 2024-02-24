from django.urls import path
from .views import Add_task, delete_task, Edit_task

urlpatterns = [
    path('add/', Add_task),
    path('delete/<int:pk>/', delete_task),
    path('edit/<int:pk>/', Edit_task),
]