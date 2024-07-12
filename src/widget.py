from typing import Any

import masks


def mask_account_card(mask_card_and_account: Any) -> Any:
    """Функция маскировки банковской карты и банковского счёта"""
    if "Счёт" in mask_card_and_account:
        return masks.get_mask_account(mask_card_and_account)
    else:
        cards = masks.get_mask_card_number(mask_card_and_account[-16:])
        return cards


def get_date(date: str) -> str:
    """Функция трансформации даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
