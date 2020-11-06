"""
Post Models
"""
###
# Libraries
###
from django.contrib.auth.models import models
from topic.models import topic
from accounts.models import User

###
# Choices
###


###
# Querysets
###


###
# Models
class post(models.Model):
    title = models.CharField(max_length=255)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(topic, on_delete=models.CASCADE,)


    def __str__(self):
        return self.title