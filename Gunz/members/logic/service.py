from members.logic.selectors import get_characters_for_account


def max_out_account(*, account_id: int, target_level: int):
    for char in get_characters_for_account(id=account_id):
        char.level = target_level
        char.bp    = 133337
        char.save()

