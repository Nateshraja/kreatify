from django.contrib import admin
from .models import Proposal
import csv
from django.http import HttpResponse

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'submitted_at')
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=proposals.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"