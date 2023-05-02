from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class AnkiCardManager(models.Manager):
    pass


class AnkiCard(models.Model):
    anki_id = models.AutoField(primary_key=True)
    #   user_id = models.ManyToOneRel('Users')
    front_side = models.TextField(default='')
    back_side = models.TextField(default=None)
    image = models.CharField(max_length=250, null=True, blank=True, default=None)
    objects = AnkiCardManager()

    def __str__(self):
        return self.front_side


class CardsSet(models.Model):
    cards_set_id = models.AutoField(primary_key=True)
    set_name = models.TextField(default='')

    def __str__(self):
        return self.set_name


class CardToSet(models.Model):
    sets = ForeignKey(CardsSet, on_delete=models.CASCADE)
    cards = models.ManyToManyField(AnkiCard)

    #   user_id = models.ManyToOneRel('Users')
