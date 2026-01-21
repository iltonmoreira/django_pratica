from django.shortcuts import get_object_or_404

from snippets.application.interfaces.snippet_interface import ISnippetRepository
from snippets.infrastructure.django.models import Snippet


class SnippetRepository(ISnippetRepository):

    def listar(self):
        return Snippet.objects.all()

    def buscar_por_id(self, id:int):
        return get_object_or_404(Snippet,id=id)

    def criar(self, dados: dict):
        return Snippet.objects.create(**dados)

    def atualizar(self, id:int, dados:dict):
        snippet =self.buscar_por_id(id)

        for k, v in dados.items():
            setattr(snippet, k, v)

        snippet.save()
        return snippet