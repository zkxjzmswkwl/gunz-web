from django.contrib import admin
from .models import Account, Character, Characteritem, Charactermakinglog, Friend, Login, Gamerooms

class CharacterAdmin(admin.ModelAdmin):
    search_fields = ["name", "aid", "bp", "xp"]

class FriendAdmin(admin.ModelAdmin):
    search_fields = ["cid", "friendcid"]

class AccountAdmin(admin.ModelAdmin):
    search_fields = ["userid", "ugradeid", "email", "regdate"]


class GameroomsAdmin(admin.ModelAdmin):
    search_fields = ["title",]

admin.site.register(Account, AccountAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Gamerooms, GameroomsAdmin)
admin.site.register(Characteritem)
admin.site.register(Charactermakinglog)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Login)
