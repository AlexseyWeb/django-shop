from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = "Панель Администрирования"
admin.site.site_title = "Курсы и API"
admin.site.index_title = "Добро пожаловать в маленький проект!"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = models.Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [(None, {'fields': ['title']}), ('Dates', {
        'fields': ['created_at'], 'classes': ['collapse']})]
    inlines = [CoursesInline]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
