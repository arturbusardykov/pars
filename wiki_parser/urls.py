# wiki_parser/urls.py
from django.urls import path
from api.views import parse_wikipedia

urlpatterns = [
    path('parse_wikipedia/<str:title>/', parse_wikipedia),
]
