from django.urls import path
from .views import HomeView, UserAdminECreateView,UserECreateView,AdminCreateView,EntidadCreateView, EntidadListView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('c_admin_en',UserAdminECreateView.as_view(),name='c_admin_en'),
    path('c_user_en',UserECreateView.as_view(),name='c_user_en'),
    path('c_admin',AdminCreateView.as_view(),name='c_admin'),
    path('c_en',EntidadCreateView.as_view(),name='c_en'),
    path('l_en',EntidadListView.as_view(),name='l_en'),
]

