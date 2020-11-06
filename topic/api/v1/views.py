"""
API V1: Topic Views
"""
###
# Libraries
###
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from topic.api.v1.serializers import TopicSerializer
from topic.api.v1.permissions import IsAuthorOrReadOnly
from topic.models import topic
###
# Filters
###


###
# Viewsets
###

class TopicViewSet(viewsets.ModelViewSet):
    queryset = topic.objects.order_by('-created_at')
    serializer_class = TopicSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'URLName'


