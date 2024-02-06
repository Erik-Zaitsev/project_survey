from django.shortcuts import render
from django.views.generic import ListView
from book.models import Book

# Create your views here.
class HomePage(ListView):
    model = Book