from django.contrib import admin
from .models import Clan, Clanmember

class ClanAdmin(admin.ModelAdmin):
    search_fields = ["name", "point"]

admin.site.register(Clan, ClanAdmin)
admin.site.register(Clanmember)
