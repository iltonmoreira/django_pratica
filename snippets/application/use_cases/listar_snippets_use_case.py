from snippets.application.interfaces.snippet_interface import ISnippetRepository


class ListarSnippetsUseCase:
    def __init__(self, repository: ISnippetRepository):
        self.repository = repository

    def execute(self):
        return self.repository.listar()