from django.contrib import admin
from movies.models import Movie, MovieReview

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'releasedate', 'runningtime', 'avgreview', 'director', 'publication',)
    search_fields = ('name', 'director', 'publication',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieReview)
