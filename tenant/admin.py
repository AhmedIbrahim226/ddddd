from django.contrib import admin
from .models import Tenant, Member


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['name', 'subdomain']


admin.site.register(Member)
