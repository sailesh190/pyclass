from django.shortcuts import render, redirect, get_object_or_404
from address_something.models import *
from address_something import forms

# Create your views here.


def homepage(request):
    cityList = City.objects.all()
    bookList = Book.objects.all()
    context = {
        'cityList': cityList,
        'bookList': bookList,
    }
    return render(request, 'homepage.html', context)


def add_homepage(request):
    if (request.method == 'POST'):
        # submit the form
        print("this in post add")
        form = forms.addressform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        print("1111")
        form = forms.addressform()
        context = {
            'form':form
        }
        return render(request, 'add_homepage.html', context)

def edit_homepage(request, bookId):
    context ={}
    book = get_object_or_404(Book, pk=bookId)
    form = forms.addressform(instance=book)

    if (request.method == 'POST'):
        # submit the form
        print("this in post edit")
        form = forms.addressform(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            form.save()
            return redirect('')
    else:
        print("1111")
        form = forms.addressform()
        context = {
            'form': form
        }
        return render(request, 'edit_homepage.html', context)

def delete_homepage(request,bookId):
    context ={}
    print(bookId)
    print("this is in delete")
    Book.objects.filter(id=bookId).delete()
    return redirect('')
    # return render(request, 'delete_homepage.html', context)