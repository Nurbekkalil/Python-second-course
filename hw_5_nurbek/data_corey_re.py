import re

file = open("./src/data_corey.txt",'r')
text = file.read()
file.close()
number = r"(\d{3}[-.]\d{3}[-.]\d{4})"
found = re.findall(number, text)
print(found)

print(f"Total amount of phone numbers: {len(found)}")

ending_number = r"(\d{3}[-.]\d{3}[-.]\d\d\d[7])"
found1 =  re.findall(ending_number, text)

print(f"Total amount of phone numbers with ending 7: {len(found1)}")

mail_adres = r'([a-zA-z]\D\S+@[a-zA-z]\D\S+\.(com|net))'
found2 = re.findall(mail_adres, text)
print(found2)