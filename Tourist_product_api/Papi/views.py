from itertools import product
from typing import Generic
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize

from Papi.forms import CreateProducts
from .serializes import ProductSelializer
from .models import Product
from rest_framework import generics,status
from . import serializes

# Create your views here.


def productview(request):
    return render(request, 'Papi/product.html')

""" @api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list',
        'Detail view ': 'product-detail/<int:id>',
        'Create': 'product-create/',
        'update': 'product-update/<int:id>',
        'Delete': 'product-delete/<int:id>',
    }
    return Response(api_urls)"""

@api_view(['GET'])
def ShowAll(request):
    product = Product.objects.all()
    serializer = ProductSelializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewproduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSelializer(product, many=False)
    return Response(serializer.data)

       

# @api_view(['POST'])
# def Createproduct(request):
#     serializer = ProductSelializer(data= request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)



@api_view(['POST'])
def Updateproduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSelializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)    

@api_view(['GET'])
def deleteproduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response("successfully")


class ProductCreateView(generics.GenericAPIView):
    serializer_class = serializes.ProductSelializer

    def post(self, request):
        data =request.data

        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    




def create_Peoduct_View(request):
    form = CreateProducts()
    if request.method == 'POST':
        form = CreateProducts(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create_product.html', {'form': form})