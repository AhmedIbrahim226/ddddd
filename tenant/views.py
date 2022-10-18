from django.shortcuts import render
from django.views.generic import TemplateView
from .utilities import hostname_from_request, tenant_from_request


class MemberInfoView(TemplateView):
    template_name = 'member_info.html'

    def get_context_data(self, **kwargs):
        hostname = hostname_from_request(self.request)
        print(hostname)
        tenant = tenant_from_request(self.request)
        print(tenant)
        return super().get_context_data(**kwargs)
