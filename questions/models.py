from django.db import models
from django.conf import settings

# Create your models here. 
class QuestioCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    question = models.TextField()
    category = models.ForeignKey(QuestioCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    