from django.db import models
from djmoney.models.fields import MoneyField
from django import forms

# Create your models here.

class Warehouse(models.Model):
    title = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    location_url = models.URLField(max_length=500)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='UZS')
    quantity = models.PositiveIntegerField()
    sku=models.PositiveIntegerField()
    add_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    @property
    def total_price(self):
        return self.price * self.quantity

    @property
    def sales_price(self):
        persentage=self.price / 100 
        profit_price=persentage * 15
        return self.price + profit_price

class Customer(models.Model):
    full_name = models.CharField(max_length=255) 
    phone = models.CharField(max_length=13)
    company_title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.full_name

class Delivery(models.Model):
    customery = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    destination = models.CharField(max_length=255)
    destination_url = models.URLField(max_length=500) 
    
    def __str__(self):
        return f'Delivery #{self.id}'
