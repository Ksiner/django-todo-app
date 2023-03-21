from django.db import models
import uuid
from django.utils.timezone import now


class CompanyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False)

    created_at = models.DateTimeField(auto_now_add=now)

    def __str__(self) -> str:
        return self.name
