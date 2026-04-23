from django.shortcuts import render

from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)