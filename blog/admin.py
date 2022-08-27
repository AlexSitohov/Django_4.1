from django.contrib.admin import *

from .models import *


@register(Note)
class NoteModelAdmin(ModelAdmin):
    list_display = ('title_of_note', 'create_date', 'category')
    list_display_links = ('title_of_note',)
    prepopulated_fields = {
         'slug': ('title_of_note',)
    }
    # list_editable = ('title_of_note',)
    # list_per_page = 1



@register(Category)
class CategoryModelAdmin(ModelAdmin):
    prepopulated_fields = {
        'slug': ('name_of_category',)
    }
