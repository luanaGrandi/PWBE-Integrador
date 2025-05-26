from django.urls import path
from .views import AmbienteListCreate, AmbienteRetrieveUpdateDestroy, SensoresRetrieveUpdateDestroy, SensoresListCreate, HistoricoListCreate, HistoricoRetrieveUpdateDestroy
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # AMBIENTES
    path('ambientes/', AmbienteListCreate.as_view()),
    path('ambientes/<int:pk>/', AmbienteRetrieveUpdateDestroy.as_view()),

    # SENSORES
    path('sensores/', SensoresListCreate.as_view()),
    path('sensores/<int:pk>/', SensoresRetrieveUpdateDestroy.as_view()),

    # HISTORICO
    path('historicos/', HistoricoListCreate.as_view()),
    path('historicos/<int:pk>/', HistoricoRetrieveUpdateDestroy.as_view()),

    # Login e já gera o token de acesso
    path('login/',TokenObtainPairView.as_view()),
]