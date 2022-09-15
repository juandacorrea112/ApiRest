from django.urls import path

from tutoriales import views

urlpatterns = [
    path('api/tutoriales',views.tutorial_lista),
    path('api/tutoriales/<int:id>', views.tutorial_detalle),
]