from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models

# Create your models here.
class User(BaseUser):
    # could add custom user attributes here
    pass


class Snippet(models.Model):
    code = models.TextField()
    description = models.CharField(max_length=512, default="")
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name="snippets", blank=True, null=True)
    # related name should be the plural of the model that it's in. This is a O2M relationship. A snippet has one user. A user has many snippets.
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="snippets")
    # if I want to have more than one user associated with a snippet, I use an M2M field
    users = models.ManyToManyField('User', related_name='snippets')

    def __str__(self):
        return f'{self.description} in {self.language}'


class Language(models.Model):
    name = models.CharField(max_length=255)
    version = models.FloatField(blank=True, null=True)

