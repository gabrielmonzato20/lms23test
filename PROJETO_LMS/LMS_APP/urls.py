
from django.urls import path,include
from applms.views import *
urlpatterns = [
    path("",home,name='home'),
    path("aluno/",aluno,name='aluno'),
    path('professor',professor,name='professor'),
    path('disciplina/',disciplina,name='disciplina'),

]
