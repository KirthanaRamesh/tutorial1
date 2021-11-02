from django.db import models
from rest_framework import serializers
from advisorapi.models import Advisor, User, AdvisorBookingTrans



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userid','name','email','password']
class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['adName','adProfilePictureURL','adId']
class AdvisorBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorBookingTrans
        fields = ['bookingId','bookingDateTime','whoBooked','whichAdvisor']
class AdvisorBookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorBookingTrans
    # whoBooked = models.CharField(max_length=100)
    # whichAdvisor = models.CharField(max_length=100)
    # bookingId = models.AutoField(primary_key=True)
    # bookingDateTime = models.DateTimeField()
        fields = ['bookingId','whoBooked','whichAdvisor','bookingDateTime']
 #       fields = ['bookingId','bookingDateTime','adName','adId','adProfilePictureURL']
 #       fields = ['bookingDateTime']
class AdvisorBookedSerializerNew(serializers.ModelSerializer):
    #    booking = AdvisorBookedSerializer()
    #    advisors = AdvisorSerializer()
        class Meta:
            model = AdvisorBookingTrans
            fields = ['bookingId','whoBooked','whichAdvisor','bookingDateTime']
            depth = 1
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userid','email','password']