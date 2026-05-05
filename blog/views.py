from django.shortcuts import render
from .models import Articles
# Create your views here.


def home(request):
    # ['title', 'description', 'views', ...]
    articles = Articles.objects.all()
    return render(request, 'index.html', context={'articles': articles})
