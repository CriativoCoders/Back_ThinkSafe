from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from app.models import Aluno, Curso, Turma, User
from app.serializers import AlunoSerializer, CursoSerializer, TurmaSerializer
from rest_framework import generics

class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_instructor

class AlunoView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CursoView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TurmaView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def post(self, request):
        serializer = TurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AlunoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    
class CursoListView(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class TurmaListView(generics.ListAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

