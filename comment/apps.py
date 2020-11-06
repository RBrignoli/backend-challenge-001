"""
Comment Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class CommentConfig(AppConfig):
    name = 'comment'

    def ready(self):
        import comment.signals
