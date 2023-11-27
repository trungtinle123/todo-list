from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('delete/row/', views.delete_row, name="delete_row"),
    path('insert/row/', views.insert_row, name="insert_row"),
    path('update/status/', views.update_status, name="update_status"),
]
