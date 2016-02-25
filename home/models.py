from django.db import models
from django.contrib import admin

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50, db_index = True)
    content = models.TextField()
    created = models.DateTimeField()
    pic = models.CharField(max_length = 100, blank = True)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')

admin.site.register(Article, ArticleAdmin)