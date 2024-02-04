from django import forms
from .models import Menu, SubMenu, SubMenuItems


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('menu',)


class SubMenuForm(forms.ModelForm):
    class Meta:
        model = SubMenu
        fields = '__all__'


class SubMenuItemsForm(forms.ModelForm):
    class Meta:
        model = SubMenuItems
        fields = '__all__'
