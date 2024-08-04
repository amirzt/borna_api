from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin

from users.models import CustomUser, Grade, Field, City, Student, Banner, TutorialVideo, AdvisorRequest, University, \
    OTP, Wallet, Advisor, Comment, PartnerShip
# from import_export import resources
from django.contrib.auth.models import Group


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
    fields = ('title', 'code', 'max_time', 'end_week_max_time', 'max_question', 'max_test', 'test_score')


#
# @admin.register(Field)
# class FieldAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     search_fields = ('title__startswith',)
#     fields = ('title',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title__startswith',)
    fields = ('title',)


# class StudentResource(resources.ModelResource):
#     class Meta:
#         model = Student
#         fields = ['user__phone', 'first_name', 'last_name', 'student_code', 'grade__title', 'city__title',
#                   'invitation_code', 'expire_date']
#
#
# class StudentAdmin(ImportExportModelAdmin):
#     resource_classes = [StudentResource]
#
#     list_display = ('user', 'first_name', 'last_name', 'grade')
#     list_filter = ('grade', 'city')
#     search_fields = ('user__phone__startswith', 'first_name__startswith', 'last_name__startswith')
#     fields = ('user', 'first_name', 'last_name', 'student_code', 'grade', 'city', 'invitation_code', 'expire_date')


# admin.site.register(Student, StudentAdmin)

admin.site.register(Banner)


# @admin.register(Banner)
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ('image', 'url', 'is_active',)
#     # search_fields = ('title__startswith',)
#     fields = ('image', 'url', 'is_active',)


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


# admin.site.register(OTP)
admin.site.register(Wallet)

admin.site.unregister(Group)


# admin.site.unregister(Token)


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    # list_filter = ('app_type', 'version')
    search_fields = ('name__startswith',)
    fields = (
    'user', 'name', 'capacity', 'field', 'history', 'pros', 'bio', 'experience', 'skills', 'voice', 'is_active')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('advisor',)
    # list_filter = ('app_type', 'version')
    # search_fields = ('name__startswith',)
    fields = ('advisor', 'content', 'file')


@admin.register(PartnerShip)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('advisor', 'student', 'start_date', 'end_date')
    # list_filter = ('app_type', 'version')
    # search_fields = ('name__startswith',)
    fields = ('advisor', 'student', 'start_date', 'end_date')
