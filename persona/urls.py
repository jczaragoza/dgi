from django.conf.urls import include
from django.urls import path

# PARA MEDIA
from django.conf.urls.static import static
from django.conf import settings

from persona import report, dash

from . import views

urlpatterns = [
    
    path('', views.PersonaList.as_view(), name='index'),
    path('persona/new/', views.PersonaCreate.as_view(), name='persona_new'),
    path('detail/<int:pk>/', views.PersonaDetailView.as_view(), name='persona_detail'),
    path('update/<int:pk>/', views.PersonaUpdateView.as_view(), name='persona_update'),
    path('delete/<int:pk>/', views.PersonaDeleteView.as_view(), name='persona_delete'),
    path('search/', views.PersonaSearchView, name='persona_search'),
    path('report/<int:pk>/', report.ReportView.as_view(), name='report'),
    #path('conteo/', views.conteo_list, name='conteo'),

    #REPORTS
    path('personal/uiip/', views.UiipView.as_view(), name='uiip'),
    path('personal/c5/', views.c5View.as_view(), name='c5'),
    path('personal/uac/', views.uacView.as_view(), name='uac'),
    
        # Management
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path('chaining/', include('smart_selects.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)