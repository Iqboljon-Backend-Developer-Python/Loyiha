from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class AboutPageView(TemplateView):
    template_name = 'about.php.html'
    
class four_o_four(TemplateView):
    template_name = '404.php.html'
    
class ContactPageView(TemplateView):
    template_name = 'contact.php.html'