"""
Comment admin
"""
###
# Libraries
###
from django.contrib import admin
from .models import comment

###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "Author", "post", "created_at", "updated_at")
