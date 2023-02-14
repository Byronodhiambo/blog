from django.contrib import admin
from .models import Thread, Post, Message, Relationship, Event

# Register your models here.

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Relationship)
admin.site.register(Event)
