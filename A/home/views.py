from django.shortcuts import render,redirect,get_object_or_404
from django.http import FileResponse
from django.views import View
from home.models import Companies,Company,CompanyAssembly,CompanyPeople
from reportlab.pdfgen import canvas
from io import BytesIO
from .pdf import create_pdf

# Create your views here.


class HomeView(View):
    def get(self,request):
        companies = Companies.objects.all()
        return render(request,'home/home.html',{'Companies':companies})
    
class CompanyView(View):
    def get(self,request,*args, **kwargs):
        company = Company.objects.filter(name=kwargs['comany_name'])
        return render(request,'home/company.html',{'Company':company})
    
class CompanyAssemblyView(View):
    def get(self, request, *args, **kwargs):
        company_name = kwargs['company_name']
        assembly = CompanyAssembly.objects.filter(company=company_name)
        return render(request, 'home/assembly.html', {'assembly': assembly})
    
class PeopleView(View):
    def get(self,request,*args, **kwargs):
        assembly_name = kwargs['assembly_name']
        peoples = CompanyPeople.objects.filter(company = assembly_name)
        print(peoples)
        return render(request, 'home/people.html', {'peoples': peoples})

class pdfView(View):
    def get(self,request,*args, **kwargs):
        people = get_object_or_404(CompanyPeople ,pk=kwargs['user_id'])
        response = FileResponse(create_pdf(people.name ,people.number), 
                            as_attachment=True, 
                            filename='Cart.pdf')
        return response