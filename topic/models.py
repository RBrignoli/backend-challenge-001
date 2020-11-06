"""
Topic Models
"""
###
# Libraries
###
from django.contrib.auth.models import models
from accounts.models import User

###
# Choices
###


###
# Querysets
###


###
# Models
###
class topic(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    URLName = models.SlugField(max_length=255, unique=True)


    def __str__(self):
        return self.title