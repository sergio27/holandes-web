from rest_framework import serializers
from core.models import Word, Category


class WordSerializer(serializers.ModelSerializer):
    """Serializer for word objects"""
    class Meta:
        model = Word
        fields = ('spanish', 'dutch', 'category')
        read_only_fields = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects"""
    class Meta:
        model = Category
        fields = ('name')
        read_only_fields = ('id',)
