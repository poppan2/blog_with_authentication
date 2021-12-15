from rest_framework import serializers
from ..models.blog import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        field = ('id', 'title', 'content', 'author_id')