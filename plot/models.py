from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pi(models.Model) :
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.address + '-' + self.code

class Data(models.Model):
    pi = models.ForeignKey(Pi, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    vol = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self):
        return "Vol:" + str(self.vol) + " Time:" + self.date_time.strftime(
            '%x/%X') + \
                      'Pi:' +\
               str(self.pi)