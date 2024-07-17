from django import forms
from .models import Companies,Company,CompanyAssembly


class CompanyForm(forms.ModelForm):
    class Meta :
        model = Companies
        fields =('name',)

class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name','number')

class AddCompanyAssmblyForm(forms.ModelForm):
    class Meta :
        model = CompanyAssembly
        fields = ('name',)