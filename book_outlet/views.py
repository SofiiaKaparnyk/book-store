from django.db.models import Avg
from django.shortcuts import get_object_or_404, render

from .models import Book


def index(request):
    books = Book.objects.all()
    avg_rating = books.aggregate(Avg("rating"))["rating__avg"]
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": books.count(),
            "average_rating": round(avg_rating, 2),
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {"book": book})
