from django.contrib import admin

from .models import MenuCategory, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    fields = ["text", "url"]


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    ordering = ["id"]
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "url", "category"]
    ordering = ["id"]
    list_filter = ["category"]
