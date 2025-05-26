from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Ambientes, Historico, Sensores
from .serializers import AmbientesSerializer, HistoricoSerializer, SensoresSerializer
from rest_framework.exceptions import ValidationError
from django.http import Http404
from rest_framework.response import Response



#  ---- Crud ambientes ----
# class para criar e listar AMBIENTES
class AmbienteListCreate(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer

# essa class ira consultar o AMBIENTE pelo id, e fazer o get, put e delete dos ambientes
class AmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    # procurar pelo id do ambiente
    lookup_field = 'pk'

    # quando o ambiente for apagdo, aparecer essa mensagem
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response ({'mensagem':"O ambiente foi excluido com sucesso!"})
    
    # quando fixer o update, mostrar essa mensagem
    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response ({'mensagem':"O ambiente foi modificado com sucesso!"})
    
    # mensagem de erro, se o ambiente não for encontrado
    def get_object(self):
        try:
            return super().get_object()
        except Exception:
            raise Http404({'Erro': 'Ambiente não encontrado'})
 

# ---- Crud Historicos ----
# class para criar e listar HISTORICO
class HistoricoListCreate(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer

# essa class ira consultar o HISTORICO pelo id, e fazer o get, put e delete dos historicos
class HistoricoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    # procurar pelo id do Historico
    lookup_field = 'pk'

    # quando o Historico for apagdo, aparecer essa mensagem
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response ({'mensagem':"O historico foi excluido com sucesso!"})
    
    # quando fizer o update, mostrar essa mensagem
    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response ({'mensagem':"O historico foi modificado com sucesso!"})
    
    # mensagem de erro, se o historico não for encontrado
    def get_object(self):
        try:
            return super().get_object()
        except Exception:
            raise Http404({'Erro': 'historico não encontrado'})
        

# ---- Crud Sensores ----
# class para criar e listar SENSORES
class SensoresListCreate(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer

# essa class ira consultar os SENSORES pelo id, e fazer o get, put e delete dos SENSORES
class SensoresRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):  
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    # procurar pelo id do Sensores
    lookup_field = 'pk'

    # quando o SENSOR for apagdo, aparecer essa mensagem
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response ({'mensagem':"O sensor foi excluido com sucesso!"})
    
    # quando fizer o update, mostrar essa mensagem
    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response ({'mensagem':"O sensor foi modificado com sucesso!"})
    
    # mensagem de erro, se o sensor não for encontrado
    def get_object(self):
        try:
            return super().get_object()
        except Exception:
            raise Http404({'Erro': 'sensor não encontrado'})