from rest_framework import serializers
from  tutoriales.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ( 'id',
                   'Tatuador',
                   'Fecha',
                   'Hora',
                   'Imagen',
                   'Descripcion')