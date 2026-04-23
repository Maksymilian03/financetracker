from django.shortcuts import render

from rest_framework import viewsets
from .serializers import CategorySerializer, TransactionSerializer, InvestmentSerializer
from .models import Category, Transaction, Investment


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)






