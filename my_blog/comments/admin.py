# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from comments.models import Comments
from django.contrib import messages

def make_revert(modeladmin, request, queryset):
    for i in queryset:
        messages.add_message(
            request,
            messages.INFO if not i.is_publick else messages.ERROR,
            'On comments %s is_publick %s'%(i.id, not i.is_publick)
        )
        i.is_publick = not i.is_publick
        i.save()
make_revert.short_description = "Mark selected comments is_publick revert"

def make_publick(modeladmin, request, queryset):
    for i in queryset:
        messages.add_message(request, messages.INFO, 'On comments %s is_publick %s'%(i.id, not i.is_publick))
        i.is_publick = True
        i.save()
make_publick.short_description = "Mark selected comments is publick"

def make_unpublick(modeladmin, request, queryset):
    for i in queryset:
        messages.add_message(request, messages.ERROR, 'On comments %s is_publick %s'%(i.id, not i.is_publick))
        i.is_publick = False
        i.save()
make_unpublick.short_description = "Mark selected comments is unpublick "


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('get_article_title', 'is_publick', 'title', 'body' )
    actions = [make_revert, make_publick, make_unpublick]
    actions_on_bottom = True
    date_hierarchy = 'date_create'
    readonly_fields = ('date_create', 'author', 'article')
    # exclude = ('article', )
    fieldsets = (
                 ('Information', {
                     'classes': ('collapse', 'wide'),
                     'fields': ('author', 'article', 'date_create')
                 }),
                 (None, {'fields': ('title', 'body', 'is_publick')}),
                 )

    list_display_links = ('title','get_article_title')
    list_editable = ('is_publick',)
    list_filter = ('is_publick', 'author', 'article')
    list_per_page = 3
    list_max_show_all = 25
    list_select_related = ('author', 'article')
    def get_article_title(self, obj):
        return obj.article.title
    get_article_title.short_description="Article Title"
    get_article_title.admin_order_field='article__title'

admin.site.register(Comments, CommentsAdmin)
