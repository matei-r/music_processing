from django.contrib import admin
from .models import Project,Song

class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project,ProjectAdmin)

class SongAdmin(admin.ModelAdmin):
    pass
admin.site.register(Song,SongAdmin)