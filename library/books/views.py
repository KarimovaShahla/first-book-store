from .models import Book
from django.shortcuts import render

# Create your views here.

def books(request):
    books = Book.objects.order_by("-created_at")[:5]
    context = {
        "books": books
    }
    return render(request, "books/home.html", context)