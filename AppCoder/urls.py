from django.urls import path
from AppCoder.views import * #en clase estaba como: from .views import*

urlpatterns = [
    path('', inicio),         #en filminas era: path('cursos/', views.cursos), e idem en todas....
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    
]