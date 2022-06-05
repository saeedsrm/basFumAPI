from django.contrib import admin
from monolith.accounts.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass