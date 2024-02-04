from django.db import models


class Menu(models.Model):
    menu = models.CharField(max_length=30, unique=True,
                            verbose_name='Меню')
    order = models.SmallIntegerField(default=0, db_index=True,
                                     verbose_name='порядок')

    def __str__(self):
        return self.menu

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['order']


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,
                             verbose_name='Меню')
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Название', db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'
        ordering = ['name']


class SubMenuItems(models.Model):
    submenu = models.ForeignKey(SubMenu, on_delete=models.CASCADE,
                                verbose_name='Подменю')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вложения'
        verbose_name_plural = 'Вложения'
        ordering = ['-created_at']
