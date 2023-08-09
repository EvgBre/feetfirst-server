from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from feetfirstapi.models import OrderProduct, User, Order
from feetfirstapi.views.product import ProductSerializer

class OrderProductView(ViewSet):
    """Feet First Customer View"""
    def retrieve(self, request, pk):
        """GET request for a single user"""
        try:
            order_product = OrderProduct.objects.get(pk=pk)
            serializer = OrderProductSerializer(order_product)
            return Response(serializer.data)
        except OrderProduct.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of users"""
        order_products = OrderProduct.objects.all()
        # order = request.query_params.get('order')
        # order_products = order_products.filter(order_id=order)
        serializer = OrderProductSerializer(order_products, many=True, context={'request': request})
        return Response(serializer.data)
    
class OrderProductSerializer(serializers.ModelSerializer):
  """JSON serializer for categories"""
  product_id = ProductSerializer()
  class Meta:
      model = OrderProduct
      fields = ('id', 'product_id', 'order_id')
      depth = 1