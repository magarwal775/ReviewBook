from django.contrib import admin
from games.models import Game, GameReview

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'releasedate', 'size', 'publication',)
    search_fields = ('name', 'publication',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Game, GameAdmin)
admin.site.register(GameReview)
