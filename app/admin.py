
# Register your models here.
from django.contrib import admin
from .models import Curso, Turma, Aluno, User
# Instrutor, Local, Evento, Palestrante, Palestra, Card
admin.site.register(User)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Aluno)
# admin.site.register(Instrutor)
# admin.site.register(Local)
# admin.site.register(Evento)
# admin.site.register(Palestrante)
# admin.site.register(Palestra)
# admin.site.register(Card)
