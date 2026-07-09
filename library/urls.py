from django.urls import path
from . import views  # from the current app folder

urlpatterns = [
    # Home page ko route
    path('', views.home, name='home'),

    # Book ko routes
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/add/', views.book_add, name='book_add'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('books/<int:pk>/borrow/', views.book_borrow, name='book_borrow'),
    path('books/<int:pk>/return/', views.book_return, name='book_return'),

    # Author ko routes
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/add/', views.author_add, name='author_add'),
    path('authors/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
]