from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Style(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Boxer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255)
    style = models.ForeignKey(Style, on_delete=CASCADE) 
    
    def __str__(self):
        return str(self.id) + ' ' + self.last_name + ' ' + self.first_name


class Fight(models.Model):
    red_corner_id = models.ForeignKey(Boxer, on_delete=CASCADE)
    blue_corner_id = models.IntegerField()
    title_fight = models.BooleanField()
    scheduled_rounds = models.IntegerField()
    decision_round = models.IntegerField()
    decision_type = models.IntegerField()
    winner_id = models.IntegerField()

    def __str__(self):
        return str(self.id)