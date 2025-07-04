from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

class Class(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    schedule = models.DateTimeField()

class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)
    gym_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    schedule = models.DateTimeField()
    status = models.CharField(max_length=20)

class Notification(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)