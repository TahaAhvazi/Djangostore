import imp
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderItem, Product, Collection
from .serializers import CollectionSerializer, ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from django.db.models import Count
# Create your views here.


class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

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


class CollectionList(ListCreateAPIView):
    queryset= Collection.objects.annotate(product_count=Count('product')).all()
    serializer_class = CollectionSerializer

class CollectionDetail(RetrieveDestroyAPIView):
    queryset = Collection.objects.annotate(products_count=Count('product'))
    serializer_class=CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.product.count()> 0:
            return Response({'error':'Collection have some products'}, status=status.HTTP_204_NO_CONTENT)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)