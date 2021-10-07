from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Todo(models.Model):
    title = models.CharField(null=False, max_length=30, blank=False)
    detail = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_important = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title + ' - ' + self.user.username