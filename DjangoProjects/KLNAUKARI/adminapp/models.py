from django.db import models

class useraccount(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Job seeker'),
    ]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    phonenumber = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    def __str__(self):
        return self.firstname