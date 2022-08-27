from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', main, name='main'),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls'))
]
