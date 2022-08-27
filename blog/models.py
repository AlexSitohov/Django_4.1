import uuid

from django.db.models import (
    Model,
    PROTECT,
    CASCADE,
    CharField,
    TextField,
    IntegerField,
    SlugField,
    ForeignKey,
    BooleanField,
    PositiveSmallIntegerField, UUIDField,
    DateTimeField
)
from django.urls import reverse


class Category(Model):
    name_of_category = CharField('Название категории', max_length=100, db_index=True)
    slug = SlugField('URL', unique=True, null=True)

    def __str__(self):
        return self.name_of_category

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category',
                       kwargs={
                           'category_slug': self.slug
                       })


class Note(Model):
    title_of_note = CharField('Заголовок записи', max_length=100)
    text_of_note = TextField('Текст записи')
    create_date = DateTimeField('Дата создания', auto_now=True)
    slug = SlugField('URL', unique=True)
    category = ForeignKey(Category, on_delete=CASCADE, verbose_name='Категория', null=True)

    def __str__(self):
        return self.title_of_note

    class Meta:
        db_table = 'Note'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return reverse('note',
                       kwargs={
                           'note_slug': self.slug,
                           'category_slug': self.category.slug
                       })
