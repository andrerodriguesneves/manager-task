from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

#admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'solution', 'responsible', 'priority', 'finalized_in' )
    list_filter = ('responsible', 'priority')
    search_fields = ('title', 'responsible', 'priority')




