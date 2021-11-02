from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
class Advisor(models.Model):
    adName = models.CharField(max_length=100)
    adProfilePictureURL = models.TextField()
    adId = models.AutoField(primary_key=True)
class AdvisorBookingTrans(models.Model):
   # whoBooked = models.CharField(max_length=100)
    #whichAdvisor = models.CharField(max_length=100)
    whoBooked = models.ForeignKey(to='User',to_field='userid',on_delete=CASCADE)
    whichAdvisor = models.ForeignKey(to='Advisor',to_field='adId', on_delete=models.CASCADE)
    bookingId = models.AutoField(primary_key=True)
    bookingDateTime = models.DateTimeField()
class AdvisorBooking(models.Model):
    whoBooked = models.ForeignKey(to='User',to_field='userid', on_delete=models.CASCADE)
    whichAdvisor = models.ForeignKey(to='Advisor',to_field='adId',on_delete=models.CASCADE)
    bookingId = models.AutoField(primary_key=True)
    bookingDateTime = models.DateTimeField()


