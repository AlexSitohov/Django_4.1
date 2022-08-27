from django.urls import path, include, re_path

from blog.views import *


urlpatterns = [
    path('', blog_view, name='blog'),
    path('add/', add_view, name='add'),
    path('<slug:category_slug>/', category_view, name='category'),
    path('<slug:category_slug>/<slug:note_slug>', note_view, name='note'),


]
