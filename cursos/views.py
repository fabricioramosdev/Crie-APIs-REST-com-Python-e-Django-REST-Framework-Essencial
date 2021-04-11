from rest_framework import generics
from rest_framework.generics import get_object_or_404


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
API V1
"""


class CursosAPIView(generics.ListCreateAPIView):
    """
    API de Cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API de Cursos
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    """
    API de Avaliações
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API de Avaliações
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), 
                                     curso_id=self.kwargs.get('curso_pk'), 
                                     pk=self.kwargs.get('avaliacao_pk'))
        
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))


"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    # CARREGA AS AVALIAÇÔES DO CURSO COM ID api\v2\1\avaliacoes\

    @action(detail=True, methods=['get'])
    def avaliacoe(self, request, pk=None):
        self.pagination_class.page_size = 1
        #  Paginação
        avaliacoes =  Avaliacao.objects.filter(curso_i=pk)
        page = self.paginate_queryset(avaliacoes)
        if page is not None:
            serializer =  AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        #curso = self.get_object()
        #serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


"""
## Permite retirar algumas das opções somente omitindo na lista de parametros
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    #mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""