from django.contrib import admin

from .models import Category, Articles

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'view']
    list_filter = ['category']
    readonly_fields = ['view']

admin.site.register(Articles, ArticleAdmin)
admin.site.register(Category)
