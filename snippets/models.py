from django.db import models
from users.models import User

class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tag

class Snippet(models.Model):
    user = models.ForeignKey(to=User, 
                            on_delete=models.CASCADE, 
                            related_name="snippets",
                            null=True)
    title = models.CharField(max_length=255)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    language = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=1000)
    tags = models.ManyToManyField(to=Tag, related_name="snippets")


    def __str__(self):
        return self.title
