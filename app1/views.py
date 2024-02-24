
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import TechB

from .serializers import TechBSerializers

def Add_task(request):
    try:
        serializer = TechBSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(data=serializer.errors)


@api_view(http_method_names=['PUT','PATCH'])
def Edit_task(request, pk=None):
    try:
        eid = TechB.objects.get(eid, pk=pk)
        if request.method == 'PUT':
            serializer = TechBSerializers(data=request.data, instance=eid)
        if request.method == 'PATCH':
            serializer = TechBSerializers(data=request.data, instance=eid)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail':'Error updating data'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['DELETE'])
def delete_task(request, pk=None):
    try:
        eid = TechB.objects.get(eid, pk=pk)
        eid.delete()
        return Response(data={'detail':'task deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail':'Error deleting task'}, status=status.HTTP_400_BAD_REQUEST)




