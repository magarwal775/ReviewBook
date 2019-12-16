from django.contrib import admin
from series.models import Series, Episode, EpisodeReview

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'running_time', 'avg_review', 'publication',)
    search_fields = ('name', 'publication',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'episode_name', 'episode_number', 'release_date', 'running_time', 'avg_review',)
    search_fields = ('show_name', 'episode_name', 'publication',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Series, SeriesAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(EpisodeReview)
