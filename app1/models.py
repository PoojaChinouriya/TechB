from django.db import models


class TechB(models.Model):
    Eid = models.IntegerField()
    Ename = models.CharField(max_length=10)
    task = models.CharField(max_length=30)

