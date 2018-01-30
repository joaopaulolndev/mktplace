from django.shortcuts import render, render_to_response


def register(request):
    #return render(request, 'registration/register.html', {})
    return render_to_response('registration/register.html', {})


def register_success(request):
    #return render_to_response('registration/success.html')
    pass


