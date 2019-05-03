from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='event_index'),
    path('<int:event_id>/', views.detail, name='event_detail'),
    path('<int:event_id>/daftar', views.daftar, name='event_daftar'),
    path('<int:event_id>/paket/<int:paket_id>/<bidang>', views.detail_paket, name='event_detail_paket'),
]
