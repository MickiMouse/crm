import calendar
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class Variables(models.Model):
    monthly_calculation_indicator = models.IntegerField(
        'Месячный расчетный показатель')
    minimal_celery = models.IntegerField('Минимальная зарплата')
    # limit_opv = models.IntegerField('Предел по ОПВ')
    # limit_co = models.IntegerField('Предел по СО')
    # limit_ocmc = models.IntegerField('Предел по ОСМС')
    # limit_ip = models.IntegerField('Предел по ИПН')

    def limit_opv(self):
        return self.minimal_celery * 50 * 0.1

    def limit_co(self):
        return self.minimal_celery * 7 * 0.035

    def limit_ocmc(self):
        return self.minimal_celery * 10 * 0.015

    def limit_ip(self):
        return self.monthly_calculation_indicator * 25

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        pass

    class Meta:
        verbose_name = 'Переманная'
        verbose_name_plural = 'Системные переменные'


def plus_year():
    return timezone.now() + relativedelta(year=1)


class PaydaUser(AbstractUser):
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True)
    is_paydaadmin = models.BooleanField(default=False, db_index=True)
    is_agent = models.BooleanField(default=False, db_index=True)
    is_client = models.BooleanField(default=False, db_index=True)
    is_sales = models.BooleanField(default=False, db_index=True)

    class Meta(AbstractUser.Meta):
        pass


User = get_user_model()


class PaydaAdmin(models.Model):
    CHOICES = (
        ('active', 'Активный'),
        ('inactive', 'Неактивный'),
        ('draft', 'Черновик')
    )
    user = models.OneToOneField(PaydaUser, on_delete=models.CASCADE, null=True,
                                related_name='admin')
    status = models.CharField(max_length=8, choices=CHOICES)
    address = models.CharField(max_length=100, blank=True)
    last_change = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'


class Agent(models.Model):
    user = models.OneToOneField(PaydaUser, on_delete=models.CASCADE, null=True,
                                related_name='agent')
    phone = models.CharField(max_length=13, null=True)
    created_at = models.DateField(default=timezone.now)
    last_change = models.DateField(auto_now=True, null=True)
    is_blocked = models.BooleanField(default=False)
    admin = models.ForeignKey(PaydaAdmin, on_delete=models.PROTECT, null=True)
    # добавить тэги

    def rating(self):

        taxes_supervisor = self.clients.annotate(
            staxcount=models.Count('workers__supervisor_taxes'),
            struetax=models.Count('workers__supervisor_taxes', filter=models.Q(
                workers__supervisor_taxes__check_paid=True))
        ).filter(staxcount__gte=1).values('staxcount', 'struetax')

        taxes_workers = self.clients.annotate(
            wtaxcount=models.Count('workers__worker_taxes'),
            wtruetax=models.Count('workers__worker_taxes', filter=models.Q(
                workers__worker_taxes__check_paid=True))
        ).filter(wtaxcount__gte=1).values('wtaxcount', 'wtruetax')

        accounting_services = self.clients.annotate(
            ascount=models.Count('payments'),
            truecount=models.Count('payments', filter=models.Q(
                payments__check_paid=True))
        ).filter(ascount__gte=1).annotate(
            rating=100*models.F('truecount') / models.F('ascount')).values('rating')

        rating_one, rating_two = 0, 0

        for i, j, k in zip(taxes_supervisor, taxes_workers, accounting_services):
            rating_one = 100*(i['struetax']+j['wtruetax'])/(i['staxcount']+j['wtaxcount'])
            rating_two = k['rating']

        return round((rating_one + rating_two) / 2, 1)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'


class TaxAuthority(models.Model):
    """Налоговый орган УГД"""
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    requisite = models.CharField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Region(models.Model):
    """Область"""
    name = models.IntegerField()
    code = models.IntegerField()


class Activity(models.Model):
    """Вид деятельности"""
    activity = models.CharField(max_length=50)

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'


class Tag(models.Model):
    short = models.CharField(max_length=3, blank=True)
    full = models.CharField(max_length=30, blank=True)


class Archive(models.Model):
    pass


