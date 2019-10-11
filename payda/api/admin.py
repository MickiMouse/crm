from django.contrib import admin

from api import models


class AdminPaydaUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name')


admin.site.register(models.PaydaUser, AdminPaydaUser)


class AdminPaydaAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')


admin.site.register(models.PaydaAdmin, AdminPaydaAdmin)


class AdminPaydaAgent(admin.ModelAdmin):
    list_display = ('user', 'rating', 'phone', 'is_blocked')


admin.site.register(models.Agent, AdminPaydaAgent)


class AdminClient(admin.ModelAdmin):
    list_display = ('pk', 'amount_deal', 'short_name', 'date')


admin.site.register(models.WorkSheet, AdminClient)


class AdminActivity(admin.ModelAdmin):
    list_display = ('activity',)


admin.site.register(models.Activity, AdminActivity)


class AdminPaid(admin.ModelAdmin):
    list_display = ('amount', 'pay_month','check_paid', 'client')


admin.site.register(models.PaidForDeal, AdminPaid)


class AdminMessage(admin.ModelAdmin):
    list_display = ('mess',)


admin.site.register(models.Message, AdminMessage)


class AdminWorker(admin.ModelAdmin):
    list_display = ('position', 'earn', 'client')


admin.site.register(models.Worker, AdminWorker)


class AdminTaxSupervisor(admin.ModelAdmin):
    list_display = ('check_paid',
                    'supervisor',
                    'earn',
                    'profit',
                    'pension_contrib',
                    'income_for_so',
                    'social_contrib',
                    'osms')


admin.site.register(models.TaxesSupervisor, AdminTaxSupervisor)


class AdminTaxWorker(admin.ModelAdmin):
    list_display = ('check_paid',
                    'worker',
                    'earn',
                    'profit',
                    'individual_income_tax',
                    'pension_contrib',
                    'adjustment',
                    'social_contrib',
                    'med_contrib')


admin.site.register(models.TaxesWorker, AdminTaxWorker)


class TaxesMessage(admin.ModelAdmin):
    list_display = ('message', 'created_at')


admin.site.register(models.AgentClientTaxesMessage, TaxesMessage)


class AccountingMessage(admin.ModelAdmin):
    list_display = ('message', 'created_at')


admin.site.register(models.AgentClientAccountingServicesMessage, AccountingMessage)


class AdminVars(admin.ModelAdmin):
    list_display = ('monthly_calculation_indicator',
                    'minimal_celery',
                    'limit_opv',
                    'limit_co',
                    'limit_ocmc',
                    'limit_ip')


admin.site.register(models.Variables, AdminVars)
