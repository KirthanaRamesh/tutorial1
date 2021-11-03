from django.db.models.sql import query
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.response import Response
from advisorapi.renderers.ApiRenderer import ApiRenderer

from advisorapi.models import AdvisorBookingTrans, User
from advisorapi.models import Advisor
from advisorapi.serializers import UserSerializer
from advisorapi.serializers import AdvisorSerializer
from advisorapi.serializers import AdvisorBookingSerializer
from advisorapi.serializers import AdvisorBookedSerializer
from advisorapi.serializers import AdvisorBookedSerializerNew
from advisorapi.serializers import LoginSerializer
import collections


# Create your views here.

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
@api_view(['GET', 'POST'])
#@renderer_classes((ApiRenderer,))
def user_list(request):
    """
    List all users
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            cusdata = {}
            cusdata['userid'] = serializer.data.get('userid')
     #       print(serializer.data)
     #       print(serializer.data.get('userid'))
            userdetails = {}
            userdetails['username']=serializer.data.get('name')
            userdetails['id'] = serializer.data.get('userid')
     #       print(userdetails)
            object_name = collections.namedtuple("ObjectName", userdetails.keys())(*userdetails.values())
            print(getattr(object_name, 'id'))
            jwttoken = get_tokens_for_user(object_name)
       #     print(jwttoken);
            cusdata.update(jwttoken)
            return Response(cusdata, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
def advisor_list(request):
        """
        List all advisor
        """
        if request.method == 'GET':
            advisor = Advisor.objects.all()
            serializer = AdvisorSerializer(advisor, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = AdvisorSerializer(many=True,data=request.data)
            if serializer.is_valid():
                serializer.save()
                cusdata = {}
                return Response(cusdata, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def user_login(request):
    """
        Registers a User
    """
    if request.method == 'POST':
        inPassword=request.data['email']
        user = User.objects.filter(email=inPassword)
        print(inPassword)
        serializer = LoginSerializer(user, many=True)
        userpassword = user.values('password')
        password = userpassword[0].get('password')
        print(password)
        print(request.data)
        print(user)
        print(user.values('userid'))
        cusdata = {}
        cusdata = prepareJWTToken(user.values('userid'))
        print(cusdata)
        if request.data['password'] == password:
            return Response(cusdata)
        return Response("invalid password",status=status.HTTP_400_BAD_REQUEST )
        
def prepareJWTToken(userid):
    cusdata = {}
    cusdata['userid'] = userid
     #       print(serializer.data)
     #       print(serializer.data.get('userid'))
    userdetails = {}
    #userdetails['username']=serializer.data.get('name')
    userdetails['id'] = userid
     #       print(userdetails)
    object_name = collections.namedtuple("ObjectName", userdetails.keys())(*userdetails.values())
    print(getattr(object_name, 'id'))
    jwttoken = get_tokens_for_user(object_name)
    #     print(jwttoken);
    cusdata.update(jwttoken)
    print(cusdata)
    return cusdata

@api_view(['GET'])
def user_advisor_list(request,userid):
    """
        List all Advisors
    """
    if request.method == 'GET':
            advisor = Advisor.objects.all()
            serializer = AdvisorSerializer(advisor, many=True)
            return Response(serializer.data)
    
@api_view(['GET'])
def advisor_booked_list(request):
    """
        List all Advisors Booked List
    """
    if request.method == 'GET':
            #advisorBooked = AdvisorBookingTrans.objects.all()
            advisorBooked = AdvisorBookingTrans.objects.all()
            print(advisorBooked)
            serializer = AdvisorBookedSerializer(advisorBooked,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 #           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_advisor_booked_list(request,userid):
    """
        List Advisors booked by a user
    """
    if request.method == 'GET':
            #advisorBooked = AdvisorBookingTrans.objects.all()
            query_set = AdvisorBookingTrans.objects.select_related('whichAdvisor').filter(whoBooked=userid)
            #advisorBooked = AdvisorBookingTrans.objects.filter(whoBooked=userid)
            #print(advisorBooked)
           # print(query_set.query)
           # print(query_set.get(many=True))
           # serializer = AdvisorBookedSerializer(advisorBooked,many=True)
            #bookingset = query_set.values('adName')
            #print(bookingset[0].get('adName'))
            #for i in bookingset.iterator():
            #    print(i.adId)
            #print(query_set.query)

            serializer = AdvisorBookedSerializerNew(query_set,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
 #           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_advisor_booking_list(request,userid,advisorid):
    """
        Books an Advisor
    """
    if request.method == 'POST':
        print(request.data)
        requestdata = {}
        requestdata['whoBooked'] = userid
        requestdata['whichAdvisor'] = advisorid
        requestdata['bookingDateTime'] = request.data['bookingDateTime']
        print(requestdata)
        serializer = AdvisorBookingSerializer(data=requestdata)
        if serializer.is_valid():
            serializer.save()
            cusdata = {}
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
