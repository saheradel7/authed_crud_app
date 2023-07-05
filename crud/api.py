#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework import status
from crud.serializer import UserSerializer
from django.http import Http404



class UserDetail(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        req_data = request.data
        serializer = UserSerializer(data = req_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"user added successfully"}, status= status.HTTP_200_OK)
        return Response ({"msg":"user data invalid"},status= status.HTTP_400_BAD_REQUEST)
    
class UserInfo(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

    def put(self, request, id, format=None):
        req_data = request.data
        try:
            user = self.get_object(id)
        except User.DoesNotExist:
            return Response({"msg":"user not found"} , status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(user, data=req_data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        return Response({"msg":"invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, id, format=None):
        req_data = request.data
        try:
            user = self.get_object(id)
        except User.DoesNotExist:
            return Response({"msg":"user not found"} , status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(user, data=req_data,partial=True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        return Response({"msg":"invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id,format=None):
        try:
            user = self.get_object(id)
        except User.DoesNotExist:
            return Response({"msg":"user not found"} , status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response({"msg":"user deleted"} , status=status.HTTP_200_OK)
    


        

    









""" 

@api_view(['GET', 'POST'])
def user_list(request):
    
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 """