from rest_framework import serializers
from app.views import Aluno, Curso, Turma, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_instructor']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'edv', 'data']

class CursoSerializer(serializers.ModelSerializer):
    professor_responsavel = UserSerializer(read_only=True)

    class Meta:
        model = Curso
        fields = ['id', 'nome', 'local', 'professor_responsavel']

class TurmaSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    alunos = AlunoSerializer(many=True, read_only=True)
    professor_responsavel = UserSerializer(read_only=True)

    class Meta:
        model = Turma
        fields = ['id', 'nome', 'curso', 'alunos', 'professor_responsavel']