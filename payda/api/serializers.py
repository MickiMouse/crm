from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import password_validation

from api import models


class PaydaUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, required=True)
    full_name = serializers.CharField(max_length=200, required=True)

    # def validate_password(self, value):
    #     if value:
    #         password_validation.validate_password(value)
    #     return value

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
            full_name=user_data['full_name'],
            email=user_data['email']
        )
        u.username = user_data['full_name']
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
    password2 = serializers.CharField(label='Repeat password', min_length=6, required=True)

    class Meta:
        model = models.Agent
        fields = ('user',
                  'phone',
                  'password2')

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
            full_name=user_data['full_name'],
            email=user_data['email'])
        u.username = user_data['full_name']
        u.set_password(raw_password=password)
        u.is_agent = True
        u.save()
        agent = models.Agent.objects.create(
            phone=validated_data['phone'])
        agent.user = u
        agent.save()
        validated_data['password2'] = password2
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


class UpdateSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaydaUser
        fields = ('username',
                  'password')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ('activity',)


class UserShortDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaydaUser
        fields = ('username',
                  'email',
                  'full_name')


class AgentShortDescriptionSerializer(serializers.ModelSerializer):
    user = UserShortDescriptionSerializer()

    class Meta:
        model = models.Agent
        fields = ('user',)


class ListClientsSerializer(serializers.ModelSerializer):
    kind_of_activity = ActivitySerializer(many=True)
    agent = AgentShortDescriptionSerializer()

    class Meta:
        model = models.WorkSheet
        fields = ('pk',
                  'short_name',
                  'kind_of_activity',
                  'extra_address',
                  'bin_iin',
                  'agent',
                  'expiration_date')


class TaxLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaxesSupervisor
        fields = ('month',
                  'earn',
                  'profit',
                  'pension_contrib',
                  'income_for_so',
                  'social_contrib',
                  'osms')


class WorkerShortDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = ('last_name',
                  'first_name')


class TaxWorkerSerializer(serializers.ModelSerializer):
    worker = WorkerShortDescriptionSerializer()

    class Meta:
        model = models.TaxesWorker
        fields = ('month',
                  'profit',
                  'earn',
                  'adjustment',
                  'pension_contrib',
                  'individual_income_tax',
                  'social_contrib',
                  'med_contrib',
                  'worker')


class CreateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkSheet
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Worker
        fields = '__all__'


class LeaderTaxesSerializer(serializers.ModelSerializer):
    supervisor_taxes = TaxLeaderSerializer(many=True)

    class Meta:
        model = models.Worker
        fields = ('supervisor_taxes',)


class WorkerTaxesSerializer(serializers.ModelSerializer):
    worker_taxes = TaxWorkerSerializer(many=True)

    class Meta:
        model = models.Worker
        fields = ('worker_taxes',)


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaxAuthority
        fields = '__all__'


class TaxShortDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaxAuthority
        fields = ('name',)


class DetailClientSerializer(serializers.ModelSerializer):
    agent = AgentShortDescriptionSerializer()
    kind_of_activity = ActivitySerializer(many=True)
    tax = TaxShortDescriptionSerializer()

    class Meta:
        model = models.WorkSheet
        fields = ('organization',
                  'full_name',
                  'kind_of_activity',
                  'bin_iin',
                  'address_physical',
                  'address_legal',
                  'extra_address',
                  'phone', 'bik', 'iik',
                  'bank_name', 'leader',
                  'position_leader',
                  'phone_number',
                  'tax', 'kbe', 'date',
                  'last_change',
                  'conclusion_date',
                  'expiration_date',
                  'amount_deal',
                  'comments',
                  'agent')


class ClientShortDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkSheet
        fields = ('pk',
                  'full_name',
                  'expiration_date')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
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
    agent = AgentShortDescriptionSerializer()

    class Meta:
        model = models.Message
        fields = ('agent',
                  'mess',
                  'created_at')


class BlockAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = ('is_blocked',)


class CreateVariablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variables
        fields = '__all__'


class ClientsInAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkSheet
        fields = ('short_name',)


class ListAgentsSerializer(serializers.ModelSerializer):
    user = UserShortDescriptionSerializer()

    class Meta:
        model = models.Agent
        fields = ('pk',  # 'tag',
                  'user',
                  'last_change',
                  'created_at',
                  'clients',)


class DetailAgentSerializer(serializers.ModelSerializer):
    user = UserShortDescriptionSerializer()
    clients = ClientsInAgentSerializer(many=True)

    class Meta:
        model = models.Agent
        fields = ('pk',
                  'user',
                  'phone',
                  'clients',)


class UpdateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkSheet
        fields = '__all__'


class UpdateAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = '__all__'
