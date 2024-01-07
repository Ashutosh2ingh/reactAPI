from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Table
from .serializers import TableSerializer

class TableAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            table = self.get_object(pk)
            serializer = TableSerializer(table)
        else:
            tables = Table.objects.all()
            serializer = TableSerializer(tables, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        table = self.get_object(pk)
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        table = self.get_object(pk)
        table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
