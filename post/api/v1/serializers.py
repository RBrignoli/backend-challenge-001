"""
API V1: post Serializers
"""
###
# Libraries
###
from rest_framework import serializers

from post.models import post


###
# Serializers
###
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = post
        fields = ('title', 'Author', 'content','created_at', 'updated_at', 'topic')

