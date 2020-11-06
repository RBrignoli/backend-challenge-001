"""
Comment Models
"""
###
# Libraries
###
from django.contrib.auth.models import models
from post.models import post
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
class comment(models.Model):
    title = models.CharField(max_length=255)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title