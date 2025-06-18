from django.db import models

class Proposal(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    technology = models.CharField(max_length=200, blank=True)
    needs = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company}"