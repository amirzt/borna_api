from django.contrib import admin

from users.models import CustomUser, Grade, Field, City, Student, Banner, TutorialVideo, AdvisorRequest, University, \
    OTP, Wallet


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone',)
    list_filter = ('app_type', 'version')
    search_fields = ('phone__startswith',)
    fields = ('phone', 'is_visible', 'is_active', 'is_staff', 'app_type', 'version')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title__startswith',)
    fields = ('title', 'code', 'max_time', 'max_question', 'max_test', 'test_score')


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
    list_display = ('user', 'first_name', 'last_name', 'grade')
    list_filter = ('grade', 'city')
    search_fields = ('user__phone__startswith', 'first_name__startswith', 'last_name__startswith')
    fields = ('user', 'first_name', 'last_name', 'student_code', 'grade', 'city', 'invitation_code', 'expire_date')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image', 'url', 'is_active',)
    # search_fields = ('title__startswith',)
    fields = ('image', 'url', 'is_active',)


@admin.register(TutorialVideo)
class TutorialVideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title__startswith',)
    fields = ('title', 'file', 'description')


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name__startswith',)
    fields = ('name', 'logo', 'url')


@admin.register(AdvisorRequest)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'is_called', 'created_at')
    search_fields = ('name__startswith',)
    list_filter = ('is_called',)
    fields = ('student', 'name', 'phone', 'is_called', 'grade')


admin.site.register(OTP)
admin.site.register(Wallet)