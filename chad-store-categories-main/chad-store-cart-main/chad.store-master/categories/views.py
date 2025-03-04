from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from categories.serializers import CategorySerializer, CategoryDetailSerializer, CategoryImageSerializer
from categories.models import Category, CategoryImage

class CategoryListView(ListModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class CategoryDetailView(ListModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class CategoryImageListView(ListModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(category=self.kwargs['category_id'])
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)