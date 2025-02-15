from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Connection(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('connections_detail', kwargs={'connection_id': self.id})
    

class Job(models.Model):
    company = models.CharField(max_length=50)
    date = models.DateField('Applied Date')
    salary = models.IntegerField()
    position = models.CharField(max_length=50)
    notes = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connections = models.ManyToManyField(Connection)
    
    def __str__(self):
        return f'{self.company} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('jobs_detail', kwargs={'job_id': self.id})


class Todo(models.Model):
    description = models.TextField(max_length=200)
    done = models.BooleanField(default=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'
    

class Status(models.Model):
    description = models.TextField(max_length=200)
    date = models.DateField('Status Date')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'



class Interaction(models.Model):
    description = models.TextField(max_length=200)
    date = models.DateField('Interaction Date')
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'
    


