from snippets.application.dtos.snippet_dtos import AlterarTituloSnippetDto, AlterarSnippetDto
from snippets.application.interfaces.snippet_interface import ISnippetRepository
from django.core.exceptions import ValidationError


class AlterarSnippetUseCase:
    def __init__(self, repository:ISnippetRepository):
        self.repository = repository

    def execute(self, id:int, dto:AlterarSnippetDto):
        snippet = self.repository.buscar_por_id(id)

        if dto.language != snippet.language:
            raise ValidationError("Não é permitido alterar o language após a criação do snippet.")

        if not dto.title:
            raise ValidationError("O título não pode ser vazio.")

        return self.repository.atualizar(id, dto.__dict__)
    
class AlterarTituloSnippetUseCase:
    def __init__(self, repository:ISnippetRepository):
        self.repository = repository

    def execute(self, id:int, dto:AlterarTituloSnippetDto):
        snippet = self.repository.buscar_por_id(id)

        if not dto.title:
            raise ValidationError("O título não pode ser vazio.")

        return self.repository.atualizar(id, dto.__dict__)