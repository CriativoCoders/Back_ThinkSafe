from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AlunoView, CursoView, TurmaView, AlunoListView, CursoListView, TurmaListView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('aluno/', AlunoView.as_view()),
    path('curso/', CursoView.as_view()),
    path('turma/', TurmaView.as_view()),
    path('aluno/list/', AlunoListView.as_view()),
    path('curso/list/', CursoListView.as_view()),
    path('turma/list/', TurmaListView.as_view()),
]