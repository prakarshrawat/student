from django.db import models

# Create your models here.


class info(models.Model):
    FullName = models.CharField(max_length=200)
    PhoneNo = models.IntegerField(default=0 )
    AdmissionNo = models.IntegerField(default=0)
    Standard = models.IntegerField(default=0 )
    Section = models.CharField(max_length=200 )

    # def __str__(self):
        # return 
