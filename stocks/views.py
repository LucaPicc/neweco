from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView, ListView, UpdateView
from .forms import IngStockMatForm,IngStockProdForm,EnvPForm, EnvMForm
from .models import StockMat,StockProd,MovSM,MovSP, EnvP,RecP
from user.models import UserCustom, Entidad

class IngStockPView(FormView):
    template_name = 'stock/ing_prod.html'
    form_class = IngStockProdForm

    def post(self,request,*args, **kwargs):
        formu = self.form_class(request.POST)
        userl = UserCustom.objects.get(id = request.user.id)
        en = Entidad.objects.get(id = userl.entity_id)

        if formu.is_valid():
            
            sp = StockProd(
                entidad = en,
                prod = formu.cleaned_data.get('prod'),
                unidad = formu.cleaned_data.get('unidad'),
                cant = formu.cleaned_data.get('cantidad')  
            )
            mv = MovSP(
                user = userl,
                prod = formu.cleaned_data.get('prod'),
                unidad = formu.cleaned_data.get('unidad'),
                cant = formu.cleaned_data.get('cantidad'),
                tipo = 'IN'
            )
            mv.save()

            if StockProd.objects.filter(entidad_id = sp.entidad_id, prod_id = sp.prod_id).exists():
                sp_c = StockProd.objects.filter(entidad_id = sp.entidad_id, prod_id = sp.prod_id).get()
                if sp_c.unidad == sp.unidad:
                    c_c = sp_c.cant + sp.cant
                    sp_c.cant = c_c
                    sp_c.save()
                else:
                    if sp_c.unidad == 'Tn':
                        c_c = sp_c.cant + sp.cant/1000
                        sp_c.cant = c_c
                        sp_c.save()
                    else:
                        c_c = sp_c.cant + sp.cant*1000
                        sp_c.cant = c_c
                        sp_c.save()
                return redirect('home')
            else:
                sp.save()
                return redirect('home')
        else:
            return render(self.template_name,{'formu':formu})

class IngStockMView(FormView):
    template_name = 'stock/ing_mat.html'
    form_class = IngStockMatForm

    def post(self,request,*args, **kwargs):
        formu = self.form_class(request.POST)
        userl = UserCustom.objects.get(id = request.user.id)
        en = Entidad.objects.get(id = userl.entity_id)

        if formu.is_valid():
            
            sm = StockMat(
                entidad = en,
                mat= formu.cleaned_data.get('mat'),
                unidad = formu.cleaned_data.get('unidad'),
                cant = formu.cleaned_data.get('cantidad')  
            )
            mv = MovSM(
                user = userl,
                mat = formu.cleaned_data.get('mat'),
                unidad = formu.cleaned_data.get('unidad'),
                cant = formu.cleaned_data.get('cantidad'),
                tipo = 'IN'
            )
            mv.save()

            if StockMat.objects.filter(entidad_id = sm.entidad_id, mat_id = sm.mat_id).exists():
                sm_c = StockMat.objects.filter(entidad_id = sm.entidad_id, mat_id = sm.mat_id).get()
                if sm_c.unidad == sm.unidad:
                    c_c = sm_c.cant + sm.cant
                    sm.cant = c_c
                    sm_c.save()
                else:
                    if sm_c.unidad == 'Tn':
                        c_c = sm_c.cant + sm.cant/1000
                        sm_c.cant = c_c
                        sm_c.save()
                    else:
                        c_c = sm_c.cant + sm.cant*1000
                        sm_c = c_c
                        sm_c.save()
                return redirect('home')
            else:
                sm.save()
            return redirect('home')
        else:
            return render(self.template_name,{'formu':formu})

class TabEnv(TemplateView):
    template_name = 'stock/env_tab.html'

class REnvPView(FormView):
    template_name='stock/r_env_prod.html'
    form_class = EnvPForm

    def post(self, request,*args, **kwargs):
        formu = self.form_class(request.POST)
        userl = UserCustom.objects.get(id = request.user.id)
        en = Entidad.objects.get(id = userl.entity_id)

        if formu.is_valid():
            env_p = EnvP(
                ent = formu.cleaned_data.get('entidad'),
                prod = formu.cleaned_data.get('producto'),
                unidad = formu.cleaned_data.get('unidad'),
                cant = formu.cleaned_data.get('cantidad'),
            )
            if StockProd.objects.filter(entidad = en, prod = env_p.prod).exists():
                p_s = StockProd.objects.filter(entidad = en, prod = env_p.prod).get()
                if p_s.unidad == env_p.unidad:
                    if p_s.cant < env_p.cant:
                        return HttpResponse('<h1>No tiene suficiente producto</h1>')
                    else:
                        c_c = p_s.cant - env_p.cant
                        p_s.cant = c_c
                        p_s.save()
                        env_p.cant
                        env_p.save()
                        
                        mv = MovSP(
                            user = userl,
                            prod = formu.cleaned_data.get('producto'),
                            unidad = formu.cleaned_data.get('unidad'),
                            cant = formu.cleaned_data.get('cantidad'),
                            tipo = 'SA'
                        )
                        mv.save()

                        r_p = RecP(
                            ent = en,
                            env_id = EnvP.objects.get(prod = env_p.prod, ent = env_p.ent).id,
                            recp = False,
                        )
                        r_p.save()
                        return redirect('home')
                else:
                    if p_s.unidad == 'Tn':
                        if p_s.cant < env_p.cant/1000:
                            return HttpResponse('<h1>No tiene suficiente producto</h1>')
                        else:
                            
                            c_c = p_s.cant - env_p.cant/1000
                            p_s.cant = round(c_c,2)
                            p_s.save()
                            env_p.cant
                            
                            mv = MovSP(
                                user = userl,
                                prod = formu.cleaned_data.get('producto'),
                                unidad = formu.cleaned_data.get('unidad'),
                                cant = formu.cleaned_data.get('cantidad'),
                                tipo = 'SA'
                            )
                            mv.save()

                            r_p = RecP(
                                ent = en,
                                env_id = EnvP.objects.get(prod = env_p.prod, ent = env_p.ent).id,
                                recp = False,
                            )
                            r_p.save()
                            return redirect('home')

                    else:
                        if p_s.cant < env_p.cant*1000:
                            return HttpResponse('<h1>No tiene suficiente producto</h1>')
                        else:
                            
                            c_c = p_s.cant - env_p.cant*1000
                            p_s.cant = round(c_c,2)
                            p_s.save()
                            env_p.cant
                            
                            mv = MovSP(
                                user = userl,
                                prod = formu.cleaned_data.get('producto'),
                                unidad = formu.cleaned_data.get('unidad'),
                                cant = formu.cleaned_data.get('cantidad'),
                                tipo = 'SA'
                            )
                            mv.save()

                            r_p = RecP(
                                ent = en,
                                env_id = EnvP.objects.get(prod = env_p.prod, ent = env_p.ent).id,
                                recp = False,
                            )
                            r_p.save()
                            return redirect('home')
        else:
            return render(self.template_name,{'formu':formu})
        return redirect('home')

