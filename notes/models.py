import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        null=False
    )
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes_detail', args=[str(self.id)])
