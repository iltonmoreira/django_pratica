from snippets.application.dtos.snippet_dtos import CriarSnippetDto
from snippets.application.interfaces.snippet_interface import ISnippetRepository


class CriarSnippetUseCase:
    def __init__(self, repository: ISnippetRepository):
        self.repository = repository

    def execute(self, dto: CriarSnippetDto):
        return self.repository.criar(dto.__dict__)