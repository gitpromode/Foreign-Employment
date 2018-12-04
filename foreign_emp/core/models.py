from django.db import models

# Create your models here.
class Province(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class District(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey(Province, related_name="district", on_delete=models.CASCADE)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class LocGov(models.Model):
	name = models.CharField(max_length=100)
	district = models.ForeignKey(District, related_name="locgov", on_delete=models.CASCADE)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name