from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from base.models import Account,Movie,Game,Director,Star,Publication,Genre,TvShow,Episode

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','date_joined','last_login','first_name','last_name','is_admin')
    search_fields = ('email','username','first_name','last_name',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Movie)
admin.site.register(Game)
admin.site.register(Director)
admin.site.register(Star)
admin.site.register(Publication)
admin.site.register(Genre)
admin.site.register(TvShow)
admin.site.register(Episode)
