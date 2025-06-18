from rest_framework import serializers
from app.models import Aluno, Curso, Turma, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_instructor']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_instructor=validated_data.get('is_instructor', False)
        )
        return user

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