from django.contrib import admin
from .models import article
from .models import accident
from .models import acmodels
from .models import comment
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

@admin.register(comment)
class comment_Admin(admin.ModelAdmin):
    list_display = ('post','name','body','created')
    list_filter = ('created',)
    search_fields = ('name','body')

@admin.register(article)
class article_Admin(admin.ModelAdmin):
    a = article()
    list_display = ('title','truncated_content')
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(terms)
class terms_Admin(admin.ModelAdmin):
    list_display = ('title','content', 'acmodels')
    list_filter = ('title',)
    search_fields = ('title',)
# Register your models here.
