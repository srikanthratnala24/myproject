# books/urls.py

from django.urls import path
from .views import SearchItemView

urlpatterns = [
    path('search/', SearchItemView.as_view(), name='search-items'),
]
