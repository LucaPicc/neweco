from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import CargaProdForm, CargaMatForm, ProdMatForm,LocalForm, CompRecForm
from .models import Mat, Prod, ProdMat, Localidad, CompRec

class CargaMatView(FormView):
    template_name = 'mercado/c_mat.html'
    form_class = CargaMatForm

    def post(self, request, *args, **kwargs):
        formu =self.form_class(request.POST)
        if formu.is_valid():
            mat = Mat(
                nom = formu.cleaned_data.get('nombre'),
                desc = formu.cleaned_data.get('descripcion')
            )
            mat.save()
            return redirect('home')
        else:
            return redirect(request,self.template_name,{'formu':formu})

class CargaProdView(FormView):
    template_name = 'mercado/c_prod.html'
    form_class = CargaProdForm

    def post(self, request, *args, **kwargs):
        formu = self.form_class(request.POST)
        if formu.is_valid():
            prod = Prod(
                nom = formu.cleaned_data.get('nombre'),
                descr =  formu.cleaned_data.get('descripcion')
            )
            i = formu.cleaned_data.get('cant_comp')
            prod.save()
            return redirect('prod_mat',i = i,pid = prod.id)
        else:
            return render(self.template_name,{'formu':formu})

class ProdMatView(FormView):
    template_name = 'mercado/prod_mat.html'
    form_class = ProdMatForm

    def post(self,request,pid, i ,*args, **kwargs):
        formu = self.form_class(request.POST)
        if formu.is_valid():
            pm = ProdMat(
                prod = Prod.objects.get(id = pid),
                mat = formu.cleaned_data.get('mat'),
                porc = formu.cleaned_data.get('porc'),
            )
            pm.save()
            i-=1
            if i == 0:
                return redirect('home')
            else:
                return redirect('prod_mat',i = i, pid = pid)
        else:
            return render(self.template_name,{'formu':formu})

class CargaLocalView(FormView):
    template_name = 'mercado/local.html'
    form_class = LocalForm

    def post(self, request,*args, **kwargs):
        formu = self.form_class(request.POST)
        if formu.is_valid():
            lo = Localidad(
                nom = formu.cleaned_data.get('nombre'),
                pais = formu.cleaned_data.get('pais'),
                prov = formu.cleaned_data.get('provincia'),
                g_rec_sol = formu.cleaned_data.get('residuos'),
            )
            lo.save()
            cp = formu.cleaned_data.get('cant_rec')
            cr = formu.cleaned_data.get('residuos')
            pr = formu.cleaned_data.get('porc_rec')
            li = Localidad.objects.get(nom = formu.cleaned_data.get('nombre')).id
            return redirect('prod_rec',cp = cp , cr = cr, li = li)
        else:
            return render(self.template_name,{'formu':formu})

class CompRecView(FormView):
    template_name = 'mercado/comp.html'
    form_class = CompRecForm

    def post(self, request, cp, cr, pr, li, *args, **kwargs):
        formu = self.form_class(reques.POST)
        if formu.is_valid():
            com_r = CompRec(
                localidad = Localidad.objects.get(id = li),
                prod = formu.cleaned_data.get('prod'),
                porc = formu.cleaned_data.get('porc'),
            )
            com_r.save()
            cp-=1
            if cp == 0:
                return redirect('home')
            else:
                return redirect('prod_rec',cp = cp, cr = cr, li = li)