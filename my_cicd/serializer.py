from .models import *
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    # categories = BlogCategorySerial(many=True,read_only=True)
    class Meta:
        model = Blog
        fields = ["id", "name", "slug"]

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug', 'status']


class BlogCategorySerial(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True,read_only=True)
    class Meta:
        model = BlogCategory
        fields = ["id", "name", "slug", "status", "blogs"]


class BlogSerial(serializers.ModelSerializer):
    categories = BlogCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'name', 'slug', 'categories']

