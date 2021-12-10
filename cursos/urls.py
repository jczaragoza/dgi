from django.urls import path
from . import views  

urlpatterns = [
    
    path('new/', views.CursoCreateView.as_view(), name='curso_new'),
    path('curso_list/',views.CursoListView.as_view(), name='curso_list'),
    path('curso_update/<int:pk>/', views.CursoUpdateView.as_view(), name='curso_update'),
    path('curso_delete/<int:pk>/', views.CursoDeleteView.as_view(), name='curso_delete'),
    path('showlist/', views.showlist, name='showlist'),
   
] 