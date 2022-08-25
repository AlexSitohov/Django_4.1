from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', main),
    path('blog/', include('blog.urls')),
]
