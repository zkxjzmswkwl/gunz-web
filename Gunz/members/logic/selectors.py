from members.models import Account, Character, Gamerooms
from typing import List


def get_account(*, by_id: int) -> Account:
    return Account.objects.get(id=by_id)

def get_characters_for_account(*, id: int) -> List[Character]:
    return Character.objects.filter(aid=id)

def get_character(*, cid: int) -> Character:
    return Character.objects.get(cid=cid)

def list_characters_by_level() -> List[Character]:
    return Character.objects.all().order_by('-level')

def list_accounts() -> List[Account]:
    return Account.objects.all().order_by('aid')

def list_characters() -> List[Character]:
    return Character.objects.all().order_by('cid')

def list_stages() -> List[Gamerooms]:
    return Gamerooms.objects.all()
