import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .serializers import ArchivoSerializer, EtiquetaSerializer, PruebaSerializer,TareaSerializer,TareasSerializer
from .models import Etiqueta, Tareas
from rest_framework import status
from django .utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@api_view(http_method_names=['GET','POST'])
def inicio(request: Request):
    print(request.method)
    print(request)
    if request.method == 'GET':
           
        return Response(data={
            "message":"Bienvenido a mi API de agenda"
        })
    elif request.method == 'POST':
        return Response(data={
            "message":"Hice un post"
        },status=201)

class PruebaApiView(ListAPIView):
    serializer_class = PruebaSerializer
    queryset = [{
        'nombre':'Eduardo',
        'apellido':'De Rivero',
        'correo':'ederivero@gmail.com',
        'estado_civil':'Viudo',
        'dni':'74501400'
    },{
        'nombre':'Maria',
        'apellido':'Perez',
        'correo':'ederiv@gmail.com',
        'estado_civil':'casado',
        'dni':'74501401'
    }
    ]
    def get(self,request:Request):
        informacion = self.queryset
        informacion_serializada = self.serializer_class(data=informacion,many=True)
        informacion_serializada.is_valid(raise_exception=True)
        return Response(data={
            'message':'Hola',
            'content': informacion_serializada.data
            })
class TareasApiView(ListCreateAPIView):
    queryset = Tareas.objects.all()
    serializer_class=TareasSerializer

    def post(self,request:Request):
        serializador = self.serializer_class(data=request.data)
        if serializador.is_valid():
            fechaCaducidad = serializador.validated_data.get("fechaCaducidad")
            importancia = serializador.validated_data.get("importancia")
            
            if importancia < 0 or importancia > 10:
                return Response(data={
                    "message":"La importancia puede ser entre 0 y 10"
                },status=status.HTTP_400_BAD_REQUEST)
            
            if timezone.now()>fechaCaducidad:
                return Response(data={
                    "message":"la fecha no puede ser menor que la fecha actual"
                },status=status.HTTP_400_BAD_REQUEST)

            serializador.save()

            return Response(data=serializador.data,status=status.HTTP_201_CREATED)
        else:
            serializador.errors
            return Response(data={"message":"la data no es valida","content":serializador.errors},status=status.HTTP_400_BAD_REQUEST)
class EtiquetasApiView(ListCreateAPIView):
    queryset=Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer
    queryset = Tareas.objects.all()

class ArchivosApiView(CreateAPIView):
    serializer_class=ArchivoSerializer

    def post(self,request:Request):
        print(request.FILES)
        data = self.serializer_class(data=request.FILES)
        if data.is_valid():
            archivo:InMemoryUploadedFile = data.validated_data.get("archivo")
            print(archivo.name)
            resultado = default_storage.save('imagenes/'+archivo.name,ContentFile(archivo.read()))
            print(resultado)
            return Response(data={"message":"archivo guardado exitosamente"},status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message":"Error al subir la imagen",
                "content":data.errors
            },status=status.HTTP_400_BAD_REQUEST)