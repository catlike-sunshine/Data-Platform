from django.contrib import admin
from .models import accident
from .models import acmodels

# decorator
@admin.register(accident)
class accident_Admin(admin.ModelAdmin):
    list_display = ('title','date','content','acmodels')
    list_filter = ('date','acmodels')
    search_fields = ('title','content')
    date_hierarchy = 'date'
    ordering = ('date','acmodels')

admin.site.register(acmodels)

# Register your models here.
