from django.shortcuts import render, redirect, get_list_or_404
from .models import Book
# from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books':books})

def book_create(request):
    
    return render(request, 'library/book_form.html', {'form': form})

