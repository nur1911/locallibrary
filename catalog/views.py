from django.shortcuts import render

from .models import Book, BookInstanse, Author, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstanse.objects.all().count()
    num_instances_available = BookInstanse.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count(2)

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors}
    )
