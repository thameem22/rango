from django.contrib import admin

# Register your models here.
from rango.models import Category, Page
from rango.models import UserProfile

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)