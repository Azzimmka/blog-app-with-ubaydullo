from django.urls import  path

from .views import home, detail_articles
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail_articles, name='detail')
]