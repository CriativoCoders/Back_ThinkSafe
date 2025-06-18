from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Aluno, Curso, Turma
from app.serializers import AlunoSerializer, CursoSerializer, TurmaSerializer, UserSerializer
from rest_framework import generics, status
import logging

# permissão personalizada para o instrutor 
class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_instrutor

logger = logging.getLogger(__name__)

class UserView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"error": "Erro de validação", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            return Response({"error": "Erro de integridade", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Erro interno", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# criar aluno
class AlunoView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def post(self, request):
        try:
            serializer = AlunoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Aluno criado com sucesso: {serializer.data}")
                return Response(
                    {"message": "Aluno criado com sucesso", "data": serializer.data}, 
                    status=HTTP_201_CREATED
                )
            logger.warning(f"Erro de validação ao criar aluno: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Erro ao criar aluno: {str(e)}")
            return Response(
                {"Erro": "Erro interno ao criar aluno"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
# criar Curso                
class CursoView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def post(self, request):
        try:
            serializer = CursoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Curso criado: {serializer.data}")
                return Response(
                    {"message": "Curso criado com sucesso", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
            logger.warning(f"Erro de validção ao criar curso: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Erro ao criar curso: {str(e)}")
            return Response(
                {"erro": "Erro interno ao criar curso"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
           
# Criar Turma
class TurmaView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def post(self, request):
        try:
            serializer = TurmaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Turma criada: {serializer.data}")
                return Response(
                    {"message": "Turma criada com sucesso", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
            logger.warning(f"Erro de validção ao criar Turma: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Erro ao criar Turma: {str(e)}")
            return Response(
                {"erro": "Erro interno ao criar Turma"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Lista de aluno
class AlunoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

# Lista de curso
class CursoListView(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# Lista de Turma
class TurmaListView(generics.ListAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
 
    
# Deletar aluno
class AlunoDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]
    
    def delete(self, request, pk):
        try:
            aluno = Aluno.objects.get(pk=pk)
            aluno.delete()
            return Response({"message": "Aluno deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Aluno.DoesNotExist:
            return Response({"Error": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Erro ao deletar aluno: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# Deletar curso
class CursoDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]
    
    def delete(self, request, pk):
        try:
            curso = Curso.objects.get(pk=pk)
            curso.delete()
            return Response({"message": "Curso deletado com sucesso"}, status=status.HTTP_204_NO_CONTENT)
        except Curso.DoesNotExist:
            return Response({"Erro": "Curso não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": f"Erro ao deletar curso: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Deletar Turma
class TurmaDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def delete(self, request, pk):
        try:
            turma = Turma.objects.get(pk=pk)
            turma.delete()
            return Response({"message": "Turma deletada com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Turma.DoesNotExist:
            return Response({"Erro": "Turma não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": f"Erro ao deletar Turma: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    

