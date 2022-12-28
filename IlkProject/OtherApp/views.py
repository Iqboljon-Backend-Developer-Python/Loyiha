from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SliderPageView(TemplateView):
    template_name = 'home-slider.php.html'
    
class CartPageView(TemplateView):
    template_name = 'cart.php.html'
    
class ShopPageView(TemplateView):
    template_name = 'shop.php.html'
    
class Single_ProductsPageView(TemplateView):
    template_name = 'single-product.php.html'