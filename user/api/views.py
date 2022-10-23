from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from ..models import TenantDomain, Tenant
from .serializers import (
    TenantSerializer
)

class TenantRetrieveAPI(CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        tenant_domain_id = self.request.data.get('tenant_domain_id')
        tenant_domain = TenantDomain.objects.get(id=tenant_domain_id)
        queryset = Tenant.objects.filter(tenant_domain=tenant_domain)
        return queryset

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serial = self.get_serializer(instance=queryset, many=True)
        return Response(serial.data)


    