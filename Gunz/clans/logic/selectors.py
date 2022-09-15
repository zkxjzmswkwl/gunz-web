from clans.models import Clan, Clanmember
from typing import List

def get_clan_by(*, id: int) -> Clan:
    return Clan.objects.get(clid=id)

def list_clans_by_wins() -> List[Clan]:
    return Clan.objects.all().order_by("-wins")

def list_clans_by_points() -> List[Clan]:
    return Clan.objects.all().order_by("-point")

def list_clans_by_total_points() -> List[Clan]:
    return Clan.objects.all().order_by("-totalpoint")

def get_members_for(*, clan_id: int) -> List[Clanmember]:
    return Clanmember.objects.filter(clid=clan_id)


