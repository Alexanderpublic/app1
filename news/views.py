from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import Article, Comment
from .forms import CommentForm
from django.contrib import auth


def search(request):
    return render(request, 'createNews.html')


def articles(request):
    return render(request,'articles.html', {'articles': Article.objects.all(), 'username': auth.get_user(request).username})


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comment_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article.html', args)


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_article = Article.objects.get(id=article_id)
            comment.creator = auth.get_user(request).username
            form.save()
    return redirect('/news/get/%s' % article_id)