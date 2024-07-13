from typing import Any


def filter_by_state(base_list: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция, сортирующая список по указанному ключу"""
    new_list = []
    for key in base_list:
        if key.get("state") == state_id:
            new_list.append(key)
    return new_list


def sort_by_date(base_list: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки исходных данных по дате"""
    sorted_base_list = sorted(base_list, key=lambda base_list: base_list["date"], reverse=reverse)
    return sorted_base_list
