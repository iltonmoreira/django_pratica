from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class CriarSnippetDto:
    title:str
    code:str
    linenos:bool =False
    language:str ="python"
    style:str ="friendly"
    expires_at: Optional[datetime] = None


@dataclass(frozen=True)
class AlterarSnippetDto:
    title:str
    code:str
    linenos:bool =False
    language:str ="python"
    style:str ="friendly"
    expires_at: Optional[datetime] = None

@dataclass(frozen=True)
class AlterarTituloSnippetDto:
    title:str