from django.urls import path, include, re_path

from blog.views import *

urlpatterns = [
    path('', blog),
    path('<int:categories_int>/', categories),
    re_path(r'^year/(?P<year>[0-9]{4})/', year_check),
]
