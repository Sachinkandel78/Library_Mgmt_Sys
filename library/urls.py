from django.urls import path
from . import views  #from the current app folder

urlpatterns =[
        #Home page ko route
        path('',views.home, name='home'),
        #Book ko routes
        path('books/', views.book_list, name='book_list'),
        path('books/<int:pk>/', views.book_detail,name='book_detail'),
        path('books/add/', views.book_add, name='book_add'),
        path('books/<id>/edit', views.book_edit, name='book_edit'),
        path('books/<id>/delete', views.book_delete, name='book_delete'),
        path('books/<id>/borrow', views.book_borrow, name='book_borrow'),
        path('books/<id>/return', views.book_return, name='book_return'),
        #Author ko routes
        path('authors/', views.author_list, name='author_list'),
        path('authors/<id>/', views.author_detail, name='author_detail'),
        path('authors/add/', views.author_add, name='author_add'),
        path('authors/<id>/edit/', views.author_edit, name='author_edit'),
        path('authors/<id>/delete/', views.author_delete, name='author_delete'),

]