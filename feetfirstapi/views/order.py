from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from feetfirstapi.models import Order
from feetfirstapi.views.user_view import UserSerializer

class OrderView(ViewSet):
    """Feet First Customer View"""
    def retrieve(self, request, pk):
        """GET request for a single user"""
        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of users"""
        orders = Order.objects.all()
        order = request.query_params.get('user')
        orders = orders.filter(customer_id=order)
        serializer = OrderSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)
    
class OrderSerializer(serializers.ModelSerializer):
  """JSON serializer for categories"""
  customer_id = UserSerializer()
  class Meta:
      model = Order
      fields = ('id', 'customer_id', 'date_placed', 'open')
      depth = 1