from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AlunoView, CursoView, TurmaView, AlunoListView, CursoListView, TurmaListView, AlunoDeleteView, CursoDeleteView # não edsquecer de importar os delete dos curso, turma
# Definindo endpoints utilizando class-based views
urlpatterns = [
    # JWT Authenticação
    path('token/', TokenObtainPairView.as_view(), name=''),
    path('token/refresh/', TokenRefreshView.as_view(), name=''),
    
    # Aluno
    path('aluno/', AlunoView.as_view(), name='criar_aluno'), # POST para criar aluno
    path('aluno/list/', AlunoListView.as_view(), name='listar_alunos'), # GET para listar alunos
    path('aluno/delete/', AlunoDeleteView.as_view(), name='deletar_alunos'), # Deletar alunos.
    
    # Curso
    path('curso/', CursoView.as_view(), name='criar_curso'), # POST para criar cruso
    path('curso/list/', CursoListView.as_view(), name='listar_cursos'), # GET  para listar curso
    path('curso/delete/', CursoDeleteView.as_view(), name='deletar_curso'), # deletar cursos
    
    # Turma
    path('turma/', TurmaView.as_view(), name='criar_turma'), # POST para criar turma
    path('turma/list/', TurmaListView.as_view(), name='listar_turmas'), # GET para listar turmas
    path('turma/delete/', TurmaDeleteView.as_view(), name='deletar Turma'), # deletar turma 
    
    
]