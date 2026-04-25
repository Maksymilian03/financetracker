from django.shortcuts import render

from rest_framework import viewsets
from .serializers import CategorySerializer, TransactionSerializer, InvestmentSerializer
from .models import Category, Transaction, Investment


class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InvestmentViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Investment.objects.filter(user=self.request.user)
    serializer_class = InvestmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)






