from django.http import JsonResponse
from django.shortcuts import render
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

def datos_estudiante(request):
    data={
        'nombre':'Felipe Alvarez',
        'rut':'19.478.868-1',
        'seccion':'Programación Back End (IEI-171-N4)'
    }
    return JsonResponse(data)

#api Inscritos
#Class Based Views

class InscritoList(APIView):
    def get(self, request, format=None):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
class InscritoDetail(APIView):
    def get_object(self, id):
        try:
            return Inscrito.objects.get(id=id)
        except Inscrito.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Function Based Views
@api_view(['GET', 'POST'])
def inscrito_list(request):
    if request.method == 'GET':
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def inscrito_detail(request, id):
    try:
        inscrito = Inscrito.objects.get(id=id)
    except Inscrito.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#api Instituciones
#Class Based Views

class InstitucionList(APIView):
    def get(self, request, format=None):
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
class InstitucionDetail(APIView):
    def get_object(self, id):
        try:
            return Institucion.objects.get(id=id)
        except Institucion.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        institucion = self.get_object(id)
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        institucion = self.get_object(id)
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        institucion = self.get_object(id)
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Function Based Views
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detail(request, id):
    try:
        institucion = Institucion.objects.get(id=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)