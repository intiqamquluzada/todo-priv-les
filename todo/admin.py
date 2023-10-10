from django.contrib import admin
from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("name", "add_date", "update_date", "status")


admin.site.register(Todo, TodoAdmin)
