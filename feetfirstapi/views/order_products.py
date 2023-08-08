from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from feetfirstapi.models import FavoriteProduct, User

class FavoriteProductView(ViewSet):
    """Feet First Customer View"""
    def retrieve(self, request, pk):
        """GET request for a single user"""
        try:
            favorite_product = FavoriteProduct.objects.get(pk=pk)
            serializer = FavoriteProductSerializer(favorite_product)
            return Response(serializer.data)
        except FavoriteProduct.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of users"""
        favorite_products = FavoriteProduct.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)
        favorite_products = favorite_products.filter(user_id = user)
        serializer = FavoriteProductSerializer(favorite_products, many=True, context={'request': request})
        return Response(serializer.data)
    
class FavoriteProductSerializer(serializers.ModelSerializer):
  """JSON serializer for categories"""
  
  class Meta:
      model = FavoriteProduct
      fields = ('id', 'product', 'user')
      depth = 1