class REnvMView(FormView):
    template_name='stock/r_env_mat.html'
    form_class = EnvMForm

    def post(self, request,*args, **kwargs):
        formu = self.form_class(request.POST)
        userl = UserCustom.objects.get(id = request.user.id)
        en = Entidad.objects.get(id = userl.entity_id)

        if formu.is_valid():
            env_m = EnvM(
                mat = formu.cleaned_data.get('material'),
                unidad = formu.cleaned_data.get('unidad'),
                cant = formu.cleaned_data.get('cantidad'),
                entidad_id = formu.cleaned_data.get('entidad')
            )
            if StockMat.objects.filter(entidad_id = en, mat = env_m.mat).exists():
                p_s = StockProd.objects.filter(entidad_id = en, mat = env_m.mat).get()
                if m_s.unidad == env_m.unidad:
                    if m_s.cant < env_m.cant:
                        return HttpResponse('<h1>No tiene suficiente material</h1>')
                    else:
                        c_c = m_s.cant - env_m.cant
                        m_s.cant = c_c
                        m_s.save()
                        env_m.cant
                        
                        mv = MovSM(
                            user = userl,
                            mat = formu.cleaned_data.get('material'),
                            unidad = formu.cleaned_data.get('unidad'),
                            cant = formu.cleaned_data.get('cantidad'),
                            tipo = 'SA'
                        )
                        mv.save()

                        r_m = RecM(
                            ent = en,
                            env_id = EnvM.objects.get(mat = env_m.mat, ent = env_m.ent).id,
                            recp = False,
                        )
                        r_m.save()
                        return redirect('home')
                else:
                    if m_s.unidad == 'Tn':
                        if m_s.cant < env_m.cant/1000:
                            return HttpResponse('<h1>No tiene suficiente producto</h1>')
                        else:
                            
                            c_c = p_s.cant - env_m.cant/1000
                            m_s.cant = round(c_c,2)
                            m_s.save()
                            env_m.cant
                            
                            mv = MovSM(
                                user = userl,
                                mat = formu.cleaned_data.get('material'),
                                unidad = formu.cleaned_data.get('unidad'),
                                cant = formu.cleaned_data.get('cantidad'),
                                tipo = 'SA'
                            )
                            mv.save()

                            r_m = RecM(
                                ent = en,
                                env_id = EnvM.objects.get(mat = env_m.prod, ent = env_m.ent).id,
                                recp = False,
                            )
                            r_m.save()
                            return redirect('home')

                    else:
                        if m_s.cant < env_m.cant*1000:
                            return HttpResponse('<h1>No tiene suficiente material</h1>')
                        else:
                            
                            c_c = m_s.cant - env_m.cant*1000
                            m_s.cant = round(c_c,2)
                            m_s.save()
                            env_m.cant
                            
                            mv = MovSM(
                                user = userl,
                                mat = formu.cleaned_data.get('material'),
                                unidad = formu.cleaned_data.get('unidad'),
                                cant = formu.cleaned_data.get('cantidad'),
                                tipo = 'SA'
                            )
                            mv.save()

                            r_m = RecM(
                                ent = en,
                                env_id = EnvM.objects.get(mat = env_m.mat, ent = env_m.ent).id,
                                recp = False,
                            )
                            r_m.save()
                            return redirect('home')
        else:
            return render(self.template_name,{'formu':formu})
    
class StockPListView(ListView):
    model = StockProd
    template_name = "stock/l_prod.html"

class StockMListView(ListView):
    model = StockMat
    template_name = 'stock/l_mat.html'

class TabSP(TemplateView):
    template_name = 'stock/tab_s_prod.html'

class TabSM(TemplateView):
    template_name = 'stock/tab_s_mat.html'

class RecPListView(ListView):
    model = RecP
    template_name = 'stock/l_env_prod.html'

class RecPUpdateView(UpdateView):
    model = RecP
    fields = ['recp']
    template_name = 'stock/update_p.html'
    success_url = reverse_lazy('home')