import calendar
from datetime import datetime
from django.db.models import Count, Q, Sum, F, Case, When, IntegerField
from django.db.models.functions import TruncMonth, Coalesce
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions as rest_perm
from rest_framework import generics
from rest_framework import status

from api import serializers
from api import models
from api import permissions


class CreatePaydaAdmin(generics.CreateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.PaydaAdminSerializer
    queryset = models.PaydaAdmin.objects.all()


class CreatePaydaAgent(generics.CreateAPIView):
    permission_classes = [permissions.PaydaAdminPermission]
    serializer_class = serializers.AgentSerializer
    queryset = models.Agent.objects.all()


class CreateSalesManager(generics.CreateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.SalesSerializer
    queryset = models.PaydaUser.objects.all()


class CreateWorker(generics.CreateAPIView):
    permission_classes = [permissions.PaydaSalesPermission]
    serializer_class = serializers.WorkerSerializer
    queryset = models.Worker.objects.all()


class CreateWorkSheet(generics.CreateAPIView):
    permission_classes = [permissions.PaydaSalesPermission]
    serializer_class = serializers.CreateClientSerializer
    queryset = models.WorkSheet.objects.all()


class CreateComment(generics.CreateAPIView):
    permission_classes = [permissions.PaydaCommentPermission]
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class CreateActivity(generics.CreateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.ActivitySerializer
    queryset = models.Activity.objects.all()


class CreateRegion(generics.CreateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.RegionSerializer
    queryset = models.Region.objects.all()


class CreateTax(generics.CreateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.TaxSerializer
    queryset = models.TaxAuthority.objects.all()


class CreatePayment(generics.CreateAPIView):
    permission_classes = [permissions.PaydaAdminPermission]
    serializer_class = serializers.PaidForDealSerializer
    queryset = models.PaidForDeal.objects.all()


class CreateMessage(generics.CreateAPIView):
    permission_classes = [permissions.PaydaAgentPermission]
    serializer_class = serializers.CreateMessageSerializer
    queryset = models.Message.objects.all()


class CreateVariables(generics.CreateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.CreateVariablesSerializer
    queryset = models.Variables.objects.all()


class ListPayment(generics.ListAPIView):
    permission_classes = [rest_perm.AllowAny]
    serializer_class = serializers.PaidForDealSerializer
    queryset = models.PaidForDeal.objects.all()


class BlockAgent(generics.UpdateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.BlockAgentSerializer
    queryset = models.Agent.objects.all()


class ListClients(generics.ListAPIView):
    permission_classes = [permissions.PaydaAdminPermission]
    serializer_class = serializers.ListClientsSerializer
    queryset = models.WorkSheet.objects.all()


class DetailClient(generics.RetrieveAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.DetailClientSerializer
    queryset = models.WorkSheet.objects.all()


class Taxes(APIView):
    permission_classes = [rest_perm.IsAdminUser]

    def get(self, request, *args, **kwargs):
        client = models.WorkSheet.objects.get(pk=kwargs['pk'])

        supervisor = client.workers.filter(position='supervisor').values('supervisor_taxes')
        supervisor_taxes = models.TaxesSupervisor.objects.filter(pk__in=supervisor)
        serializer_first = serializers.TaxLeaderSerializer(supervisor_taxes, many=True)

        workers = client.workers.filter(position='employee').values('worker_taxes')
        worker_taxes = models.TaxesWorker.objects.filter(pk__in=workers)
        serializer_second = serializers.TaxWorkerSerializer(worker_taxes, many=True)

        result = {'first': serializer_first.data,
                  'second': serializer_second.data}

        return Response(result, status=status.HTTP_200_OK)


class ListAgents(generics.ListAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.ListAgentsSerializer
    queryset = models.Agent.objects.all()


class DetailAgent(generics.RetrieveAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.DetailAgentSerializer
    queryset = models.Agent.objects.all()

    def get(self, request, *args, **kwargs):
        agent = models.Agent.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(agent)
        clients = agent.clients.count()

        # ПЛАН
        accounting_services = agent.clients.aggregate(count=Count('payments'))['count']
        taxes_supervisor = agent.clients.aggregate(count=Count('workers__supervisor_taxes'))['count']
        taxes_worker = agent.clients.aggregate(count=Count('workers__worker_taxes'))['count']
        taxes = taxes_supervisor + taxes_worker
        # ФАКТ
        paid_accounting_services = agent.clients.aggregate(
            count=Count('payments', filter=Q(payments__check_paid=True)))['count']
        paid_taxes = agent.clients.aggregate(
            count=Count('workers__supervisor_taxes', filter=Q(workers__supervisor_taxes__check_paid=True)))['count']
        # ОТКЛОНЕНИЕ
        deflection_accounting_services = accounting_services - paid_accounting_services
        deflection_taxes = taxes - paid_taxes
        # УВЕДОМЛЕНО ПО НАЛОГАМ
        true_taxes_notifications = models.AgentClientTaxesMessage.objects.filter(agent=agent).count()
        false_taxes_notifications = clients - true_taxes_notifications
        # УВЕДОМЛЕНО ПО БУ
        true_by_notifications = models.AgentClientAccountingServicesMessage.objects.filter(agent=agent).count()
        false_by_notifications = clients - true_by_notifications
        # СООБЩЕНИЯ
        messages = models.Message.objects.filter(agent=agent).values('mess')

        return Response({
            'agent': serializer.data,
            'clients_count': clients,
            'plan_accounting_services': accounting_services,
            'plan_taxes': taxes,
            'fact_accounting_services': paid_accounting_services,
            'fact_taxes': paid_taxes,
            'true_accounting_notified': true_by_notifications,
            'false_accounting_notified': false_by_notifications,
            'true_taxes_notified': true_taxes_notifications,
            'false_taxes_notified': false_taxes_notifications,
            'deflection_accounting_services': deflection_accounting_services,
            'deflection_taxes': deflection_taxes,
            'messages': messages
        }, status=status.HTTP_200_OK)


class Debtor(APIView):
    permission_classes = [rest_perm.IsAdminUser]

    def get(self, request):
        result = []

        count_clients = models.Agent.objects.annotate(
            count_clients=Count('clients')
        ).values('user__username', 'count_clients')

        accruals = models.Agent.objects.annotate(
            accruals=Coalesce(Sum('clients__payments__amount'), 0)
        ).values('accruals')

        arrears = models.Agent.objects.annotate(
            arrears=Sum(Case(When(clients__payments__check_paid=False,
                                  then=F('clients__payments__amount')),
                             output_field=IntegerField(),
                             default=0))
        ).values('arrears')

        paid_accruals = models.Agent.objects.annotate(
            paid=Sum(Case(When(clients__payments__check_paid=True,
                               then=F('clients__payments__amount')),
                          output_field=IntegerField(),
                          default=0))
        ).values('paid')

        for count_cli, accrual, arrear, paid_acc, agent in zip(count_clients, accruals, arrears,
                                                               paid_accruals, models.Agent.objects.all()):
            if count_cli['user__username'] not in result:
                result.append({
                    'agent': count_cli['user__username'],
                    'clients': count_cli['count_clients'],
                    'accruals': accrual['accruals'],
                    'arrears': str(arrear['arrears']),
                    'paid': paid_acc['paid'],
                    'mark': agent.rating()
                })

        return Response(result, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([permissions.PaydaAdminPermission])
def dashboard(request):
    if request.method == 'GET':
        now = datetime.now()

        paid_true = models.PaidForDeal.objects.filter(
            Q(pay_month__month=now.month) & Q(check_paid=True)
        ).count()

        paid_false = models.PaidForDeal.objects.filter(
            Q(pay_month__month=now.month) & Q(check_paid=False)
        ).count()

        true = round(100 * paid_true / (paid_true + paid_false))
        false = 100 - true

        PIE_CHART = [true, false]

        LINE_CHART = {'0': 0}

        for data in models.WorkSheet.objects.annotate(
                month=TruncMonth('date')
        ).values('month').annotate(count=Count('id')).order_by('month'):
            month = calendar.month_name[data['month'].month]

            if month in LINE_CHART:
                LINE_CHART[month] += data['count']
            else:
                LINE_CHART[month] = data['count']

        months, values = [], []
        for t in list(LINE_CHART.items()):
            months.append(t[0])
            values.append(t[1])

        LINE_CHART = {'x': months, 'y': values}

        TOTAL_AMOUNT = request.user.admin.agent_set.aggregate(
            total_amount=Sum('clients__amount_deal'))['total_amount']

        COUNT_CLIENTS = models.WorkSheet.objects.count()

        AGENTS = request.user.admin.agent_set.count()

        now = datetime.now()
        days_in_month = calendar.monthrange(now.year, now.month)[1]
        CLIENTS = models.WorkSheet.objects.annotate(
            boo=F('expiration_date') - days_in_month).filter(
            Q(conclusion_date__gte=F('boo')) & Q(conclusion_date__lte=F('expiration_date')))

        serializer = serializers.ClientShortDescriptionSerializer(CLIENTS, many=True)

        messages = request.user.admin.agents_messages.all()[:5]
        ser_messages = serializers.MessageSerializer(messages, many=True)

        # ОЦЕНКИ АГЕНТОВ
        rating = []
        for agent in models.Agent.objects.all():
            result = {'pk': agent.pk, 'username': agent.user.full_name,
                      'mark': agent.rating()}
            rating.append(result)

        return Response({
            'pie_chart': PIE_CHART,
            'line_chart': LINE_CHART,
            'total_amount': TOTAL_AMOUNT,
            'count_clients': COUNT_CLIENTS,
            'agents_count': AGENTS,
            'expiring_contracts': serializer.data,
            'messages': ser_messages.data,
            'rating': rating
        }, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # ФИЛЬТРАЦИЯ PIE
        if request.data['type'] == 'pie':
            _from = request.data['range']['from']
            _to = request.data['range']['to']

            _from = [int(i) for i in _from.split('.')]
            _to = [int(i) for i in _to.split('.')]

            _from_date = datetime(year=_from[2], month=_from[1], day=_from[0])
            _to_date = datetime(year=_to[2], month=_to[1], day=_to[0])

            paid_true = models.PaidForDeal.objects.filter(
                Q(pay_month__gte=_from_date) &
                Q(pay_month__lte=_to_date) &
                Q(check_paid=True)
            ).count()

            paid_false = models.PaidForDeal.objects.filter(
                Q(pay_month__gte=_from_date) &
                Q(pay_month__lte=_to_date) &
                Q(check_paid=False)
            ).count()

            true = round(100 * paid_true / (paid_true + paid_false))
            false = 100 - true

            PIE_CHART = [true, false]

            return Response({
                'pie_chart': PIE_CHART
            }, status=status.HTTP_200_OK)

        elif request.data['type'] == 'line':
            # ФИЛЬТРАЦИЯ LINE
            _from = request.data['range']['from']
            _to = request.data['range']['to']

            _from = [int(i) for i in _from.split('.')]
            _to = [int(i) for i in _to.split('.')]

            _from_date = datetime(year=_from[2], month=_from[1], day=_from[0])
            _to_date = datetime(year=_to[2], month=_to[1], day=_to[0])

            LINE_CHART = {'0': 0}
            for data in models.WorkSheet.objects.filter(
                Q(date__gte=_from_date) & Q(date__lte=_to_date)
            ).annotate(count=Count('id')).values('date', 'count'):
                if calendar.month_name[data['date'].month] in LINE_CHART:
                    LINE_CHART[calendar.month_name[data['date'].month]] += data['count']
                else:
                    LINE_CHART[calendar.month_name[data['date'].month]] = data['count']

            return Response({
                'line_chart': LINE_CHART
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 404
            }, status=status.HTTP_400_BAD_REQUEST)


class APILoginView(APIView):
    permission_classes = [rest_perm.AllowAny]

    def post(self, request):
        """
        :param request:
        :return: str - Token, str - role
        """
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = models.User.objects.get(email=email)
            if not user.check_password(raw_password=password):
                return Response({
                    'error': 'Неправильный пароль'
                }, status=status.HTTP_400_BAD_REQUEST)
        except models.User.DoesNotExist:
            return Response({
                'error': 'Неправальный email'
            }, status=status.HTTP_400_BAD_REQUEST)
        role = None
        if getattr(user, 'is_paydaadmin'):
            role = 'admin'
        elif getattr(user, 'is_agent'):
            role = 'agent'
        elif getattr(user, 'is_client'):
            role = 'client'
        elif getattr(user, 'is_sales'):
            role = 'sales'
        token = Token.objects.filter(user=user)
        if token.exists():
            return Response({
                'access_token': token.first().key,
                'role': role,
                'username': user.full_name
            }, status=status.HTTP_200_OK)
        else:
            if role == 'agent' and user.agent.is_blocked:
                return Response({
                    'message': 'Ваш аккаунт заблокирован'
                }, status=status.HTTP_200_OK)
            token = Token.objects.create(user=user)
            return Response({
                'access_token': token.key,
                'role': role,
                'username': user.full_name
            }, status=status.HTTP_200_OK)


class APILogoutView(APIView):
    permission_classes = [rest_perm.IsAuthenticated]

    def post(self, request):
        """
        :param request: UWSGIRequest
        :return: message
        """
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({
            'message': 'Logout successful',
        }, status=status.HTTP_200_OK)


class UpdateClient(generics.UpdateAPIView):
    permission_classes = [permissions.PaydaAgentPermission]
    serializer_class = serializers.UpdateClientSerializer
    queryset = models.WorkSheet.objects.all()


class UpdateAgent(generics.UpdateAPIView):
    permission_classes = [permissions.PaydaAdminPermission]
    serializer_class = serializers.UpdateAgentSerializer
    queryset = models.Agent.objects.all()


class UpdateSales(generics.UpdateAPIView):
    permission_classes = [permissions.PaydaAdminPermission]
    serializer_class = serializers.UpdateSalesSerializer
