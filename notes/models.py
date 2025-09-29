from django.db import models
from django.utils.timezone import now


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    tags = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
