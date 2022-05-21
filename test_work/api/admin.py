from django.contrib import admin

from .models import Contact, Mailing, Message

admin.site.register(Contact)
admin.site.register(Mailing)
admin.site.register(Message)
