from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def blog(request):
    return HttpResponse('<h1>Issa Blog</h1>')


def categories(request, categories_int):
    return HttpResponse(f'<h1>Issa category: {categories_int}</h1>')


def year_check(request, year):
    if int(year) > 2022:
        raise Http404()
    return HttpResponse(f'<h1>Issa year: {year}</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('not_found')
