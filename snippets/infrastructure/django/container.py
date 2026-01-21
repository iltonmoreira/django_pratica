from functools import cached_property

from snippets.infrastructure.django.repositories.snippet_repository import SnippetRepository
from snippets.application.use_cases.listar_snippets_use_case import ListarSnippetsUseCase
from snippets.application.use_cases.criar_snippet_use_case import CriarSnippetUseCase
from snippets.application.use_cases.detalhar_snippet_use_case import DetalharSnippetUseCase
from snippets.application.use_cases.alterar_snippet_use_case import AlterarSnippetUseCase
from snippets.application.use_cases.alterar_titulo_snippet_use_case import AlterarTituloSnippetUseCase


class SnippetsContainer:

    @cached_property
    def snippet_repository(self):
        return SnippetRepository()

    @cached_property
    def listar_snippets_use_case(self):
        return ListarSnippetsUseCase(self.snippet_repository)

    @cached_property
    def criar_snippet_use_case(self):
        return CriarSnippetUseCase(self.snippet_repository)

    @cached_property
    def detalhar_snippet_use_case(self):
        return DetalharSnippetUseCase(self.snippet_repository)
    
    @cached_property
    def alterar_snippet_use_case(self):
        return AlterarSnippetUseCase(self.snippet_repository)

    @cached_property
    def alterar_titulo_snippet_use_case(self):
        return AlterarTituloSnippetUseCase(self.snippet_repository)


snippets_container = SnippetsContainer()
