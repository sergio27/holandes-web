from rest_framework import serializers
from core.models import Word, Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects"""
    class Meta:
        model = Category
        fields = ('name',)
        read_only_fields = ('id',)


class WordSerializer(serializers.ModelSerializer):
    """Serializer for word objects"""
    category = CategorySerializer()

    class Meta:
        model = Word
        fields = ('spanish', 'dutch', 'level', 'category',)
        read_only_fields = ('id',)
