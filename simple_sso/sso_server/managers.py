from django.db import models


class TokenManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("consumer", "user")
