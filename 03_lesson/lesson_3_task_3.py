from address import Address
from mailing import Mailing


to_addr = Address("101000", "Москва", "Тверская", "15", "42")
from_addr = Address("190000", "Санкт-Петербург", "Невский", "25", "7")


mailing = Mailing(to_addr, from_addr, 350.50, "TRACK123456789")


print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)