from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class Variables(models.Model):
    monthly_calculation_indicator = models.IntegerField(
        'Месячный расчетный показатель')
    minimal_celery = models.IntegerField('Минимальная зарплата')
    limit_opv = models.IntegerField('Предел по ОПВ')
    limit_co = models.IntegerField('Предел по СО')
    limit_ocmc = models.IntegerField('Предел по ОСМС')
    limit_ip = models.IntegerField('Предел по ИПН')

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        pass


def plus_year():
    return timezone.now() + relativedelta(year=1)


class PaydaUser(AbstractUser):
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
    telephone = models.CharField(max_length=13, null=True)
    last_change = models.DateTimeField(auto_now=True, null=True)
    is_blocked = models.BooleanField(default=False)
    admin = models.ForeignKey(PaydaAdmin, on_delete=models.PROTECT, null=True)
    # ТЭГ

    def rating(self):
        self.clients.worker_set.all()

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


class Tag(models.Model):
    pass


class Archive(models.Model):
    pass


class WorkSheet(models.Model):
    """Client"""
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
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True,
                              related_name='clients')
    obj_place = models.CharField('Объект и место', max_length=100, blank=True)
    tax = models.ForeignKey(TaxAuthority, on_delete=models.CASCADE, null=True)  # УГД регистрация – выпадающий список с единичным выбором из УДП
    amount_deal = models.IntegerField('Сумма договора', default=60000)
    conclusion_date = models.DateField('Дата заключения договора', null=True)
    expiration_date = models.DateField('Дата окончания договора', default=plus_year)
    kind_of_activity = models.ManyToManyField(Activity)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)
        PaidForDeal.objects.get_or_create(
            client=self,
            pay_month=self.date
        )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Worker(models.Model):
    POSITION = (
        ('supervisor', 'Руководитель'),
        ('employee', 'Сотрудник'))
    MONTHS = (
        ('Jan', 'Январь'),
        ('Feb', 'Февраль'),
        ('Mar', 'Март'),
        ('Apr', 'Апрель'),
        ('May', 'Май'),
        ('Jun', 'Июнь'),
        ('Jul', 'Июль'),
        ('Aug', 'Август'),
        ('Sep', 'Сентябрь'),
        ('Oct', 'Октябрь'),
        ('Nov', 'Ноябрь'),
        ('Dec', 'Декабрь'))
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
    month = models.CharField('Месяц', max_length=3, choices=MONTHS)
    earn = models.IntegerField('Заработанная плата "на руки"', default=0)
    disability = models.CharField('Инвалидность', max_length=2, choices=DISABILITY,
                                  blank=True)
    resident = models.BooleanField('Резидент')
    tax_deduction = models.BooleanField('Налоговый вычет МЗП')
    pensioner = models.BooleanField('Пенсионер')
    contract = models.BooleanField('По договору ГПХ')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class PaidForDeal(models.Model):
    client = models.ForeignKey(WorkSheet, on_delete=models.CASCADE,
                               related_name='payments')
    pay_month = models.DateField()
    check_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['pay_month']


class TaxesSupervisor(models.Model):
    supervisor = models.ForeignKey(Worker, on_delete=models.CASCADE,
                                   related_name='supervisor_taxes')
    check_paid = models.BooleanField(default=False)

    def period(self):
        return self.supervisor.month

    def earn(self):
        return self.supervisor.earn

    def profit(self):
        return self.supervisor.earn / .9

    def pension_contrib(self):
        return self.profit() * .1

    def income_for_so(self):
        return self.profit() - self.pension_contrib()

    def social_contrib(self):
        return round(self.income_for_so() * .035)


class TaxesWorker(models.Model):
    name = models.CharField('ФИО', max_length=100)
    iin = models.CharField('ИИН', max_length=50)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,
                               related_name='worker_taxes')
    check_paid = models.BooleanField(default=False)

    def period(self):
        return self.worker.month

    def profit(self):
        coef = .891 if self.worker.earn < 60000 else .81
        if self.worker.pensioner or not self.worker.resident:
            coef = .9
        return self.worker.earn / coef

    def earn(self):
        return self.worker.earn

    def pension_contrib(self):
        return self.profit() * .1

    def individual_income_tax(self):
        var = Variables.objects.get(pk=1)
        if not self.worker.resident:
            return self.profit() * .1
        else:
            if self.profit() > var.limit_ip:
                return (self.profit() - self.pension_contrib() - var.minimal_celery) * .1
            else:
                return (self.profit() - self.pension_contrib() - var.minimal_celery) * .01

    def adjustment(self):
        var = Variables.objects.get(pk=1)
        value = (self.profit() - self.pension_contrib() - var.minimal_celery) * .9
        return 0 if self.profit() > var.limit_ip else value

    def social_contrib(self):
        return (self.profit() - self.pension_contrib()) * .035

    def med_contrib(self):
        return (self.profit() - self.adjustment()) * .015


class Message(models.Model):
    admin = models.ForeignKey(PaydaAdmin, on_delete=models.CASCADE,
                              related_name='messages')
    mess = models.CharField('Сообщение', max_length=50)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Comment(models.Model):
    client = models.ForeignKey(WorkSheet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)








