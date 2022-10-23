from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserEmailFoundation(models.Model, BaseUserManager):
    email = models.EmailField(max_length=50, unique=True)


    def save(self, *args, **kwargs):
        self.email = self.normalize_email(self.email)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email

@receiver(pre_delete, sender=UserEmailFoundation)
def scans_assets_files(sender, instance, **kwargs):
    user_email = User.objects.filter(email=instance.email)
    user_email.delete()

class TenantDomain(models.Model):
    domain_name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.domain_name

class Tenant(models.Model):
    tenant_owner = models.CharField(max_length=50)
    tenant_email = models.OneToOneField(UserEmailFoundation, on_delete=models.CASCADE)
    tenant_domain = models.ForeignKey(TenantDomain, on_delete=models.CASCADE, blank=True, null=True, related_name="tenant_domain")
    tenant_subdomain = models.CharField(max_length=50)
    tenant_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tenant_subdomain

class UserManager(BaseUserManager):
    
    def create_user(self, tenant, email, password=None):
        user = self.model(
            tenant=tenant,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, tenant, email, password):
        tenant = Tenant.objects.get(id=tenant)
        user = self.create_user(
            tenant=tenant,
            email=self.normalize_email(email),
            password=password
        )
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['tenant']
    
    objects = UserManager()
    
    def __str__(self) -> str:
        return 'User: {} belong to tenant: {}'.format(self.email, self.tenant)
    
    def has_perm(self, perm, obj=None):
        return self.is_staff
 
    def has_module_perms(self, app_label):
        return True
