from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .forms import GsimpleForm, GIRSUForm, GrafAñoForm
from .models import Empleos, GGirsu,Recuperacion,GIRSU
from user.models import UserCustom

# Create your views here.

class GSimpleView(FormView):
    template_name = 'girsu/cargar_entidad.html'
    form_class = GsimpleForm
    

    def post(self,request, *args, **kwargs):
        formu = self.form_class(request.POST)
        userlog = UserCustom.objects.get(id = request.user.id)
        if formu.is_valid():
            emp = Empleos(
                entidad_id = userlog.entity_id,
                recolecccion = formu.cleaned_data.get('em_reco'),
                clas = formu.cleaned_data.get('em_clas'),
                educ = formu.cleaned_data.get('em_educ'),
                disp = formu.cleaned_data.get('em_disp'),
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'),
            )
            recu = Recuperacion(
                entidad_id = userlog.entity_id,
                recol = formu.cleaned_data.get('g_recol'),
                clasf = formu.cleaned_data.get('g_clasf'),
                edu = formu.cleaned_data.get('g_edu'),
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'),
            )
            g_r = recu.recol + recu.clasf + recu.edu
            ggirsu = GGirsu(
                entidad_id = userlog.entity_id,                
                recoleccion = formu.cleaned_data.get('g_recol'),
                gest_reci = g_r,
                disp_trat = formu.cleaned_data.get('g_disp_trat'),
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'), 
                )
            girsu = GIRSU(
                entidad_id = userlog.entity_id ,
                recup = formu.cleaned_data.get('reciclables'),
                empleos = emp.clas + emp.educ + emp.disp ,
                g_rec = recu.recol + recu.clasf + recu.edu,
                g_girsu = ggirsu.recoleccion + ggirsu.gest_reci + ggirsu.disp_trat,
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'),
                )
            emp.save()
            recu.save()
            ggirsu.save()
            girsu.save()
            return redirect('home')
        else:
            return render(request,self.template_name,{'formu':formu} )

class GIRSUView(FormView):
    template_name = 'girsu/cargar_entidad.html'
    form_class = GIRSUForm
    

    def post(self,request, *args, **kwargs):
        formu = self.form_class(request.POST)
        userlog = UserCustom.objects.get(id = request.user.id)
        if formu.is_valid():
            emp = Empleos(
                entidad_id = formu.cleaned_data.get('entidad').id,
                recolecccion = formu.cleaned_data.get('em_reco'),
                clas = formu.cleaned_data.get('em_clas'),
                educ = formu.cleaned_data.get('em_educ'),
                disp = formu.cleaned_data.get('em_disp'),
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'),
            )
            recu = Recuperacion(
                entidad_id = formu.cleaned_data.get('entidad').id,
                recol = formu.cleaned_data.get('g_recol'),
                clasf = formu.cleaned_data.get('g_clasf'),
                edu = formu.cleaned_data.get('g_edu'),
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'),
            )
            g_r = recu.recol + recu.clasf + recu.edu
            ggirsu = GGirsu(
                entidad_id = formu.cleaned_data.get('entidad').id,                
                recoleccion = formu.cleaned_data.get('g_recol'),
                gest_reci = g_r,
                disp_trat = formu.cleaned_data.get('g_disp_trat'),
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'), 
                )
            girsu = GIRSU(
                entidad_id = formu.cleaned_data.get('entidad').id,
                recup = formu.cleaned_data.get('reciclables'),
                empleos = emp.clas + emp.educ + emp.disp,
                g_rec = recu.recol + recu.clasf + recu.edu,
                g_girsu = ggirsu.recoleccion + ggirsu.gest_reci + ggirsu.disp_trat,
                f_mes= formu.cleaned_data.get('f_mes'),
                f_año= formu.cleaned_data.get('f_año'),
                )
            emp.save()
            recu.save()
            ggirsu.save()
            girsu.save()
            return redirect('c_s_girsu')
        else:
            return render(request,self.template_name,{'formu':formu})

