from django.db import models

class Article(models.Model):
	source = models.CharField(max_length=100, null=True, blank=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=150, default='Unknown', null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	publication_date = models.DateTimeField('date published')
	url = models.CharField(max_length=300)
	urlToImage = models.CharField(max_length=300, null=True, blank=True)
	avgImgColorR = models.IntegerField(null=True)
	avgImgColorG = models.IntegerField(null=True)
	avgImgColorB = models.IntegerField(null=True)
	sentiment = models.DecimalField(max_digits=5, decimal_places=4, null=True)
	def __str__(self):
		return self.title
