"""
API V1: Topic Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

from topic.api.v1.views import TopicViewSet
from post.api.v1.views import PostViewSet
from comment.api.v1.views import CommentViewSet

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet, basename='topic')

topic_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
topic_router.register(r'posts', PostViewSet, basename='post')

post_router = routers.NestedSimpleRouter(topic_router, r'posts', lookup='post')
post_router.register(r'comments', CommentViewSet, basename='comment')

###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(topic_router.urls)),
    url(r'^', include(post_router.urls)),
]

