from rest_framework import viewsets, mixins

from core.models import Word, Category
from words.serializers import WordSerializer, CategorySerializer


class WordViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage words in the database"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        """Return word objects"""
        queryset = self.queryset

        level = self.request.query_params.get("level")
        category = self.request.query_params.get('category')

        if level:
            queryset = queryset.filter(level=level)
        if category:
            category_id = Category.objects.get(name=category)
            queryset = queryset.filter(category_id=category_id)

        return queryset.order_by('category', 'spanish')


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage categories in the database"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        """Return category objects"""
        return self.queryset.order_by('name')
