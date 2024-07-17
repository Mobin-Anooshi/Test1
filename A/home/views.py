from django.shortcuts import render,redirect,get_object_or_404
from django.http import FileResponse
from django.views import View
from home.models import Companies,Company,CompanyAssembly,CompanyPeople
from reportlab.pdfgen import canvas
from io import BytesIO
from .pdf import create_pdf
from home.forms import CompanyForm,AddCompanyForm,AddCompanyAssmblyForm

# Create your views here.


class HomeView(View):
    def get(self,request):
        companies = Companies.objects.all()
        return render(request,'home/home.html',{'Companies':companies})
class CompaniesFormView(View):
    def get(self,request):
        form = CompanyForm()
        return render(request ,'home/add_companies.html',{'form':form})
    def post(self,request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Companies.objects.create(name=cd['name'])
            return redirect('home:home')
        return render(request ,'home/add_companies.html',{'form':form})
class CompanyView(View):
    def get(self,request,*args, **kwargs):
        company_name = kwargs['comany_name']
        company = Company.objects.filter(name=company_name)
        return render(request,'home/company.html',{'Company':company,'company_name':company_name})
class AddCompanyView(View):
    def get(self,request,*args, **kwargs):
        form = AddCompanyForm
        return render(request ,'home/add_company.html',{'form':form})
    def post(self,request,*args, **kwargs):
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            company_name = get_object_or_404(Companies,pk=kwargs['company_name'])
            Company.objects.create(name=company_name,company_name=cd['company_name'],number=cd['number'])
            return redirect('home:company',company_name.id)
        return render(request ,'home/add_company.html',{'form':form})
        
class CompanyAssemblyView(View):
    def get(self, request, *args, **kwargs):
        company_name = kwargs['company_name']
        assembly = CompanyAssembly.objects.filter(company=company_name)
        return render(request, 'home/assembly.html', {'assembly': assembly,'company_name':company_name})
class AddCompanyAssemblyView(View):
    def get(self,request,*args, **kwargs):
        form = AddCompanyAssmblyForm()
        return render(request , 'home/add_assembly.html',{'form':form})
    def post(self,request,*args, **kwargs):
        form = AddCompanyAssmblyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            company_name = get_object_or_404(Company,pk=kwargs['company_name'])
            CompanyAssembly.objects.create(company=company_name,name=cd['name'])
            return redirect('home:assembly',company_name.id)
        return render(request, 'home/add_assembly.html',{'form':form})
    
        
    
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