from django.db import models

# Create your models here.

class Work(models.Model):
    body = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body)
