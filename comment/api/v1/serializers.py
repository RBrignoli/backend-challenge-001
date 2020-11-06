"""
API V1: Comment Serializers
"""

###
# Libraries
###
from rest_framework import serializers
from comment.models import comment


###
# Serializers
###
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ('title', 'Author', 'content', 'created_at', 'updated_at', 'post')
