from django.shortcuts import render
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class ProductsView(APIView):
    
    def get(self,request):
        products=Products.objects.all()
        serializer=ProductSerializers(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        permission_classes=(IsAuthenticated,)
        serializer=ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UpdateProductView(APIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    def put(self,request,id):
        product=Products.objects.get(id=id)
        serializer=ProductSerializers(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        try:
            product=Products.objects.get(id=id)
        except Products.DoesNotExist:
            return Response({"messege":"BU mavjud emas"})
        product.delete()
        return Response({"messege":"Muvaffaqiyatli O'chirildi"})
        
        
    
    
        
