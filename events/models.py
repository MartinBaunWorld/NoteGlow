from django.db import models

class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=256, null=False, default="INFO")
    name = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=False, default="")
    country = models.CharField(max_length=256, null=False, default="")
    ip = models.CharField(max_length=256, null=False, default="")
    body = models.TextField(null=False, default="{}")
    ref = models.CharField(max_length=256, null=False, default="")

    def __str__(self):
        return f'{self.level} - {self.name} - {self.email}'
