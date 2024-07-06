from masks import get_mask_account, get_mask_card_number
from widget import get_date, mask_account_card

print(get_mask_account(1234567890123456))
print(get_mask_card_number(23654890436512183622))


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счёт 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))