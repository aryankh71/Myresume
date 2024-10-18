from django.contrib import admin
from .models import *


# admin.site.register(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['author', 'gender', 'linkedin_url', 'phone']


@admin.register(ProfessionalSummary)
class ProfessionalSummary(admin.ModelAdmin):
    list_display = ['user', 'skills', 'languages', 'education']
# admin.site.register(ProfessionalSummary)

# admin.site.register(JobHistory)

@admin.register(JobHistory)
class JobHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'job_title', 'start_date', 'end_date', 'employment_type']
    search_fields = ['company_name']
    ordering = ['start_date', 'end_date']

admin.site.register(Education)


