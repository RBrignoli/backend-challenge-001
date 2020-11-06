"""
Topic Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class TopicConfig(AppConfig):
    name = 'topic'

    def ready(self):
        import topic.signals
