from django.contrib import admin
from .models import *


class TalabaAdmin(admin.ModelAdmin):
    list_display = ['id', 'ism', 'kurs', 'guruh', 'kitob_soni']
    list_display_links = ['id', 'ism']
    list_filter = ['kurs', 'guruh']
    list_editable = ('guruh', 'kitob_soni')
    list_per_page = 10
    search_fields = ('ism', 'kurs')
    search_help_text = "Ism yoki kurs bo'yicha..."


class RecordAdmin(admin.ModelAdmin):
    list_display = ('Talaba', 'kitob', 'Kutubxonachi', 'olingan_sana', 'qaytarilgan_sana', 'qaytardi')
    list_editable = ('qaytardi',)
    date_hierarchy = 'qaytarilgan_sana'


class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1


class KitobAdmin(admin.ModelAdmin):
    list_display = ('nom', 'janr', 'sahifa', 'Muallif')


class MuallifAdmin(admin.ModelAdmin):
    inlines = [KitobInline]


admin.site.register(Talaba, TalabaAdmin)
admin.site.register(Kitob, KitobAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Kutubxonachi)
