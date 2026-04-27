from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Category, Transaction
from api.serializers import CategorySerializer
from django.urls import reverse
from django.contrib.auth.models import User


class CategoryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpasword')
        self.client.force_authenticate(user=self.user)

    def test_create_category(self):
        response = self.client.post('/api/category/', {"transaction_category": "Raty"})


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_get_categories(self):
        response = self.client.get('/api/category/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/category/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 


class TransactionTests(APITestCase):
    def setUp(self):
        self.user1= User.objects.create_user(username='testuser', password='testpasword')
        self.user2= User.objects.create_user(username='testuser2', password='testpasword2')
    

    def test_negative_amount_rejected(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post('/api/transaction/', {"type": "wydatek", "category_id": 1, "amount": -100})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_sees_only_own_transactions(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post('/api/category/', {"transaction_category": "Raty"})
        category_id = response.data['id']
        self.client.post('/api/transaction/', {"type": "wydatek", "category_id": category_id, "amount": 2000, "date": "2024-01-01"})
        self.client.post('/api/transaction/', {"type": "wydatek", "category_id": category_id, "amount": 300, "date": "2024-01-01"})

        self.client.force_authenticate(user=None)
        self.client.force_authenticate(user=self.user2)

        response = self.client.post('/api/category/', {"transaction_category": "Subskrybcja"})
        category_id_2 = response.data['id']
        self.client.post('/api/transaction/', {"type": "wydatek", "category_id": category_id_2, "amount": 1000, "date": "2024-01-01"})

        self.client.force_authenticate(user=None)
        self.client.force_authenticate(user=self.user1)

        respons = self.client.get('/api/transaction/')
        self.assertEqual(respons.status_code, status.HTTP_200_OK)
        self.assertEqual(respons.data['count'], 2)


        
        






