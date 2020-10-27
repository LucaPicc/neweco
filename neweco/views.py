from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

class Index(TemplateView):
    template_name = "index.html"


def Contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['asunto']
            from_email = form.cleaned_data['email_contac']
            message = form.cleaned_data['cuerpo']
            try:
                send_mail(subject, message + from_email, 'superfalsoflaso@gmail.com',['superfalsoflso@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, "contacto.html", {'form': form})

class Graf(TemplateView):
    template_name = 'girsu/girsu_estadisticas.html'
