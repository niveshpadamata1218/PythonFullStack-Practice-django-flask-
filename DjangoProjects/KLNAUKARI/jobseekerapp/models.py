from django.db import models

class JobSeekerProfile(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    hobbies = models.TextField()
    skills = models.TextField()
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.name