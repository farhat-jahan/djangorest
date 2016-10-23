from django.contrib import admin
from expense_tracker.models import UserDetail

# Register your models here.

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    pass
#admin.site.register(UserDetail, UserDetailAdmin)

# class UserDetailCountryDistributorAdmin(GmModelAdmin):
#     search_fields = ('distributor_id',)
#     list_display = ('distributor_id', 'get_user', 'get_profile_number', 'country')