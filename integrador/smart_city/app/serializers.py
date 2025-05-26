from rest_framework import serializers
from .models import Sensores, Ambientes, Historico


class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        fields = '__all__'

class AmbientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        fields = '__all__'

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'