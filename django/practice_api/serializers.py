from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from .models import Student, Attendance, JWTPayloadTrack


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


# class AttendanceSerializer(serializers.ModelSerializer):
#     # students = serializers.PrimaryKeyRelatedField(read_only=True)
#
#     class Meta:
#         model = Attendance
#         # fields = ('student', 'date', 'status')
#         fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class JWTPayloadTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = JWTPayloadTrack
        fields = '__all__'
