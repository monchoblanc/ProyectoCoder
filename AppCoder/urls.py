from django.urls import path
from AppCoder.views import * #en clase estaba como: from .views import*

urlpatterns = [
    path('', inicio, name='inicio'),         #en filminas era: path('cursos/', views.cursos), e idem en todas....
    path('cursos/', cursos, name='cursos'), #este name es p q lo tome en el padre.html como referencia al url en el boton
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables, name='entregables'),
    #me falta poner el padre aca? NO! no hace falta
]