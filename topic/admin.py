"""
Topic admin
"""
###
# Libraries
###
from django.contrib import admin
from .models import topic

###
# Inline Admin Models
###


###
# Main Admin Models
###
@admin.register(topic)

class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "Author", "URLName", "created_at", "updated_at")
    prepopulated_fields = {"URLName": ("title",)}