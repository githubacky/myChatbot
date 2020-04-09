from django.db import models

# Create your models here.
class Chatbot(models.Model):
	comment = models.TextField('コメント')
	
	def __str__(self):
		return self.comment
