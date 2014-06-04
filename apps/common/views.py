from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext as _


def password_change_done(request):
    messages.success(request, _(u'Your password has been successfully changed.'))
    return redirect('home')
