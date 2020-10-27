from django.urls import path
from .views import IngStockPView, IngStockMView, TabEnv, REnvPView, REnvMView, RecPListView, StockPListView,TabSP, TabSM, StockMListView, RecPUpdateView


urlpatterns = [
    path('i_prod/',IngStockPView.as_view(), name = 'i_prod'),
    path('i_mat/',IngStockMView.as_view(), name = 'i_mat'),
    path('t_env/',TabEnv.as_view(), name = 't_env'),
    path('r_env_prod/',REnvPView.as_view(), name = 'r_env_prod'),
    path('r_env_mat/',REnvMView.as_view(), name = 'r_env_mat'),
    path('l_env_p/',RecPListView.as_view(), name = 'l_env_p'),
    path('l_prod',StockPListView.as_view(), name= 'l_prod' ),
    path('tab_s_prod/',TabSP.as_view(), name = 'tab_s_prod'),
    path('tab_s_mat/',TabSM.as_view(), name = 'tab_s_mat'),
    path('l_mat/',StockMListView.as_view(),name = 'l_mat'),
    path('up_prod/<int:pk>/',RecPUpdateView.as_view(), name = 'up_prod')
]
