"""
Post Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class PostConfig(AppConfig):
    name = 'post'

    def ready(self):
        import post.signals
