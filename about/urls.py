from django.urls import path, include

from about.views import about

urlpatterns = [
    path('', about, name='about'),

]
