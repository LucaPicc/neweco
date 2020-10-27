from django.urls import path
from .views import GSimpleView, GIRSUView, EnAño, TabStats

urlpatterns = [
    path('c_girsu',GSimpleView.as_view(),name='c_girsu'),
    path('c_s_girsu',GIRSUView.as_view(),name ='c_s_girsu'),
    path('stat_form/<int:e>',EnAño.as_view(), name='stat_form'),
    path('tab_stats',TabStats.as_view(), name='tab_stats'),
]
