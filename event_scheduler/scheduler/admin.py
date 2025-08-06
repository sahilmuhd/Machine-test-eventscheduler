from django.contrib import admin
from .models import Speaker, Event, Session

admin.site.register(Speaker)
admin.site.register(Event)
admin.site.register(Session)
