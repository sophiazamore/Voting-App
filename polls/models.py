from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=30)
    individual_percentage = models.CharField(max_length=10)
    total_individual_counts = models.IntegerField()
    is_winner = models.BooleanField()

# Create your models here.
