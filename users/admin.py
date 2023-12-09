from django.contrib import admin

from users.models import CustomUser, Grade, Field, City, Student


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone',)
    list_filter = ('app_type', 'version')
    search_fields = ('phone__startswith',)
    fields = ('phone', 'is_visible', 'is_active', 'is_staff', 'date_joint', 'app_type', 'version')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title__startswith',)
    fields = ('title',)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title__startswith',)
    fields = ('title',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title__startswith',)
    fields = ('title',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'grade', 'field')
    list_filter = ('grade', 'field', 'city')
    search_fields = ('user__phone__startswith', 'first_name__startswith', 'last_name__startswith')
    fields = ('user', 'first_name', 'last_name', 'student_code', 'grade', 'field', 'city')
