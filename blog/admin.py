from django.contrib import admin
from .models import accident
from .models import acmodels
<<<<<<< HEAD
=======
from .models import terms
>>>>>>> b62a42baaa96e7f09ee92cbe27dc5d71a0eda923

# decorator
@admin.register(accident)
class accident_Admin(admin.ModelAdmin):
    list_display = ('title','date','content','acmodels')
    list_filter = ('date','acmodels')
    search_fields = ('title','content')
    date_hierarchy = 'date'
    ordering = ('date','acmodels')

admin.site.register(acmodels)

<<<<<<< HEAD
=======
@admin.register(terms)
class terms_Admin(admin.ModelAdmin):
    list_display = ('title', 'content', 'acmodels', 'tags')
    list_filter = ('title',)
    search_fields = ('title',)
>>>>>>> b62a42baaa96e7f09ee92cbe27dc5d71a0eda923
# Register your models here.
