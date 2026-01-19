from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, default="python")
    style = models.CharField(max_length=100, default="friendly")
    expires_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["created"]