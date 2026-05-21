from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Category, Our_team
# Create your views here.
from .forms import ArticlesForms


def home(request):
    # ['title', 'description', 'views', ...]
    articles = Articles.objects.all()
    categories = Category.objects.all()
    context = {'articles': articles, 'categories': categories}
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
    # greater than your car equal --> gt
    popular_articles = Articles.objects.filter(view__gt=15)
    
    article.view += 1
    article.save(update_fields=['view'])
    

    
    return render(request, 'slug-detail.html', {"article": article, 'popular_articles': popular_articles})


def category_page_view(request, category_id):
    articles = Articles.objects.filter(category=category_id)
    categories = Category.objects.all()
    

    return render(request, 'category-page.html', {"articles": articles, 'categories': categories})



def our_team(request):
    teams = Our_team.objects.all()
    
    context = {'teams': teams}
    
    return render(request, 'our-teams.html', context)
    
    

def add_article_form(request):
    if request.method == 'POST':
        form = ArticlesForms(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home') #type: ignore
    else:
        form = ArticlesForms()
        
    context = {
        'form': form
    }
        
    return render(request, 'add-article.html', context)
