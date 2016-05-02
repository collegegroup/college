from django.contrib import admin
from .models import CollegeCategory, State, CoachingCategory

# Register your models here.


class CollegeCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'lastupd_dttm')


class CoachingCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'lastupd_dttm')


class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'lastupd_dttm')


admin.site.register(CollegeCategory, CollegeCategoryAdmin)
admin.site.register(CoachingCategory, CollegeCategoryAdmin)
admin.site.register(State, StateAdmin)


