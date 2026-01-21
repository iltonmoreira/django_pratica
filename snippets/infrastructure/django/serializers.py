from rest_framework import serializers
from snippets.infrastructure.django.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id","title","code","linenos","language","style","created", "expires_at"]
        read_only_fields = ["id","created"]

class SnippetSerializertitulo(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["title"]
        read_only_fields = ["id","created"]