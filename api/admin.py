from django.contrib import admin

from api import models


class AdminPaydaUser(admin.ModelAdmin):
    list_display = ('username', 'email')


admin.site.register(models.PaydaUser, AdminPaydaUser)


class AdminPaydaAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')


admin.site.register(models.PaydaAdmin, AdminPaydaAdmin)


class AdminPaydaAgent(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'is_blocked')


admin.site.register(models.Agent, AdminPaydaAgent)


class AdminClient(admin.ModelAdmin):
    list_display = ('pk', 'amount_deal', 'short_name', 'date')


admin.site.register(models.WorkSheet, AdminClient)


class AdminActivity(admin.ModelAdmin):
    list_display = ('activity',)


admin.site.register(models.Activity, AdminActivity)


class AdminPaid(admin.ModelAdmin):
    list_display = ('check_paid', 'client')


admin.site.register(models.PaidForDeal, AdminPaid)


class AdminMessage(admin.ModelAdmin):
    list_display = ('mess',)


admin.site.register(models.Message, AdminMessage)


class AdminWorker(admin.ModelAdmin):
    list_display = ('position', 'earn', 'client')


admin.site.register(models.Worker, AdminWorker)


class AdminTaxSupervisor(admin.ModelAdmin):
    list_display = ('check_paid', 'supervisor')


admin.site.register(models.TaxesSupervisor, AdminTaxSupervisor)


class AdminTaxWorker(admin.ModelAdmin):
    list_display = ('check_paid', 'worker')


admin.site.register(models.TaxesWorker, AdminTaxWorker)

