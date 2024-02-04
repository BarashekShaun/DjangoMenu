from django.contrib import admin
from .forms import MenuForm, SubMenuForm, SubMenuItemsForm
from .models import Menu, SubMenu, SubMenuItems


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm


admin.site.register(Menu, MenuAdmin)


class SubMenuAdmin(admin.ModelAdmin):
    form = SubMenuForm
    list_display = ('menu', 'name', )


admin.site.register(SubMenu, SubMenuAdmin)


class ItemsAdmin(admin.ModelAdmin):
    form = SubMenuItemsForm


admin.site.register(SubMenuItems, ItemsAdmin)
