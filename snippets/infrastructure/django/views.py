from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import json

from snippets.application.dtos.snippet_dtos import CriarSnippetDto, AlterarSnippetDto, AlterarTituloSnippetDto
from snippets.infrastructure.django.container import snippets_container
from snippets.infrastructure.django.serializers import SnippetSerializer, SnippetSerializertitulo


class SnippetListView(APIView):
    def get(self, request):
        snippets = snippets_container.listar_snippets_use_case.execute()
        return Response(SnippetSerializer(snippets, many=True).data)

class SnippetCreateView(APIView):
    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = CriarSnippetDto(**serializer.validated_data)
        snippet = snippets_container.criar_snippet_use_case.execute(dto)

        return Response(
            SnippetSerializer(snippet).data,
            status=status.HTTP_201_CREATED
        )


class SnippetDetailView(APIView):
    def get(self, request, id:int):
        snippet = snippets_container.detalhar_snippet_use_case.execute(id)
        return Response(SnippetSerializer(snippet).data)


class SnippetUpdateView(APIView):
    def put(self, request, id:int):
        serializer = SnippetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        dto = AlterarSnippetDto(**serializer.validated_data)
        snippet = snippets_container.alterar_snippet_use_case.execute(id, dto)

        return Response(
            SnippetSerializer(snippet).data,
            status=status.HTTP_200_OK
        )

class SnippetAlterarTituloView(APIView):
    def patch(self,request, id:int):
        try:
            payload = json.loads(request.body)

            serializer = SnippetSerializertitulo(data=payload)
            serializer.is_valid(raise_exception=True)

            dto = AlterarTituloSnippetDto(
                title=serializer.validated_data["title"]
            )

            use_case = snippets_container.alterar_titulo_snippet_use_case
            snippet = use_case.execute(id, dto)

            return JsonResponse(
                {
                    "id": snippet.id,
                    "title": snippet.title,
                },
                status=200
            )

        except ValidationError as e:
            return JsonResponse(
                {"error": str(e)},
                status=400
            )