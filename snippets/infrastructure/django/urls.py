from django.urls import path

from snippets.infrastructure.django.views import (
    SnippetListView,
    SnippetCreateView,
    SnippetDetailView,
    SnippetUpdateView,
    SnippetAlterarTituloView,
)


urlpatterns = [
    path("", SnippetListView.as_view()),# GET
    path("create/", SnippetCreateView.as_view()),# POST
    path("<int:id>/", SnippetDetailView.as_view()),# GET
    path("<int:id>/update/", SnippetUpdateView.as_view()),# PUT
    path("<int:id>/titulo/", SnippetAlterarTituloView.as_view()),# PATCH
]