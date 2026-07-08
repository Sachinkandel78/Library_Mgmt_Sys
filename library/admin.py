from django.contrib import admin
from .models import Author, Book

# Register your models here. #Registered two model author rw book
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')
admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_available', 'copies_available', 'copies_total')
admin.site.register(Book, BookAdmin)
