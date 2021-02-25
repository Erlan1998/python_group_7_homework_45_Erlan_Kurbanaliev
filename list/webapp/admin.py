from django.contrib import admin
from webapp.models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'updated_at']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['id', 'description', 'status', 'updated_at']
    readonly_fields = ['updated_at', 'id']


admin.site.register(List, ListAdmin)
