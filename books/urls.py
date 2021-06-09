from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path('authors/', views.authors, name="authors"),
    path('add_books/', views.add_books, name="add_books"),
    path('add_authors/', views.add_authors, name="add_authors"),
    path('update_books/<str:pk>', views.update_books, name="update_books"),
    path('update_authors/<str:pk>/', views.update_authors, name="update_authors"),
    path('delete_books/<str:pk>/', views.delete_books, name="delete_books"),
    path('delete_authors/<str:pk>/', views.delete_authors, name="delete_authors")
]
