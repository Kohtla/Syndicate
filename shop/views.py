from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'shop/product_detail.html'