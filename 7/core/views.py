from django.shortcuts import render
from rest_framework.views import Response, APIView,status
from .serializers import CustomUserSerializer


class CustomUserRegisterView(APIView):
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)