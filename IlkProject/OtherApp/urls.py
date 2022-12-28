from django.urls import path
from .views import SliderPageView, CartPageView, ShopPageView, Single_ProductsPageView

urlpatterns = [
    path('',SliderPageView.as_view(),name='slider'),
    path('cart/',CartPageView.as_view(),name='cart'),
    path('shop/',ShopPageView.as_view(),name='shop'),
    path('single_products/',Single_ProductsPageView.as_view(),name='single_products')
]