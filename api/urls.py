from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, InvestmentViewSet, TransactionViewSet, RegisterView, SummuryView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('transaction', TransactionViewSet, basename='transaction')
router.register('investment', InvestmentViewSet, basename='investment')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token),
    path('register/', RegisterView.as_view(), name='register'),
    path('summury/', SummuryView.as_view(), name='summury'),
]