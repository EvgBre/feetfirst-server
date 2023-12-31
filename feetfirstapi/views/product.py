from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from feetfirstapi.models import Category,Product, User, FavoriteProduct, OrderProduct, Order


class ProductView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
          return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        products = Product.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(uid=uid)
        orders = Order.objects.filter(customer_id=user)
        for product in products:
            product.favorite = len(FavoriteProduct.objects.filter(
                user=user, product=product
            )) > 0
        for product in products:
            product.incart = len(OrderProduct.objects.filter(
            order_id__in=orders,  # Using the retrieved Order instances
            product_id=product,
        )) > 0
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def create(self, request):
 
       
        catId = Category.objects.get(pk=request.data["categoryId"])

        product = Product.objects.create(
            title=request.data["title"],
            image_url=request.data["imageUrl"],
            description=request.data["description"],
            price=request.data["price"],
            added_on=request.data["addedOn"],
            category_id=catId,
            
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk):

        product = Product.objects.get(pk=pk)
        product.title = request.data["title"]
        product.image_url=request.data["imageUrl"]
        product.description=request.data["description"]
        product.price=request.data["price"]
        product.category_id= Category.objects.get(pk=request.data["categoryId"])

        product.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
    
    def destroy(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def favorite(self, request, pk):
        """Post request for a user to sign up for an event"""

        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        product = Product.objects.get(pk=pk)
        FavoriteProduct.objects.create(
            product=product,
            user=user
    )
        return Response({'message': 'Made favorite'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def unfavorite(self, request, pk):
        """Delete request for a user to leave an event"""

        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        product = Product.objects.get(pk=pk)
        favorite = FavoriteProduct.objects.get(
            product=product,
            user=user
        )
        favorite.delete()

        return Response({'message': 'Remove favorite'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def add(self, request, pk):
        """Post request for a user to sign up for an event"""

        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        product = Product.objects.get(pk=pk)
        order, _ = Order.objects.get_or_create(customer_id=user, open=True)
        OrderProduct.objects.create(
            product_id=product,
            order_id=order
    )
        return Response({'message': 'Made favorite'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def remove(self, request, pk):
        """Delete request for a user to leave an event"""

        user = User.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        order = Order.objects.get(customer_id=user, open=True)
        product = Product.objects.get(pk=pk)
        cart_products = OrderProduct.objects.filter(product_id=product, order_id=order)
        cart_products.delete()
        if not OrderProduct.objects.filter(order_id=order).exists():
            order.delete()

        return Response({'message': 'Remove favorite'}, status=status.HTTP_204_NO_CONTENT)

class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Product
        fields = ('id', 'title', 'image_url', 'description', 'price', 'added_on', 'category_id', 'favorite', 'incart')
        depth = 1