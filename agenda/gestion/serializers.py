from pyexpat import model
from django.forms import fields
from rest_framework import serializers
from gestion.models import Etiqueta
from gestion.models import Tareas

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40,trim_whitespace=True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length=8,min_length=8,regex="[0-9]")

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tareas
        fields='__all__'
        extra_kwargs={
            'etiquetas':{
                "write_only":True
            }
        }

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tareas
        fields='__all__'
        depth=1


class EtiquetaSerializer(serializers.ModelSerializer):
    tareas = TareasSerializer(many=True,read_only=True)
    class Meta:
        model = Etiqueta
        fields='__all__'
        read_only_fields = ["nombre"]
class TareaPeronalizableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = "__all__"
        extra_kwargs={
            "nombre":{
                "write_only":True
            }
        }
class ArchivoSerializer(serializers.Serializer):
    
    archivo=serializers.ImageField(max_length=100)