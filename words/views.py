from rest_framework import viewsets, mixins

from core.models import Word, Category
from .serializers import WordSerializer, CategorySerializer


class WordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage meals in the database"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        """Return objects"""
        return self.queryset.order_by('category', 'spanish')


class CateogryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage diets in the database"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Return objects"""
        return self.queryset.order_by('name')
