from django.urls import path
from .views import ShortenView, RedirectView, StatsView

urlpatterns = [
    path('shorten/', ShortenView.as_view(), name='shorten'),
    path('<str:code>/', RedirectView.as_view(), name='redirect'),
    path('stats/<str:code>/', StatsView.as_view(), name='stats'),
]
