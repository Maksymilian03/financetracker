from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, InvestmentViewSet, TransactionViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('transaction', TransactionViewSet, basename='transaction')
router.register('investment', InvestmentViewSet, basename='investment')

urlpatterns = [
    path('', include(router.urls)),
]