class WorkSheet(models.Model):
    """Клиент"""
    FORMS = (
        ('901', '901'),
    )
    ORGANIZATION = (
        ('ip', 'ИП'),
        ('to', 'ТОО'),
        ('ao', 'АО'),
    )
    forms = models.CharField('Формы', max_length=3, choices=FORMS)
    organization = models.CharField('Организация', max_length=3, choices=ORGANIZATION, blank=True)
    short_name = models.CharField('Краткое наименование компании', max_length=20, blank=True)
    full_name = models.CharField('Полное наименование компании', max_length=100, blank=True)
    bin_iin = models.CharField('Бин/ИИН', max_length=50, blank=True)
    address_physical = models.CharField('Адрес физический', max_length=100, blank=True)
    address_legal = models.CharField('Адрес юридический', max_length=100, blank=True)
    extra_address = models.CharField('Дополнительное поле адреса', max_length=100, blank=True)
    phone = models.CharField('Контактный номер', max_length=13, blank=True)
    bik = models.CharField('БИК', max_length=50, blank=True)
    iik = models.CharField('ИИК', max_length=50, blank=True)
    bank_name = models.CharField('Наименование банка', max_length=20, blank=True)
    position_leader = models.CharField('Должность руководителя', max_length=50, blank=True)  # ДОЛЖНОСТЬ РУКОВОДИТЕЛЯ
    leader = models.CharField('Руководитель ФИО', max_length=100, blank=True)  # РУКОВОДИТЕЛЬ ФИО
    phone_number = models.CharField('Контакты ответственного лица', max_length=13, blank=True)
    date = models.DateField('Дата заполнения анкеты', default=timezone.now)
    last_change = models.DateField('Дата изменения', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True,
                              related_name='clients')
    obj_place = models.CharField('Объект и место', max_length=100, blank=True)
    tax = models.ForeignKey(TaxAuthority, on_delete=models.CASCADE, null=True)
    amount_deal = models.IntegerField('Сумма договора', default=60000)
    conclusion_date = models.DateField('Дата заключения договора', null=True)
    expiration_date = models.DateField('Дата окончания договора', default=plus_year)
    kind_of_activity = models.ManyToManyField(Activity)
    kbe = models.IntegerField('Реквизит')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        amount_month = self.amount_deal / 12
        conclusion_date = self.conclusion_date
        current_month = conclusion_date.month
        current_year = conclusion_date.year
        first_pay = 0

        i = 1
        while i <= 13:
            if current_month == 0:
                current_month = 12

            if i == 13:
                accounting_services = amount_month - first_pay
            elif current_month == conclusion_date.month:
                days = calendar.monthrange(current_year, current_month)[1]
                accounting_services = round(amount_month / days * (days - conclusion_date.day))
                first_pay = accounting_services
            else:
                accounting_services = amount_month

            PaidForDeal.objects.get_or_create(
                client=self,
                pay_month=timezone.datetime(current_year,
                                            current_month,
                                            conclusion_date.day),
                amount=accounting_services)

            current_month += 1
            current_month %= 12
            i += 1

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Worker(models.Model):
    POSITION = (
        ('supervisor', 'Руководитель'),
        ('employee', 'Сотрудник'))
    DISABILITY = (
        ('', 'Нет инвалидности'),
        ('1', '1 группа'),
        ('2', '2 группа'),
        ('3', '3 группа'),
        ('1b', '1 группа, бессрочно'),
        ('2b', '2 группа, бессрочно'),
        ('3b', '3 группа, бессрочно'))
    client = models.ForeignKey(WorkSheet, on_delete=models.CASCADE, null=True,
                               related_name='workers')
    last_name = models.CharField('Фамилия', max_length=20)
    first_name = models.CharField('Имя', max_length=20)
    patronymic = models.CharField('Отчество', max_length=30)
    position = models.CharField('Должность', max_length=10, choices=POSITION)
    iin = models.CharField('ИИН', max_length=12)
    earn = models.IntegerField('Заработанная плата "на руки"', default=0)
    disability = models.CharField('Инвалидность', max_length=2, choices=DISABILITY,
                                  blank=True)
    resident = models.BooleanField('Резидент')
    tax_deduction = models.BooleanField('Налоговый вычет МЗП')
    pensioner = models.BooleanField('Пенсионер')
    contract = models.BooleanField('По договору ГПХ')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.position == 'employee':
            TaxesWorker.objects.get_or_create(
                iin=self.iin, worker=self, name=self.first_name)
        else:
            TaxesSupervisor.objects.get_or_create(supervisor=self)

        # amount_month = self.amount_deal / 12
        # conclusion_date = self.client.conclusion_date
        # current_month = conclusion_date.month
        # current_year = conclusion_date.year
        #

        # i = 1
        # while i <= 13:
        #     if current_month == 0:
        #         current_month = 12
        #
        #     if i == 13:
        #         accounting_services = amount_month - first_pay
        #     elif current_month == conclusion_date.month:
        #         days = calendar.monthrange(current_year, current_month)[1]
        #         accounting_services = round(amount_month / days * (days - conclusion_date.day))
        #         first_pay = accounting_services
        #     else:
        #         accounting_services = amount_month
        #
        #     PaidForDeal.objects.get_or_create(
        #         client=self,
        #         pay_month=timezone.datetime(current_year,
        #                                     current_month,
        #                                     conclusion_date.day),
        #         amount=accounting_services)
        #
        #     current_month += 1
        #     current_month %= 12
        #     i += 1
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class PaidForDeal(models.Model):
    """Бухгалтерские услуги"""
    client = models.ForeignKey(WorkSheet, on_delete=models.CASCADE,
                               related_name='payments')
    pay_month = models.DateField('Месяц')
    check_paid = models.BooleanField(default=False)
    amount = models.IntegerField('Сумма за месяц')

    class Meta:
        verbose_name = 'Бухгалтерская услуга'
        verbose_name_plural = 'Бухгалтерские услуги'
        ordering = ['pay_month']


