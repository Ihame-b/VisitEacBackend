from dataclasses import field
import email
from enum import unique
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.forms import ValidationError
from rest_framework import serializers, status
from .models import Product
from django.db import models


class ProductSelializer(serializers.ModelSerializer):

    class Meta:
        order_status=serializers.HiddenField(default="PENDING")
        model = Product
        fields = '__all__'

    def validate(self,attrs):
        productnameexists=Product.objects.filter(productname=attrs['productname']).exists()
        
        if productnameexists:
            raise serializers.ValidationError(detail="Product with that name exist")
        
        productemailexists=Product.objects.filter(email=attrs['email']).exists()
        
        if productemailexists:
            raise serializers.ValidationError(detail="Product with that email exist")  


        productphoneexists=Product.objects.filter(phone=attrs['phone']).exists()
        
        if productphoneexists:
            raise serializers.ValidationError(detail="Product with that phone exist")

        return super().validate(attrs)
# class productSerializers(serializers.ModelSerializer):
#     productname = models.CharField(max_length=200, null=False, blank=False)
#     campanyemail = models.EmailField(max_length=100, null=False, blank=False)
#     phone =models.CharField(max_length=20, null=False, blank=False)
#     country = models.CharField(max_length=200, null=False, blank=False)
#     category = models.CharField(max_length=200, null=False, blank=False)
#     image =models.ImageField()
#     starts =models.IntegerField()

#     class Meta:
#         model=Product
