from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from .serializers import CategorySerializer, TransactionSerializer, InvestmentSerializer, RegisterSerializer
from .models import Category, Transaction, Investment


class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'type', 'amount']

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


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class SummuryView(APIView):
    def get(self, request):
        total_expenses = Transaction.objects.filter(user=self.request.user, type='wydatek').aggregate(Sum('amount'))['amount__sum'] or 0
        total_income = Transaction.objects.filter(user=self.request.user, type='przychod').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expenses
        total_invested = Investment.objects.filter(user=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
        
        response_data = {
            'total_expenses': total_expenses,
            'total_revenues': total_income,
            'balans': balance,
            'total_investments': total_invested
        }

        return Response(response_data)








