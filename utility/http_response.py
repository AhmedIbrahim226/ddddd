from user.models import Tenant
from django.http import HttpResponseForbidden
from urllib.parse import urlparse


def url_properties(request):
    full_path = request.build_absolute_uri()
    url = urlparse(full_path)
    protocol = url.scheme
    hostname = url.hostname.split('.')[1]
    port = url.port

    return protocol, hostname, port
