from django.contrib import admin
from series.models import TvShow, Episode

class TvShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'releasedate', 'runningtime', 'avgreview', 'publication',)
    search_fields = ('name', 'publication',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'episodename', 'episodenumber', 'releasedate', 'runningtime', 'avgreview',)
    search_fields = ('show_name', 'episodename', 'publication',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(TvShow, TvShowAdmin)
admin.site.register(Episode, EpisodeAdmin)
