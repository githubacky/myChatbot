from django.db import models

# Create your models here.
class Chat(models.Model):
	comment = models.TextField('コメント')
