from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.utils.module_loading import import_string
from registration.backends.simple.views import RegistrationView as BaseRegistrationView
from registration import signals
from .forms import UserCreateForm

class RegistrationView(BaseRegistrationView):
    success_url = 'registration_complete'
    form_class = UserCreateForm

    def register(self, form):
        new_user, new_userprofile = form.save()
        username_field = getattr(new_user, 'USERNAME_FIELD', 'username')
        new_user = authenticate(
            username=getattr(new_user, username_field),
            password=form.cleaned_data['password1']
        )

        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user
