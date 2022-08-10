import imp
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderItem, Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
# Create your views here.


class ProductList(ListCreateAPIView):

    def get_queryset(self):
        return Product.objects.select_related('collection').all()

    def get_serializer_class(self):
        return ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetail(APIView):
    def get(self, request ,id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self, request):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
    def delete(self, request):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view()
def collection_detail(request, pk):
    return Response('Ok')