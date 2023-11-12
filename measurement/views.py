# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorListSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response


class CreateAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class ListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class ListCreateAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

