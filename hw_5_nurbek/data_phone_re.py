import re

file = open("./src/data_phone.json", 'r')
text = file.read()
print(text)


cell_phones = re.findall(r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", text)
print(f'Total amount of phone numbers with 13 digits: {len(cell_phones)}')

cell_phones_2 = re.findall(r"(\d{3})(\d{3})(\d{4})", text)
print(cell_phones_2)