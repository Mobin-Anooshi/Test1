from django.urls import path
from home import views

app_name='home'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('company/<int:comany_name>',views.CompanyView.as_view(),name='company'),
    path('companyassembl/<int:company_name>/',views.CompanyAssemblyView.as_view(),name='assembly'),
    path('people/<int:assembly_name>/',views.PeopleView.as_view(),name='assembly_people'),
    path('pdf/<int:user_id>/',views.pdfView.as_view(),name='pdf')
]
