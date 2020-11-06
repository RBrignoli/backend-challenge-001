"""
API V1: Post Views
"""
###
# Libraries
###
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from post.api.v1.serializers import PostSerializer
from post.api.v1.permissions import IsAuthorOrReadOnly
from post.models import post
###
# Filters
###


###
# Viewsets
###

class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


    def filter_queryset(self, queryset):
        topic_urlname = self.kwargs.get('topic_URLName')
        return queryset.filter(topic__URLName=topic_urlname)