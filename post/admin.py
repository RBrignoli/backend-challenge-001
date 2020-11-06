"""
Post admin
"""
###
# Libraries
###
from django.contrib import admin
from .models import post

###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(post)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "Author", "topic", "created_at", "updated_at")
