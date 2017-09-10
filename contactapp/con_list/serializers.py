from rest_framework.serializers import ModelSerializer
from .models import Contact
from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ('email', 'username', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User(
		email=validated_data['email'],
		username=validated_data['username']
		)
		user.set_password(validated_data['password'])
		user.save()
		return user
        


class ContactSerializer(ModelSerializer):
	
    class Meta:
        model = Contact
        fields = '__all__'
    
