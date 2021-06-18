import re

file = open("./src/data_corey.txt",'r')
text = file.read()
number = re.findall(r"(\d{3}[- \s]\d{3}[- \s]\d{4}|\(\d{3}\)\s*\d{3}[- \s]\d{4}|\d{3}[- \s]\d{4})", text)
print(number)

print(f"Total amount of phone numbers: {len(number)}")

ending_number =  re.findall(r"^(\d{7})$", text)
print(f"Total amount of phone numbers with ending 7: {len(ending_number)}")


mail_adres = re.findall(r'\S+@\S+', text)
for i in mail_adres:
    print(i)