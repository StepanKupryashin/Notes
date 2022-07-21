from django.contrib import admin
from .models import Users, Notes


@admin.register(Users)
class UseresAdmin(admin.ModelAdmin):
    list_display = ("name", "birthday", "status", "bio",)
    list_filter = ("birthday",)
    search_fields = ("bio",)


@admin.register(Notes)
class AdminNotes(admin.ModelAdmin):
    list_display = ("user", "date", "title",)
    
# Register your models here.
