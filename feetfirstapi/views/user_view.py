from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from feetfirstapi.models import User

class UserView(ViewSet):
    """Feet First Customer View"""
    def retrieve(self, request, pk):
        """GET request for a single user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """GET request for a list of users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
    
    # def create(self, request):
    #     """POST request for creating a user for testing in Postman
    #        NOT USED for actual creation on client side"""
    #     user = User.objects.create(
    #         first_name = request.data['first_name'],
    #         last_name = request.data['last_name'],
    #         email = request.data['email'],
    #         username = request.data['username'],
    #         profile_image_url = request.data['profile_image_url'],
    #         uid = request.data['uid']
    #     )
    #     user.save()
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a user"""
        user = User.objects.get(pk=pk)
        uid = request.META['HTTP_AUTHORIZATION']
        user.first_name = request.data['firstName']
        user.last_name = request.data['lastName']
        user.email = request.data['email']
        user.username = request.data['username']
        user.profile_image_url = request.data['profileImageUrl']
        user.uid = uid
        user.save()
        return Response({'message': 'User UPDATED'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to delete a user"""
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message': 'User DESTROYED'}, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'profile_image_url',
                  'email',
                  'username',
                  'uid')
        depth = 1