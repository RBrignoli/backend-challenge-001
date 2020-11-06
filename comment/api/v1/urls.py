"""
API V1: Comment Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from comment.api.v1.views import CommentViewSet

###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'comments',CommentViewSet, basename='comment')


###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
]
