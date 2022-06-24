from django.http import HttpResponse
from django.shortcuts import render, redirect
from  . models import Books
from . forms import BooksForm
# Create your views here.
def  books(request):
    bookx=Books.objects.all()
    context = {
        'book_list': bookx
    }
    return render(request, "home.html", context)

def details(request, book_id):
    book=Books.objects.get(id=book_id)
    return render(request, "detail.html", {'book': book})

def add_books(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        author = request.POST.get('author', )
        year = request.POST.get('year', )
        desc = request.POST.get('desc', )
        img = request.FILES['img']
        bookx=Books(name=name, author=author, year=year, desc=desc, img=img)
        bookx.save()
        return redirect('/')
    return render(request, 'add.html')

def  update(request, id):
    book=Books.objects.get(id=id)
    form=BooksForm(request.POST or None,  request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'book':book})

def delete(request,id):
   if request.method == 'POST':
       book=Books.objects.get(id=id)
       book.delete()
       return redirect('/')
   return render(request, "delete.html")
