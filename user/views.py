from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView, ListView
from .forms import CrearUserForm, CrearUserForm2, CrearEntidadForm
from .models import UserCustom, Entidad

class HomeView(TemplateView):
    template_name = "user/home.html"

class UserAdminECreateView(CreateView):
    model = UserCustom
    template_name = "user/crear_user.html"
    form_class = CrearUserForm

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = UserCustom(
                username = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                is_admin_entity = True,
                entity_id = form.cleaned_data.get('entity').id
            )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )

class UserECreateView(CreateView):
    model = UserCustom
    template_name = "user/crear_user.html"
    form_class = CrearUserForm2

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        userlog = UserCustom.objects.get(id = request.user.id)
        if form.is_valid():
            new_user = UserCustom(
                username = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                is_user_entity = True,
                entity_id = userlog.entity_id
            )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )

class AdminCreateView(CreateView):
    model = UserCustom
    template_name = "user/crear_user.html"
    form_class = CrearUserForm2

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        userlog = UserCustom.objects.get(id = request.user.id)
        if form.is_valid():
            new_user = UserCustom(
                username = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                is_super_admin = True,
            )
            new_user.set_password(form.cleaned_data.get('password1'))
            new_user.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'form':form} )


class EntidadCreateView(CreateView):
    model = Entidad
    template_name = "user/crear_user.html"
    form_class = CrearEntidadForm
    success_url = '/'


class EntidadListView(ListView):
    model = Entidad
    template_name = "user/list_en.html"


