from django.db import models
from users.models import User

LANGUAGE_CHOICES = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JavaScript', 'JavaScript'),
    ('Python', 'Python'),
    ('Django', 'Django')
)

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
    description = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='')
    body = models.TextField(max_length=1000)
    tags = models.ManyToManyField(to=Tag, related_name="snippets")

    def tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)

        return " ".join(tag_names)

    def set_tag_names(self, tag_names):
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.create(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)

    def __str__(self):
        return self.title
