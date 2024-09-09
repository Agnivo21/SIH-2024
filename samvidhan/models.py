from django.db import models

class Preamble(models.Model):
    text = models.TextField()

class FundamentalRights(models.Model):
    article_number = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()
    simplified_text = models.TextField()

    def __str__(self):
        return self.article_number
    
class FundamentalDuties(models.Model):
    duty_number = models.CharField(max_length=10)
    description = models.TextField()
    simplified_text = models.TextField()

    def __str__(self):
        return self.duty_number
    
class DirectivePrinciples(models.Model):
    article_number = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    description = models.TextField()
    simplified_text = models.TextField()

    def __str__(self):
        return self.article_number
    
