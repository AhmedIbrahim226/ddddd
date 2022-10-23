from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from .models import TenantDomain, Tenant
from django.contrib.auth import logout
from utility.http_response import url_properties
from .forms import (
    LoginForm,
)

class MemberInfoView(TemplateView):
    template_name = 'member_info.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class HomeView(TemplateView):
    template_name = 'home_view.html'

    def get_context_data(self, **kwargs):
        tenant_domain = TenantDomain.objects.all()
        return  {'tenant_domain': tenant_domain}
    
    def post(self, request, *args, **kwargs):
        protocol, hostname, port = url_properties(request)

        tenant_id = request.POST.get('tenant_id')
        tenant = Tenant.objects.get(id=tenant_id)
        domain =  tenant.tenant_domain.domain_name
        subdomain = tenant.tenant_subdomain

        login_url = reverse('login_view')
        
        return HttpResponseRedirect("{}://{}.{}.{}:{}{}".format(protocol, subdomain, domain, hostname, port, login_url))

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'signin.html'
    success_url = reverse_lazy('member_info_view')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


