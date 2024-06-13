from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.news_view, name='index'),
    path('news_detail/<int:pk>/', views.news_detail, name='detail')
]
