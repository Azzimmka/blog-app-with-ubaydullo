from django.urls import path

from .views import (
    category_page_view,
    detail_articles,
    detail_slug_articles,
    home,
    our_team,
    add_article_form
)

urlpatterns = [
    path('', home, name='home'), # type: ignore
    path('detail/<int:pk>/', detail_articles, name='detail'), # type: ignore
    path('slug-detail/<slug:slug>', detail_slug_articles, name='slug-detail'), # type: ignore
    path('category/<int:category_id>', category_page_view, name='category'), # type: ignore
    path('our-team/', our_team, name='our-team'),  # type: ignore
    path('add-article/', add_article_form, name='form') # type: ignore
]
