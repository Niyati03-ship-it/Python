from rest_framework import generics
from myapp.models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from rest_framework import generics
from myapp.models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
