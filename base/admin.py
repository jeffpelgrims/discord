from django.contrib import admin
from .models import Room, Topic, Message

# Register your models here.

# Lignes pour afficher les différents modèle sur le site django-admin
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)