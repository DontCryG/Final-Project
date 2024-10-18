from django.db import models

class SupportMessage(models.Model):
    report = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    reply = models.BooleanField(default=False)
    
    def __str__(self):
        return self.report