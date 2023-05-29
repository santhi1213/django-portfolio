from django.db import models


class Data(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=700)
    date = models.DateField()




    def __str__(self):
        return self.title



