from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    
pattern_phone = r"(\+7|8)?\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d+)\s*\(*(доб.)*\s*(\d+)*\)*"
pattern_phone_fix = r"+7(\2)\3-\4-\5 \6\7"
for i in contacts_list[1::]:
    result = re.sub(pattern_phone, pattern_phone_fix, i[5])
    i[5] = result
    name =  i[0].split(' ')
    if len(name) == 2:
        i[0] = name[0]
        i[1] = name[1]
    elif len(name) == 3:
        i[0] = name[0]
        i[1] = name[1]
        i[2] = name[2]
    for n in contacts_list:
        if n[0] == i[0] and n[1] == n[1] and i != n:
            for m in n:
                if len(m) != 0:
                    i[n.index(m)] = m
            del contacts_list[contacts_list.index(n)]
pprint(contacts_list)
        
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

