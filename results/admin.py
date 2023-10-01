from django.contrib import admin

from .models import Results

@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ("sport","date_1")
