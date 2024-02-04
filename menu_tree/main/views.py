from django.shortcuts import render, get_object_or_404
from main.models import SubMenu, Menu, SubMenuItems


def index(request):
    return render(request, 'main/index.html')


def detail_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    submenu = SubMenu.objects.filter(menu=pk)
    context = {'menu': menu, 'submenu': submenu}

    return render(request, 'main/detail_menu.html', context)


def detail_submenu(request, menu_pk, pk):
    submenu = get_object_or_404(SubMenu, pk=pk)
    items = SubMenuItems.objects.filter(submenu=pk)
    context = {'items': items, 'submenu': submenu}
    return render(request, 'main/detail_submenu.html', context)
