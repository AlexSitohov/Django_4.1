from django.urls import path, include, re_path

from blog.views import *
from blog.views import *

urlpatterns = [
    path('', blog_view, name='note'),
    path('<slug:category_slug>/<slug:note_slug>', note_view, name='note'),
    path('<slug:category_slug>/', category_view, name='category'),
    re_path(r'^year/(?P<year>[0-9]{4})/', year_check),

]
