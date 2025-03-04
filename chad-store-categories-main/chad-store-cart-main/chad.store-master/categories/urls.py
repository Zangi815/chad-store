from django.urls import path
from categories.views import CategoryDetailView, CategoryListView, CategoryImageListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('categories/<int:category_id>/images/', CategoryImageListView.as_view(), name='images'),
]
