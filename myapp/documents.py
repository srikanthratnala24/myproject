# books/documents.py

from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Item

# Define the Elasticsearch index
item_index = Index('items')

# Document definition
@registry.register_document
@item_index.document
class ItemDocument(Document):
    name = fields.TextField(attr='name')
    class Index:
        name = 'items'

    class Django:
        model = Item  # The model associated with this Document
        fields = [
            
        ]
