from django.http import HttpResponse
from django.shortcuts import render, redirect


def main(request):
    return render(request, 'main/main.html')
