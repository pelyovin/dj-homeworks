from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Review

from .serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer, ProductFilteredSerializer


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound('Product not found')
        ser = ProductDetailsSerializer(product)
        return Response(ser.data)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        mark = request.query_params.get('mark')
        if mark:
            product = Review.objects.filter(product=product_id, mark=mark)

        else:
            product = Review.objects.filter(product=product_id)
        ser = ProductFilteredSerializer(product, many=True)
        return Response(ser.data)
