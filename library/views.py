from django.shortcuts import render, get_object_or_404
from .models import Book, Author

# Create your views here.

def home(request):
    return render(request,'home.html')

def book_list(request):
    books = Book.objects.all()      #this is a new and important concept, the Django ORM (Object-Relational Mapper)
    return render(request,'book_list.html', {'books':books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request,'book_detail.html', {'book':book})

def author_list(request):
    authors = Author.objects.all()
    return render(request,'author_list.html', {'authors':authors}) 

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.book_set.all()         
    return render(request, 'author_detail.html', {'author': author, 'books': books})

def book_add(request):
    return render(request, 'book_form.html')

def book_edit(request, pk):
    return render(request, 'book_form.html')

def book_delete(request, pk):
    return render(request, 'book_confirm_delete.html')

def book_borrow(request, pk):
    return render(request, 'book_detail.html')

def book_return(request, pk):
    return render(request, 'book_detail.html')

def author_add(request):
    return render(request, 'author_form.html')

def author_edit(request, pk):
    return render(request, 'author_form.html')

def author_delete(request, pk):
    return render(request, 'author_confirm_delete.html')