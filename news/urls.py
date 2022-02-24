from django.urls import path, re_path
from . import views
app_name='news'
urlpatterns=[
    path('', views.news_today, name='newsToday'),
    path('search', views.search_results, name='search_results'),
    path('article/<int:article_id>', views.article, name='article'),
    path('archives/<str:past_date>/', views.past_days_news, name='pastNews')
]