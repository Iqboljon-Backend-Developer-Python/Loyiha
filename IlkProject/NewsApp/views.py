from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class CheckPageView(TemplateView):
    template_name = 'checkout.php.html'
    
class NewsPageView(TemplateView):
    template_name = 'news.php.html'
    
class SingleNewsPageView(TemplateView):
    template_name = 'single-news.php.html'