from django.http import HttpResponse
from django.shortcuts import render, redirect


def main(request):
    return HttpResponse('<h1>Hello issa main page</h1>')
