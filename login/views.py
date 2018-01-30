from django.shortcuts import render, render_to_response
from login.forms import RegistrationForm


def register(request):
    form = RegistrationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def register_success(request):
    #return render_to_response('registration/success.html')
    pass


