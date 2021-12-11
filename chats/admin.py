from django.contrib import admin

from .models import Chat, Message


class ChatAdmin(admin.ModelAdmin):
    model = Chat
    list_display = ('id_from_user', 'id_to_user',)
    list_filter = ('id_from_user', 'id_to_user',)
    fieldsets = (
        (None, {'fields': ('id_from_user', 'id_to_user',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_from_user', 'id_to_user',)}
         ),
    )
    search_fields = ('id_from_user', 'id_to_user')
    ordering = ('id_from_user',)


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id_chat', 'id_user', 'datetime', 'content')
    list_filter = ('id_user',)
    fieldsets = (
        (None, {'fields': ('id_chat', 'id_user', 'datetime', 'content',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_chat', 'id_user', 'datetime', 'content',)}
         ),
    )
    search_fields = ('id_chat', 'id_user')
    ordering = ('id_chat', 'id_user')


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
