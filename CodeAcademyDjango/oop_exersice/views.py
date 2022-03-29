import json
import os
from pathlib import Path

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from oop_exersice.serializers import OrdersSerializer

EXERSICE_DIR = os.path.abspath(Path('/home/petar/exersice_materials/').resolve())


class OrdersDBAPI(APIView):
    def get(self, request):
        files = os.listdir(EXERSICE_DIR)
        files.sort(key=lambda name: int(name.split("_")[-1].split(".")[0]))
        return Response(files)


class OrdersPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


class OrdersFileAPI(ListAPIView):
    pagination_class = OrdersPageNumberPagination
    serializer_class = OrdersSerializer

    def get_queryset(self):
        with open(os.path.join(EXERSICE_DIR, self.request.data["file"]), "r") as source:
            return json.load(source)

    def get(self, request, *args, **kwargs):
        if "file" not in self.request.data:
            return Response("file param not provided", status=status.HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)
