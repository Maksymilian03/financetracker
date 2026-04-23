from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_category = models.CharField(max_length=32)

    def __str__(self):
         return f"{self.user} - {self.transaction_category}" 

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class TransactionType(models.TextChoices):
            WYDATEK = 'wydatek', 'Wydatek'
            PRZYCHOD = 'przychod', 'Przychód'
    type = models.CharField(max_length=10, choices=TransactionType.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
         return f"{self.user}, {self.type} - {self.amount}"



class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class InvestmentType(models.TextChoices):
        AKCJE = 'akcje', 'Akcje'
        ETF =  'ETF', 'ETF'
        OBLIGACJE = 'obligacje', 'Obligacje'
    type = models.CharField(max_length=10, choices=InvestmentType.choices)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
         return f"{self.user}, {self.type} - {self.amount}"


