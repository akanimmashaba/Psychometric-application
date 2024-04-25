from django.contrib import admin
from .models import Question,QuestioCategory
# Register your models here.
admin.site.register(Question)
admin.site.register(QuestioCategory)