from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User , on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30)
    national_code = models.CharField(max_length=11)
    image = models.ImageField(upload_to="images/profiles" , null=True , blank=True)

    def __str__(self):
        return self.owner.username
