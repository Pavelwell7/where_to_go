from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ['preview']
    exclude = ['order']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px;">', obj.image.url)
        return '-'

    preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 200px;">', obj.image.url)
        return '-'

    preview.short_description = 'Превью'
