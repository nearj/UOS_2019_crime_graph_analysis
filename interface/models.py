from django.db import models
from django.conf import settings
from django.utils import timezone

class Trial(models.Model):
    pd_cd = models.FloatField()
    law_cat_cd = models.FloatField()
    s_sex = models.FloatField()
    s_age = models.FloatField()
    s_race = models.FloatField()
    v_sex = models.FloatField()
    v_age = models.FloatField()
    v_race = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return str(self.pk)
