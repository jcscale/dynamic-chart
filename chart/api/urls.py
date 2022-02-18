from django.urls import path
from rest_framework import urlpatterns
from chart.api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('data/', views.ChartListView.as_view())
]
