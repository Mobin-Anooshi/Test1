from django.contrib import admin
from home.models import Companies,Company,CompanyAssembly,CompanyPeople

# Register your models here.

admin.site.register(Company)
admin.site.register(Companies)
admin.site.register(CompanyAssembly)
admin.site.register(CompanyPeople)