class TaxesSupervisor(models.Model):
    month = models.DateField('Месяц')
    supervisor = models.ForeignKey(Worker, on_delete=models.CASCADE,
                                   related_name='supervisor_taxes')
    check_paid = models.BooleanField(default=False)

    def earn(self):
        return self.supervisor.earn

    def profit(self):
        return round(self.supervisor.earn / .9, 2)

    def pension_contrib(self):
        return round(self.profit() * .1, 2)

    def income_for_so(self):
        return round(self.profit() - self.pension_contrib(), 2)

    def social_contrib(self):
        return round(self.income_for_so() * .035, 2)

    def osms(self):
        return 0

    class Meta:
        verbose_name = 'Налоги руководителя'
        verbose_name_plural = 'Налоги руководителей'


class TaxesWorker(models.Model):
    month = models.DateField('Месяц', default=timezone.now)
    name = models.CharField('ФИО', max_length=100)
    iin = models.CharField('ИИН', max_length=50)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,
                               related_name='worker_taxes')
    check_paid = models.BooleanField(default=False)

    def profit(self):
        coef = .891 if self.worker.earn < 60000 else .81
        if self.worker.pensioner or not self.worker.resident:
            coef = .9
        return round(self.worker.earn / coef, 2)

    def earn(self):
        return self.worker.earn

    def pension_contrib(self):
        return round(self.profit() * .1, 2)

    def individual_income_tax(self):
        var = Variables.objects.get(pk=1)
        if not self.worker.resident:
            return round(self.profit() * .1, 2)
        else:
            if self.profit() > var.limit_ip():
                return round((self.profit() - self.pension_contrib() - var.minimal_celery) * .1, 2)
            else:
                return round((self.profit() - self.pension_contrib() - var.minimal_celery) * .01, 2)

    def adjustment(self):
        var = Variables.objects.get(pk=1)
        value = round((self.profit() - self.pension_contrib() - var.minimal_celery) * .9, 2)
        return 0 if self.profit() > var.limit_ip() else value

    def social_contrib(self):
        return round((self.profit() - self.pension_contrib()) * .035, 2)

    def med_contrib(self):
        return round((self.profit() - self.adjustment()) * .015, 2)

    class Meta:
        verbose_name = 'Налоги работника'
        verbose_name_plural = 'Налоги работников'


class Message(models.Model):
    admin = models.ForeignKey(PaydaAdmin, on_delete=models.CASCADE,
                              related_name='agents_messages')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE,
                              related_name='admins_massages')
    mess = models.CharField('Сообщение', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class AdminClientMessage(models.Model):
    pass


class AgentClientTaxesMessage(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    client = models.ForeignKey(WorkSheet, on_delete=models.CASCADE)
    message = models.CharField('Сообщение', max_length=50)
    created_at = models.DateField(auto_now_add=True)


class AgentClientAccountingServicesMessage(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    client = models.ForeignKey(WorkSheet, on_delete=models.CASCADE)
    message = models.CharField('Сообщение', max_length=50)
    created_at = models.DateField(auto_now_add=True)


class Comment(models.Model):
    client = models.ForeignKey(WorkSheet, on_delete=models.CASCADE,
                               related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Task(models.Model):
    pass



