from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date_time']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['sensor_id', 'sensor_name', 'description', 'measurements']


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['sensor_id', 'sensor_name', 'description']


class MeasurementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature']



