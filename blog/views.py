from django.shortcuts import render, get_object_or_404
from .models import Articles
# Create your views here.


def home(request):
    # ['title', 'description', 'views', ...]
    articles = Articles.objects.all()
    return render(request, 'index.html', context={'articles': articles})


# id and pk - primary key
def detail_articles(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    my_context = {
        'title': 'detail',
        'article': article
    }
    return render(request, 'detail.html', context=my_context)