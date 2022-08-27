from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import *
from blog.models import *


def blog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories

    }
    return render(request, 'blog/base.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound('not_found')


def blog_view(request):
    notes = Note.objects.all().order_by('create_date')
    categories = Category.objects.all()
    context = {
        'notes': notes,
        'categories': categories,
        'title': 'Выбор записи'
    }
    return render(request, 'blog/blog.html', context)


def note_view(request, note_slug, category_slug):
    note = get_object_or_404(Note, slug=note_slug)

    context = {'note': note,
               'title': note.title_of_note,
               }
    return render(request, 'blog/note.html', context)


def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all()
    notes = Note.objects.filter(
        category=category
    ).order_by('create_date')
    context = {
        'notes': notes,
        'categories': categories
    }
    return render(request, 'blog/category.html', context)


def add_view(request):
    if request.method == 'POST':
        form = AddNote(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('#')
            except:
                form.add_error(None, 'Ошибка')

    else:
        form = AddNote()
    context = {
        'form': form,

    }
    return render(request, 'blog/add.html', context)
