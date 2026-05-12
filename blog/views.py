from django.shortcuts import render, get_object_or_404
from .models import Articles, Category
# Create your views here.


def home(request):
    # ['title', 'description', 'views', ...]
    articles = Articles.objects.all()
    categories = Category.objects.all()
    context = {
        'articles': articles,
        "categories": categories}
    return render(request, 'index.html', context=context)


# id and pk - primary key
def detail_articles(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    my_context = {
        'title': 'detail',
        'article': article
    }
    return render(request, 'detail.html', context=my_context)


def detail_slug_articles(request, slug):
    article = Articles.objects.get(slug=slug)
    
    return render(request, 'slug-detail.html', {"article": article})


def category_page_view(request, category_id):
    articles = Articles.objects.filter(category=category_id)
    

    return render(request, 'category-page.html', {"articles": articles})