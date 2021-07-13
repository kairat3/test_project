from django.urls import path
from . import views


urlpatterns = [
    path('articles/create/', views.ArticleCreateView.as_view()),
    path('articles/', views.ArticleListView.as_view()),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view()),
    path('articles/<int:pk>/update/', views.ArticleUpdateView.as_view()),
    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('categories/create/', views.CategoryCreateView.as_view()),
    path('categories/delete/<slug:pk>/', views.CategoryDeleteView.as_view()),
]
