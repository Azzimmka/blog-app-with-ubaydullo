from django.urls import  path

from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail_articles, name='detail'),
    path('slug-detail/<slug:slug>', detail_slug_articles, name='slug-detail'),
    path('category/<int:category_id>', category_page_view, name='category'),
    path('our-team/', our_team, name='our-team')
]