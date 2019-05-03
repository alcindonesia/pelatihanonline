from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url

from .views import RegistrationView

urlpatterns = []

if getattr(settings, 'INCLUDE_REGISTER_URL', True):
    urlpatterns += [
        url(r'^register/$',
            RegistrationView.as_view(
                success_url=getattr(settings, 'SIMPLE_BACKEND_REDIRECT_URL', '/'),
            ),
            name='registration_register'),
    ]

if getattr(settings, 'INCLUDE_AUTH_URLS', True):
    urlpatterns += [
        url(r'', include('registration.auth_urls')),
    ]
