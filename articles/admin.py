from django.contrib import admin
from .models import Articles

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']

admin.site.register(Articles, ArticleAdmin)