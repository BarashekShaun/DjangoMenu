from django import template
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from main.models import SubMenu, SubMenuItems, Menu

register = template.Library()


@register.simple_tag
def draw_menu(page):
    try:
        menu = Menu.objects.all()
        context = {'menu': menu}
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return template.render(context=context)


@register.simple_tag
def draw_items(pk):
    submenu = get_object_or_404(SubMenu, pk=pk)
    items = SubMenuItems.objects.filter(submenu=pk)
    context = {'items': items, 'submenu': submenu}
    template = get_template('main/items.html')
    return template.render(context=context)
