from django.db import models

# Create your models here.
class Employerdeatils(models.Model):
    empid = models.CharField(max_length=100,primary_key=True)
    empname = models.CharField(max_length=100)
    emploc = models.CharField(max_length=100)
    empphone = models.CharField(max_length=100)
    empmail = models.CharField(max_length=100)

def str(self):
        return self.empid