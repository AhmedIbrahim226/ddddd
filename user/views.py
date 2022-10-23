from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import TenantDomain, Tenant
from django.contrib.auth import authenticate, login , logout
from utility.http_response import url_properties


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

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
    return render(request, 'signin.html', {})


