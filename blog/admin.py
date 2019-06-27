from django.contrib import admin
from .models import accident
from .models import acmodels
from .models import terms

# decorator
@admin.register(accident)
class accident_Admin(admin.ModelAdmin):
    list_display = ('title','date','content','acmodels')
    list_filter = ('date','acmodels')
    search_fields = ('title','content')
    date_hierarchy = 'date'
    ordering = ('date','acmodels')

admin.site.register(acmodels)

@admin.register(terms)
class terms_Admin(admin.ModelAdmin):
    list_display = ('title', 'content', 'acmodels', 'tags')
    list_filter = ('title',)
    search_fields = ('title',)
# Register your models here.
