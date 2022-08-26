from django.contrib import admin
from .models import User, Snippet, Language

admin.site.register(User)
admin.site.register(Snippet)
admin.site.register(Language)
