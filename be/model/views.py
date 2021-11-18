from django.db.models import base
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

import base64
from django.core.files.base import ContentFile
import datetime

from .models import PredictModel
from .serializers import PredictModelSerializer
from .constant import *

# Create your views here.


class PredictView(ViewSet):
    queryset = PredictModel.objects.all()
    serializer_class = PredictModelSerializer
    parser_classes = [JSONParser, ]

    @action(detail=True, method=["get"])
    def list(self, request):
        return Response("test")

    @action(detail=True, method=["post"])
    def create(self, request):
        img_data = request.data
        fm, imgstr = img_data.split(IMG_DATA_SPLITTER)
        ext = fm.split(IMG_EXT_SPLITTER)[-1]
        filename = IMG_FULLNAME_FORMAT.format(
            filename=datetime.datetime.now().strftime(TIME_STRING_FORMAT),
            ext=ext)
        data = ContentFile(base64.b64decode(imgstr), name=filename)

        img = PredictModel.objects.create(img=data)
        img.save()

        return Response("ok", status=status.HTTP_200_OK)
