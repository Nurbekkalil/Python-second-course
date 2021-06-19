import re

file = open("./src/data_phone.json", 'r')
text = file.read()
file.close()
# print(text)


phone_number = r'\+[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
found = re.findall(phone_number, text)
# print(found)
print(f"Total amount of phone numbers with 13 digits: {len(found)}")

phone_number1 = r"[(][0-6][0-9][0-9][)]\s\d{3}-\d{4}"
found1 = re.findall(phone_number1, text)
# print(found1)
print(f'Total amount of phone которые имеют формат (669) 106-9923: {len(found1)}')

