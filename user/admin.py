from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserEmailFoundation, TenantDomain, Tenant, User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'tenant', 'is_active', 'is_superuser', 'is_staff')
    ordering = ('tenant',)
    search_fields = ('email', 'tenant')
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter 	  = ()
    fieldsets = (
		(None, {
			"fields": ('tenant', 'email', 'password')}),
		('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
		('Personal', {'fields': ('date_joined', 'last_login')})
	)
    add_fieldsets = (
		(None, {
				'classes': ('wide',),
				'fields': ('tenant', 'email', 'password1', 'password2',
               	'is_staff', 'is_active', 'is_superuser')
			 }
		),
	)

admin.site.register(UserEmailFoundation)
admin.site.register(TenantDomain)
admin.site.register(Tenant)
