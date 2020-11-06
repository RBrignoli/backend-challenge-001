"""
API V1: Post Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

from post.api.v1.views import PostViewSet
###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')


###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
]