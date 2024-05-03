# views.py
from rest_framework import generics
from .models import Column
from .serializers import ColumnSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ColumnSerializer
class CreateColumnAPIView(generics.CreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    # authentication_classes = [JWTAuthentication]  # Specify JWTAuthentication for token-based authentication
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ColumnRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Column.objects.all()
    authentication_classes = [JWTAuthentication]
    serializer_class = ColumnSerializer
    permission_classes = [AllowAny]

    def put(self, request):
        column = self.get_object()
        serializer = ColumnSerializer(column, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request):
        column = self.get_object()
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

