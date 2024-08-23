from rest_framework import viewsets
from .models import Item, Book
from .serializers import ItemSerializer, BookSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# books/views.py

from rest_framework import generics
from elasticsearch_dsl import Q
from .documents import ItemDocument
from .serializers import ItemSerializer

class SearchItemView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            q = Q(
                'multi_match',
                query=query,
                fields=['title', 'author'],
            )
            return ItemDocument.search().query(q)
        return ItemDocument.search()



class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer