from django.urls import path
from .views import CheckPageView, NewsPageView, SingleNewsPageView

urlpatterns = [
    path('',CheckPageView.as_view(),name='check'),
    path('news/',NewsPageView.as_view(),name='news'),
    path('single_news',SingleNewsPageView.as_view(),name='single_news')
]