class EnAño(FormView):
    template_name = 'girsu/stat_form.html'
    form_class= GrafAñoForm

    def post(self,request,e,*args, **kwargs):
        formu = self.form_class(request.POST)
        labels = []
        if formu.is_valid():
            en = formu.cleaned_data.get('entidad')
            an = formu.cleaned_data.get('año')
            if e == 1:
                data_reco = [] 
                prom_reco = 0
                data_clas = []
                prom_clas = 0
                data_educ = []
                prom_educ = 0
                data_disp = []
                prom_disp = 0
                prom = []
                promt=0
                queryset2 = Empleos.objects.all().filter(entidad= en, f_año = an)
                #queryset3 = GGirsu.objects.all().filter(entidad= en, f_año = an).order_by('f_mes')
                #queryset4 = Recuperacion.objects.all().filter(entidad= en, f_año = an).order_by('f_mes')

                for a in queryset2:
                    labels.append(a.f_mes)
                    data_reco.append(a.recolecccion)
                    prom_reco = prom_reco +a.recolecccion 
                    data_clas.append(a.clas)
                    prom_clas = prom_clas + a.clas
                    data_educ.append(a.educ)
                    prom_educ = prom_educ + a.educ
                    data_disp.append(a.disp)
                    prom_disp = prom_disp +  a.disp

                prom_clas=prom_clas/len(labels)
                prom_reco=prom_reco/len(labels)
                prom_educ=prom_educ/len(labels)
                prom_disp=prom_disp/len(labels)
                promt = (prom_reco + prom_disp + prom_educ + prom_clas)
                prom_reco = round((prom_reco/promt)*100,2) 
                prom_clas = round((prom_clas/promt)*100,2)
                prom_educ = round((prom_educ/promt)*100,2)
                prom_disp = round((prom_disp/promt)*100,2)
                prom.append(prom_clas)
                prom.append(prom_educ)
                prom.append(prom_reco)
                prom.append(prom_disp)
                return render(request,'girsu/empleos_stats_anual.html',{
                    'en':en,
                    'an':an,
                    'labels':labels,
                    'data_reco':data_reco, 
                    'data_clas':data_clas,
                    'data_educ':data_educ,
                    'data_disp':data_disp,
                    'prom':prom,
                })
            if e == 2:
                data_reco = {}
                data_clas = {} 
                data_educ = {}
                data_disp = {}
                prom_clas = []
                prom_disp = []
                prom_educ = []
                prom_reco = []
                prom = {}
                labels = []
                en = formu.cleaned_data.get('entidad')

                queryset = Empleos.objects.all().filter(entidad = en)
                
                ##Empleos en clasificación
                for a in queryset:
                    if a.f_año not in data_clas.keys():
                        data_clas[a.f_año]=[a.clas]
                    else:
                        data_clas[a.f_año].append(a.clas)
                for i in data_clas.keys():
                    prom_clas.append(round(sum(data_clas[i])/len(data_clas[i]),2))
                
                ##Empleos en disposición
                for a in queryset:
                    if a.f_año not in data_disp.keys():
                        data_disp[a.f_año]=[a.disp]
                    else:
                        data_disp[a.f_año].append(a.disp)
                for i in data_disp.keys():
                    prom_disp.append(round(sum(data_disp[i])/len(data_disp[i]),2))
                
                ##Empleos en educación
                for a in queryset:
                    if a.f_año not in data_educ.keys():
                        data_educ[a.f_año]=[a.educ]
                    else:
                        data_educ[a.f_año].append(a.educ)
                for i in data_educ.keys():
                    prom_educ.append(round(sum(data_educ[i])/len(data_educ[i]),2))

                ##Empleos en recolección
                for a in queryset:
                    if a.f_año not in data_reco.keys():
                        data_reco[a.f_año]=[a.recolecccion]
                    else:
                        data_reco[a.f_año].append(a.recolecccion)
                for i in data_reco.keys():
                    prom_reco.append(round(sum(data_reco[i])/len(data_reco[i]),2))
                
                j = 0

                for i in data_clas.keys():
                   if j < len(prom_clas):
                        if i not in prom.keys():
                            prom[i] = [prom_clas[j],prom_disp[j],prom_educ[j],prom_educ[j]]
                        else:
                            prom[i].append(prom_clas[j],prom_disp[j],prom_educ[j],prom_educ[j])
                        j+=1

                labels = list(data_clas.keys())
                return render(request, 'girsu/empleos_stats_por_año.html',{
                    'prom_clas':prom_clas,
                    'prom_disp':prom_disp,
                    'prom_educ':prom_educ,
                    'prom_reco':prom_reco,
                    'prom':prom,
                    'labels':labels,
                })
            if e == 3:
                queryset = GGirsu.objects.all().filter(f_año=an,entidad=en)
                
                labels = []
                data_greco = []
                data_greci = []
                data_gtrat = []
                gp_reco = 0
                gp_reci = 0
                gp_trat = 0
                s_reci = 0
                s_reco = 0
                s_trat = 0
                gp = []
            
                for a in queryset:
                    labels.append(a.f_mes)
                    data_greci.append(round(a.gest_reci))
                    data_greco.append(round(a.recoleccion))
                    data_gtrat.append(round(a.disp_trat))
                
                s_reci = sum(data_greci)
                s_reco = sum(data_greco)
                s_trat = sum(data_gtrat)

                gp_reci = round((s_reci/(s_reci+s_reco+s_trat))*100,2)
                gp_reco = round((s_reco/(s_reci+s_reco+s_trat))*100,2)
                gp_trat = round((s_trat/(s_reci+s_reco+s_trat))*100,2)

                gp.append(gp_reci)
                gp.append(gp_reco)
                gp.append(gp_trat)
                return render(request,'girsu/girsu_stats_anual.html',{
                    'labels':labels,
                    'data_greci':data_greci,
                    'data_greco':data_greco,
                    'data_gtrat':data_gtrat,
                    'gp':gp,
                })
            if e == 4:

                queryset = GGirsu.objects.all().filter(entidad=en)

                data_greci = {}
                data_greco = {}
                data_gtrat = {}

                prom_reci = []
                prom_reco = []
                prom_trat = []

                prom = {}

                #Armado de diccionario para calculo de promedio anual
                for i in queryset:
                    if i.f_año not in data_greci.keys():
                        data_greci[i.f_año]=[i.gest_reci]
                    else:
                        data_greci[i.f_año].append(i.gest_reci)
                
                for i in queryset:
                    if i.f_año not in data_greco.keys():
                        data_greco[i.f_año]=[i.recoleccion]
                    else:
                        data_greco[i.f_año].append(i.recoleccion)
                
                for i in queryset:
                    if i.f_año not in data_gtrat.keys():
                        data_gtrat[i.f_año]=[i.disp_trat]
                    else:
                        data_gtrat[i.f_año].append(i.disp_trat)

                for i in data_greci.keys():
                    prom_reci.append(round(sum(data_greci[i])/len(data_greci[i])))

                for i in data_greci.keys():
                    prom_reco.append(round(sum(data_greco[i])/len(data_greco[i])))

                for i in data_greci.keys():
                    prom_trat.append(round(sum(data_gtrat[i])/len(data_gtrat[i])))

                j = 0

                for i in data_greci.keys():
                   if j < len(prom_reci):
                        if i not in prom.keys():
                            prom[i] = [prom_reci[j],prom_reco[j],prom_trat[j]]
                        else:
                            prom[i].append(prom_reci[j],prom_reco[j],prom_trat[j])
                        j+=1
                
                labels = list(prom.keys())
                
                return render(request,'girsu/girsu_stats_por_año.html',{
                    'prom_reci':prom_reci,
                    'prom_reco':prom_reco,
                    'prom_trat':prom_trat,
                    'prom':prom,
                    'labels':labels,
                })
            if e == 5:
                queryset = Recuperacion.objects.all().filter(entidad = en,f_año=an )
                
                data_clas = []
                data_educ = []
                data_reco = []

                labels = []
                prom_v = []

                prom_clas = 0
                prom_educ = 0
                prom_reco = 0
                prom = 0

                s_clas = 0
                s_educ = 0
                s_reco = 0


                for a in queryset:
                    labels.append(a.f_mes)
                    data_clas.append(round(a.clasf))
                    data_educ.append(round(a.edu))
                    data_reco.append(round(a.recol))

                s_clas = sum(data_clas)
                s_educ = sum(data_educ)
                s_reco = sum(data_reco)

                prom_clas = round((s_clas/(s_clas + s_educ + s_reco))*100,2)
                prom_educ = round((s_educ/(s_clas + s_educ + s_reco))*100,2)
                prom_reco = round((s_reco/(s_clas + s_educ + s_reco))*100,2)
                
                prom_v.append(prom_clas)
                prom_v.append(prom_educ)
                prom_v.append(prom_reco)

                return render(request,'girsu/recup_stats_anual.html',{
                    'data_clas':data_clas,
                    'data_educ':data_educ,
                    'data_reco':data_reco,
                    'prom_v':prom_v,
                    'labels':labels,
                })
            if e == 6:
                queryset = Recuperacion.objects.all().filter(entidad = en)

                data_clas = {}
                data_educ = {}
                data_reco = {}

                prom_clas = []
                prom_educ = []
                prom_reco = []

                prom = {}

                for i in queryset:
                    if i.f_año not in data_clas.keys():
                        data_clas[i.f_año]=[i.clasf]
                    else:
                        data_clas[i.f_año].append(i.clasf)

                for i in queryset:
                    if i.f_año not in data_educ.keys():
                        data_educ[i.f_año]=[i.edu]
                    else:
                        data_educ[i.f_año].append(i.edu)

                for i in queryset:
                    if i.f_año not in data_reco.keys():
                        data_reco[i.f_año]=[i.recol]
                    else:
                        data_reco[i.f_año].append(i.recol)
                
                for i in data_clas.keys():
                    prom_clas.append(round(sum(data_clas[i])/len(data_clas[i])))
                
                for i in data_educ.keys():
                    prom_educ.append(round(sum(data_educ[i])/len(data_educ[i])))
                
                for i in data_reco.keys():
                    prom_reco.append(round(sum(data_reco[i])/len(data_reco[i])))

                j = 0

                for i in data_clas.keys():
                   if j < len(prom_clas):
                        if i not in prom.keys():
                            prom[i] = [prom_clas[j],prom_educ[j],prom_reco[j]]
                        else:
                            prom[i].append(prom_clas[j],prom_educ[j],prom_reco[j])
                        j+=1
                
                labels = list(prom.keys())
                return render(request,'girsu/recup_stats_por_año.html',{
                    'prom_clas':prom_clas,
                    'prom_educ':prom_educ,
                    'prom_reco':prom_reco,
                    'prom':prom,
                    'labels':labels,
                })
        else:
            return redirect(request,self.template_name,{'formu':formu})


                

class TabStats(TemplateView):
    template_name = 'girsu/tab_stats.html'





