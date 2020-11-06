"""
API V1: Comment Views
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from comment.api.v1.serializers import CommentSerializer
from comment.api.v1.permissions import IsAuthorOrReadOnly
from comment.models import comment
###
# Filters
###


###
# Viewsets
###

class CommentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def filter_queryset(self, queryset):
        post_id = self.kwargs.get('post_pk')
        return queryset.filter(post__id=post_id)