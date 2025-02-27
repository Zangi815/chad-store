from django.urls import path, include
from products.views import ProductViewSet, ReviewViewSet, FavoriteProductViewSet, CartViewSet, ProductTagListView, ProductImageViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('favorite_products', FavoriteProductViewSet)


products_router = routers.NestedDefaultRouter(
    router,
    'products',
    lookup='product'
)

products_router.register('images', ProductImageViewSet)
products_router.register('reviews', ReviewViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    path('favorite_products/', FavoriteProductViewSet.as_view({'get':'list', 'post':'create'}), name='favorite_products'),
    path('favorite_product/<int:pk>/', FavoriteProductViewSet.as_view({'get':'retrieve','delete':'destroy'}), name='favorite_product'),
    path('cart/', CartViewSet.as_view(), name='cart'),
    path('tags/', ProductTagListView.as_view(), name='tags'),
]
