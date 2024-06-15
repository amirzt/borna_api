from django.contrib import admin

# Register your models here.
from league.models import LeagueItem, LeagueGroup, GroupMember

admin.site.register(LeagueItem)


@admin.register(LeagueGroup)
class LeagueGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_filter = ('app_type', 'version')
    search_fields = ('name__startswith',)
    fields = ('name', 'creator', 'is_public', 'image')


@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('student',)
    # list_filter = ('app_type', 'version')
    # search_fields = ('student__startswith',)
    fields = ('student', 'group',)
