from rest_framework import serializers
from .models import Clan, Clanmember

from clans.logic.selectors import get_clan_by

from members.logic.selectors import get_character
from members.serializers import CharacterSerializer


class ClanSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Clan
        fields = "__all__"


class ClanMemberSerializer(serializers.ModelSerializer):
    character = serializers.SerializerMethodField()
    clan      = serializers.SerializerMethodField()

    class Meta:
        model  = Clanmember
        fields = [
            "cmid",  "clan", "character",
            "grade", "regdate", "contpoint"
        ]

    def get_character(self, obj):
        c = get_character(cid=obj.cid)
        return {
            "name":   c.name,
            "level":  c.level,
            "sex":    c.sex,
            "kills":  c.killcount,
            "deaths": c.deathcount
        }

    def get_clan(self, obj):
        c = get_clan_by(id=obj.clid)
        return {
            "name": c.name,
            "clid": c.clid
        }


