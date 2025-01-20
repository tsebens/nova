from django.db import models


class Text(models.Model):
    """An instance of text from the corpora"""
    text = models.TextField()


class Mention(models.Model):
    """A mention of an entity in the corpora"""
    text = models.ForeignKey(Text, on_delete=models.CASCADE)


# Create your models here.
class Entity(models.Model):
    """Base class for resolved entities"""
    name = models.CharField(max_length=128)