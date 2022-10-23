from user.models import TenantDomain, Tenant, User
from django.db.models import Q

class UserAuthentication():
    def authenticate(self, request, username=None, password=None):
            hostname = request.get_host().split(':')[0].lower()
            domain = hostname.split('.')[1]
            subdomain = hostname.split('.')[0]

            try:
                domain = TenantDomain.objects.get(domain_name=domain)
            except TenantDomain.DoesNotExist:
                domain = None
            
            tenant = Tenant.objects.filter(Q(tenant_domain=domain) | Q(tenant_domain=None), tenant_subdomain=subdomain).first()

            try:
                user = User.objects.get(tenant=tenant,  email=username)
                success = user.check_password(password)
                if success:
                    return user
            except User.DoesNotExist:
                return


    def get_user(self, uid):
        try:
            return User.objects.get(pk=uid)
        except User.DoesNotExist:
            return 
