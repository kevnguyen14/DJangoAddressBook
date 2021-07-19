from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()

    def __str__(self):
        return self.first_name