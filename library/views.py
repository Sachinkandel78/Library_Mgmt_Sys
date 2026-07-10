from django.shortcuts import render, get_object_or_404, redirect
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
    authors = Author.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')
        copies_total = request.POST.get('copies_total')
        copies_available = request.POST.get('copies_available')
        
        author = Author.objects.get(pk=author_id)
        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            published_date=published_date,
            copies_total=copies_total,
            copies_available=copies_available,
        )
        return redirect('book_list')
    return render(request, 'book_form.html', {'authors': authors})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    authors = Author.objects.all()

    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author = Author.objects.get(pk=author_id)
        book.isbn = request.POST.get('isbn')
        book.published_date = request.POST.get('published_date')
        book.copies_total = request.POST.get('copies_total')
        book.copies_available = request.POST.get('copies_available')
        book.save()
        return redirect('book_detail', pk=book.pk)

    return render(request, 'book_form.html', {'book': book, 'authors': authors})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

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