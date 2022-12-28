from django.urls import path
from .views import AboutPageView, four_o_four, ContactPageView

urlpatterns = [
    path('',AboutPageView.as_view(),name='aboutapp'),
    path('404',four_o_four.as_view(),name='404'),
    path('contact',ContactPageView.as_view(),name='contact')
]   