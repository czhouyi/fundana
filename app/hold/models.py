from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Stock(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Fund(models.Model):
	code = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	rate = models.DecimalField(max_digits=5, decimal_places=2)
	amount = models.DecimalField(max_digits=19, decimal_places=2)

	def __unicode__(self):
		return self.name

class Hold(models.Model):
	stock = models.ForeignKey(Stock)
	fund = models.ForeignKey(Fund)
	rate = models.DecimalField(max_digits=5, decimal_places=2)
