from smartphone import Smartphone

catalog = [
    Smartphone("Huawei", "P20 Lite", "+79779779777"),
    Smartphone("Honor", "X9b", "+79669666666"),
    Smartphone("Apple", "iPhone 10", "+79889889888"),
    Smartphone("Xiaomi", "Mi 11", "+79559559555"),
    Smartphone("Poco", "M6 Pro", "+79119119111")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
