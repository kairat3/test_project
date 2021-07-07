from django.contrib import admin

from app.models import Category, Article, ArticleImages

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ArticleImages)