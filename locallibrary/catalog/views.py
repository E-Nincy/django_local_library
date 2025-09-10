from django.shortcuts import render, get_list_or_404
from django.views import generic
# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Available books (status = 'a')
    num_genres = Genre.objects.count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_books_with_word = Book.objects.filter(title__icontains='love').count()
    num_genres_with_word = Genre.objects.filter(name__icontains='fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances_available,
        'num_genres': num_genres,
        'num_authors': num_authors,
        'num_books_with_word': num_books_with_word,
        'num_genres_with_word': num_genres_with_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'catalog/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['some_data'] = 'This is just some data'

        return context
    
class BookDetailView(generic.DetailView):
    model = Book

from django.shortcuts import get_object_or_404

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/book_detail.html', context={'book': book})