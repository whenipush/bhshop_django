from django.contrib import admin
from .models import Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo', 'availability',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('availability',)

admin.site.register(Store, StoreAdmin)