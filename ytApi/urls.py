from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from ytApi import views

app_name = 'ytApi'

urlpatterns = [
    
    path('api/<qu>/', views.snippet_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)