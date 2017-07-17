from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Contact, PhoneNumber
from phonenumber_field.modelfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model()(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PhoneNumberSerializer(serializers.ModelSerializer):
    number = serializers.CharField(validators=PhoneNumberField().validators)

    class Meta:
        model = PhoneNumber
        fields = ('id', 'number')
        read_only_fields = ('id',)

    def create(self, validated_data):
        p, _ = PhoneNumber.objects.get_or_create(number=validated_data.get('number'))
        contact = validated_data.get('contact')
        contact.phone_numbers.add(p)
        return p


class ContactSerializer(serializers.ModelSerializer):

    phone_numbers = PhoneNumberSerializer(many=True, required=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ('user', 'name', 'phone_numbers', 'id')
        read_only_fields = ('id',)

    def create(self, validated_data):
        phone_numbers = validated_data.pop('phone_numbers', [])
        contact = Contact.objects.create(**validated_data)
        for phone_number in phone_numbers:
            p, _ = PhoneNumber.objects.update_or_create(number=phone_number.get('number'))
            contact.phone_numbers.add(p)
        return contact

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance
