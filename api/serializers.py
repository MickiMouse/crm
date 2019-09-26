from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import password_validation

from api import models


class PaydaUserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, required=True)

    def validate_password(self, value):
        if value:
            password_validation.validate_password(value)
        return value

    def validate(self, attrs):
        email = attrs.get('email')
        try:
            models.PaydaUser.objects.get(email=email)
            raise ValidationError('Данный email уже занят')
        except models.PaydaUser.DoesNotExist:
            return attrs


class PaydaAdminSerializer(serializers.ModelSerializer):
    user = PaydaUserSerializer()
    password2 = serializers.CharField(label='Repeat password', min_length=6, required=True)

    class Meta:
        model = models.PaydaAdmin
        fields = ('user',
                  'password2',
                  'status',
                  'address')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        password = attrs['user']['password']
        password2 = attrs['password2']
        if password and password2 and password != password2:
            raise ValidationError('Введённые пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user_data = validated_data['user']
        password = user_data['password']
        password2 = validated_data.pop('password2')
        u = models.PaydaUser.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email']
        )
        u.username = ''.join([user_data.get('first_name'),
                              user_data.get('last_name')])
        u.set_password(raw_password=password)
        u.is_paydaadmin = True
        u.save()
        admin = models.PaydaAdmin.objects.create(
            status=validated_data['status'],
            address=validated_data['address']
        )
        admin.user = u
        admin.save()
        validated_data['password2'] = password2
        return validated_data


class AgentSerializer(serializers.ModelSerializer):
    user = PaydaUserSerializer()

    class Meta:
        model = models.Agent
        fields = ('user',
                  'telephone')

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data['user']
        password = user_data['password']
        u = models.PaydaUser.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email']
        )
        u.username = ''.join([user_data.get('first_name'),
                              user_data.get('last_name')])
        u.set_password(raw_password=password)
        u.is_agent = True
        u.save()
        agent = models.Agent.objects.create(
            telephone=validated_data['telephone']
        )
        agent.user = u
        agent.save()
        return validated_data


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaydaUser
        fields = ('username',
                  'password')

    def validate_password(self, value):
        if value:
            password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        u = models.PaydaUser.objects.create(
            username=validated_data['username']
        )
        u.set_password(raw_password=validated_data['password'])
        u.is_sales = True
        u.save()
        return validated_data


class ListClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkSheet
        fields = ('short_name',
                  'kind_of_activity',
                  'extra_address',
                  'bin_iin',
                  'agent',
                  'expiration_date')


class WorkSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkSheet
        fields = '__all__'


class WorkSheetShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkSheet
        fields = ('pk',
                  'full_name',
                  'expiration_date')


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaxAuthority
        fields = '__all__'


class PaidForDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaidForDeal
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ('agent',
                  'mess')


class BlockAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = ('is_blocked',)
