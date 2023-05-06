from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    
   path('', views.AlumnoView.as_view(),name='index'),
   path('profesores/', views.ProfesorView.as_view(),name='profesores'),
   path('alumnos/<int:pk>/eliminar/', views.AlumnoView.eliminar_alumno, name='eliminar_alumno'),
   path('profesores/<int:pk>/eliminar/',views.ProfesorView.eliminar_profesor,name='eliminar_profesor')
   
]