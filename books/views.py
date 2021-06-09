from django.db.models.fields.json import DataContains
from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import *
# Create your views here.


def books(request):
    books = Book.objects.order_by('title')
    data = {"books": books}
    return render(request, "books/books.html", data)


def authors(request):
    authors = Author.objects.order_by('first_name')
    data = {"authors": authors}
    return render(request, "books/authors.html", data)


def add_books(request):
    form = BooksForm()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    data = {"form": form}
    return render(request, "books/add_books.html", data)


def add_authors(request):
    form = AuthorsForm()
    if request.method == 'POST':
        form = AuthorsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authors')

    data = {"form": form}
    return render(request, "books/add_authors.html", data)


def update_books(request, pk):
    book = Book.objects.get(id=pk)
    form = BooksForm(instance=book)

    if request.method == "POST":
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')

    data = {"book": book, "form": form}
    return render(request, 'books/update_books.html', data)


def update_authors(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorsForm(instance=author)

    if request.method == "POST":
        form = AuthorsForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('/')

    data = {"author": author, "form": form}
    return render(request, 'books/update_authors.html', data)


def delete_books(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('/')


def delete_authors(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect('/authors')
