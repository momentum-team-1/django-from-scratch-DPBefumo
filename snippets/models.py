from django.db import models
from users.models import User

class Snippet(models.Model):
    # user = models.ForeignKey(to=User,
    #                         on_delete=models.CASCADE,
    #                         related_name="snippets")
    title = models.CharField(max_length=255)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title