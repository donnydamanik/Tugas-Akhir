from django.db import models

class Contract(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return self.name
