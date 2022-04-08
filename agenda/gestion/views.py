from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET','POST'])
def inicio(request):
    return Response(data={
        "message":"Bienvenido a mi API de agenda"
    })
