"""
API V1: topic Serializers
"""
###
# Libraries
###
from rest_framework import serializers

from topic.models import topic


###
# Serializers
###
class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = topic
        fields = ('name', 'title', 'Author', 'created_at', 'updated_at', 'URLName')

