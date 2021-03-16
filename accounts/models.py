from django.db import models

# Create your models here.
class registrationRequest(models.Model):
    proposedUsername = models.CharField(max_length=20, null=False)
    proposedPassword = models.CharField(max_length=20, null=False)
    emailAddress = models.EmailField(max_length=254, null=False, primary_key=True)
    # Leaving out requestedAccessLevel and emailVerified, not sure how to approach yet

class sspCredential (models.Model):
    userName = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    emailAddress = models.EmailField(max_length=254, null=False, primary_key=True)
    # Leaving out accessLevel and emailVerified

class student (models.Model):
    name = models.CharField(max_length=250, null=False)
    emailAddress = models.EmailField(max_length=254, primary_key=True)
    userName = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)

