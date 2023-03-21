from django.db import models
import uuid
from users.models import UserModel
from companies.models import CompanyModel
from django.utils.timezone import now
from enum import Enum


class CompanyMemberRoles(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    MEMBER = "member"


class CompanyMemberModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(
        choices=[(enum_item.name, enum_item.value) for enum_item in CompanyMemberRoles], null=False, max_length=32
    )
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="user")

    joined_at = models.DateTimeField(null=False)
