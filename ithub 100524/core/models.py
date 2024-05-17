from django.db import models


class CreatedUpdatedModel(models.Model):
    """Добавляет дату создания и обновления строки в бд."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
