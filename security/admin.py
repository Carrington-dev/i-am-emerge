from django.contrib import admin
from security.models import Contact, Subscribe


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject',  'message', 'date_recieved', 'date_last_viewed')
    list_filter = ('full_name', 'email',)
    readonly_fields = ('message',)
    search_fields = ('full_name',)
    ordering = ('full_name',)
    list_per_page: int = 30


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_subscribed', 'date_recieved', 'date_last_viewed')
    list_filter = ('is_subscribed',)
    search_fields = ('email', )
    date_hierarchy = 'date_recieved'
    ordering = ('-pk',)
    list_per_page: int = 30
    actions = []