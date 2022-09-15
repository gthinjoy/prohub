from django.shortcuts import render, redirect
from .models import Book
from .forms  import BooksForm
# Create your views here.
def  home(request):
    booklib = Book.objects.all()
    context = {
        'book_list': booklib
    }
    return render(request, 'home.html', context)


def  detail(request, book_id):
    book= Book.objects.get(id=book_id)
    return render(request, "detail.html", {'book': book})


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        author = request.POST.get('author', )
        description = request.POST.get('description',)
        year = request.POST.get('year',)
        image = request.FILES['image']
        booklib = Book(name=name, author=author, description=description, year=year, image=image)
        booklib.save()
        return redirect('/')
    return render(request, "add.html")

def edit(request, id):
    book= Book.objects.get(id= id)
    form=  BooksForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'book': book})

def delete(request, id):
    if request.method == 'POST':
        book= Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request, 'delete.html')

