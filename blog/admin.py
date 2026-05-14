from django.contrib import admin

from .models import Category, Articles, Our_team

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'view']
    list_filter = ['category']
    readonly_fields = ['view']
    prepopulated_fields = {"slug": ('title',)}

admin.site.register(Articles, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Our_team)

