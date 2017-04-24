from django.shortcuts import render
from .models import Books

def index(request):
    Books.objects.create(title='Bible',author='God',publish=1,category='Historical')
    Books.objects.create(title='Moby Dick',author='Dunno',publish=1860,category='Fiction')
    Books.objects.create(title='Eragon',author='Youth',publish=2005,category='Sci-Fi/Fantasy')
    Books.objects.create(title='Roots',author='IDK',publish=1980,category='Allegorical')
    Books.objects.create(title='The Hobbit',author='JRR Tolkien',publish=1940,category='Childrens')
    books = Books.objects.all()
    for book in books:
        print book.title, book.author, book.publish, book.category, book.in_print
    return render(request, 'books_app/index.html')



    # Create your views here.
