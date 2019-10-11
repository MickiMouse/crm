import calendar
from datetime import datetime
from django.db.models import Count, Q, Sum, F
from django.db.models.functions import TruncMonth
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
    serializer_class = serializers.WorkSheetSerializer
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


class ListPayment(generics.ListAPIView):
    permission_classes = [rest_perm.AllowAny]
    serializer_class = serializers.PaidForDealSerializer
    queryset = models.PaidForDeal.objects.all()


class DetailAgent(generics.RetrieveAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.AgentSerializer
    queryset = models.Agent.objects.all()


class BlockAgent(generics.UpdateAPIView):
    permission_classes = [rest_perm.IsAdminUser]
    serializer_class = serializers.BlockAgentSerializer
    queryset = models.Agent.objects.all()


class ListClients(generics.ListAPIView):
    permission_classes = [permissions.PaydaAgentPermission]
    serializer_class = serializers.ListClientsSerializer
    queryset = models.WorkSheet.objects.all()

    def get(self, request, *args, **kwargs):
        clients = request.user.agent.clients.all()
        return Response(self.get_serializer(clients, many=True).data)


@api_view(['GET'])
@permission_classes([permissions.PaydaAdminPermission])
def dashboard(request):
    PIE_CHART = {'paid': {}, 'unpaid': {}}

    payed_true = models.PaidForDeal.objects.filter(
        ~Q(client__agent=None)
    ).annotate(
        month=TruncMonth('pay_month')
    ).values('month').annotate(
        count_paid=Count('id', filter=Q(check_paid=True))
    ).values('month', 'count_paid')

    payed_false = models.PaidForDeal.objects.filter(
        ~Q(client__agent=None)
    ).annotate(
        month=TruncMonth('pay_month')
    ).values('month').annotate(
        count_paid=Count('id', filter=Q(check_paid=False))
    ).values('month', 'count_paid')

    for i, j in zip(payed_true, payed_false):
        PIE_CHART['paid'].update({
            calendar.month_name[i['month'].month]:
                round(100 * i['count_paid'] / (i['count_paid'] + j['count_paid']))
        })
        PIE_CHART['unpaid'].update({
            calendar.month_name[j['month'].month]:
                round(100 * j['count_paid'] / (i['count_paid'] + j['count_paid']))
        })

    LINE_CHART = {'0': 0}
    for data in models.WorkSheet.objects.annotate(
            month=TruncMonth('date')
    ).values('month').annotate(count=Count('id')).order_by('month'):
        LINE_CHART.update({
            calendar.month_name[data['month'].month]: data['count']
        })

    TOTAL_AMOUNT = request.user.admin.agent_set.aggregate(
        total_amount=Sum('clients__amount_deal'))['total_amount']

    COUNT_CLIENTS = models.WorkSheet.objects.count()

    AGENTS = request.user.admin.agent_set.count()

    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    CLIENTS = models.WorkSheet.objects.annotate(
        boo=F('expiration_date') - days_in_month).filter(
        Q(conclusion_date__gte=F('boo')) & Q(conclusion_date__lte=F('expiration_date')))

    serializer = serializers.WorkSheetShortSerializer(CLIENTS, many=True)

    messages = request.user.admin.messages.all()[:5]
    ser_messages = serializers.MessageSerializer(messages, many=True)

    taxsupervisor = 'clients__workers__supervisor_taxes'
    taxworker = 'clients__workers__worker_taxes'
    acc_serv = 'clients__payments'

    taxes_supervisor = models.Agent.objects.annotate(
        staxcount=Count(taxsupervisor),
        struetax=Count(taxsupervisor, filter=Q(
            clients__workers__supervisor_taxes__check_paid=True))
    ).filter(staxcount__gte=1).values('staxcount', 'struetax', 'pk', 'user__first_name',
                                      'user__last_name')

    taxes_worker = models.Agent.objects.annotate(
        wtaxcount=Count(taxworker),
        wtruetax=Count(taxworker, filter=Q(
            clients__workers__worker_taxes__check_paid=True))
    ).filter(wtaxcount__gte=1).values('wtaxcount', 'wtruetax', 'pk', 'user__first_name',
                                      'user__last_name')

    accounting_services = models.Agent.objects.annotate(
        ascount=Count(acc_serv),
        truecount=Count(acc_serv, filter=Q(
            clients__payments__check_paid=True))
    ).filter(ascount__gte=1).annotate(
        rating=100*F('truecount')/F('ascount')).values('rating')

    result = []
    for i, j, k in zip(taxes_supervisor, taxes_worker, accounting_services):
        rating_one = 100*(i['struetax']+j['wtruetax'])/(i['staxcount']+j['wtaxcount'])
        rating_two = k['rating']
        rating = round((rating_one + rating_two) / 2, 1)
        result.append({
            'pk': i['pk'],
            'first_name': i['user__first_name'],
            'last_name': i['user__last_name'],
            'mark': rating,
        })

    return Response({
        'pie_chart': PIE_CHART,
        'line_chart': LINE_CHART,
        'total_amount': TOTAL_AMOUNT,
        'count_clients': COUNT_CLIENTS,
        'agents_count': AGENTS,
        'clients': serializer.data,
        'messages': ser_messages.data,
        'rating': result
    }, status=status.HTTP_200_OK)


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
                'role': role
            }, status=status.HTTP_200_OK)
        else:
            if user.check_password(password):
                if role == 'agent' and user.agent.is_blocked:
                    return Response({
                        'message': 'Ваш аккаунт заблокирован'
                    }, status=status.HTTP_200_OK)
                token = Token.objects.create(user=user)
                return Response({
                    'access_token': token.key,
                    'role': role
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'Invalid password'
                }, status=status.HTTP_400_BAD_REQUEST)


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
