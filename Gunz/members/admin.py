from django.contrib import admin
from .models import Account, Character, Characteritem, Charactermakinglog, Friend, Login

class CharacterAdmin(admin.ModelAdmin):
    search_fields = ["name", "aid", "bp", "xp"]

class FriendAdmin(admin.ModelAdmin):
    search_fields = ["cid", "friendcid"]

class AccountAdmin(admin.ModelAdmin):
    search_fields = ["userid", "ugradeid", "email", "regdate"]

admin.site.register(Account, AccountAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Characteritem)
admin.site.register(Charactermakinglog)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Login)
