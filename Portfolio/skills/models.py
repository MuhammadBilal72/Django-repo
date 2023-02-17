from django.db import models

# Create your models here.
class Skills(models.Model):
    skillID=models.IntegerField(primary_key=True)
    skillName=models.CharField(max_length=100)
    skillExp=models.IntegerField()
    onSite=models.BooleanField(default=True)