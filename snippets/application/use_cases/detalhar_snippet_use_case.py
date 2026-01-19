from snippets.application.interfaces.snippet_interface import ISnippetRepository


class DetalharSnippetUseCase:
    def __init__(self, repository: ISnippetRepository):
        self.repository = repository

    def execute(self, id:int):
        return self.repository.buscar_por_id(id)