from abc import ABC, abstractmethod
from typing import Any, Iterable


class ISnippetRepository(ABC):

    @abstractmethod
    def listar(self) -> Iterable[Any]:
        raise NotImplementedError
    
    @abstractmethod
    def buscar_por_id(self, id:int) ->Any:
        raise NotImplementedError

    @abstractmethod
    def criar(self, dados: dict) ->Any:
        raise NotImplementedError

    @abstractmethod
    def atualizar(self, id:int, dados:dict) ->Any:
        raise NotImplementedError