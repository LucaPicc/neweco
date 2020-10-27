from django.urls import path
from .views import ProdMatView, CargaProdView, CargaMatView, CargaLocalView, CompRecView



urlpatterns = [
    path('c_prod/', CargaProdView.as_view(),name = 'c_prod'),
    path('c_mat/', CargaMatView.as_view(), name = 'c_mat'),
    path('prod_mat/<int:i>/<int:pid>/', ProdMatView.as_view(), name = 'prod_mat'),
    path('c_local/',CargaLocalView.as_view(),name = 'c_local'),
    path('prod_rec/<int:cp>/<int:cr>/<int:li>/',CompRecView.as_view(),name = 'prod_rec'),
]
