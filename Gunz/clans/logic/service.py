from clans.models import Clan

def reset_clan(*, clan_id: int):
    clan = Clan.objects.get(clid=clan_id)
    clan.wins        = 0
    clan.losses      = 0
    clan.totalpoint  = 0
    clan.point       = 0
    clan.ranking     = 0
    clan.level       = 0
    clan.exp         = 0
    print(f"Reset {clan.name}")
    clan.save()

def admin_abuse(*, clan_id: int):
    clan = Clan.objects.get(clid=clan_id)
    clan.wins       = 1337
    clan.totalpoint = 6969
    clan.point      = 6969
    clan.save()



