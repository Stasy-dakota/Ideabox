from masks import get_mask_account, get_mask_card_number
from widget import get_date, mask_account_card
from processing import filter_by_state
from processing import sort_by_date


print(get_mask_account(1234567890123456))
print(get_mask_card_number(23654890436512183622))


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счёт 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))


base_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]
print(filter_by_state(base_list))
print(sort_by_date(base_list))
