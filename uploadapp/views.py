from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import ImageSerializer

class ImageUploadView(APIView):
    permission_classes = (permissions.IsAuthenticated,) # Set permissions policy
    parser_class = (MultiPartParser)


    def post(self, request, *args, **kwargs):
        file_serializer = ImageSerializer(data = request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)