from django.contrib import admin
from news.models import Article, Comment

# Register your models here.


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [CommentAdmin]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)