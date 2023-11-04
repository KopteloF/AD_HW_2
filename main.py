import re
import csv

from pprint import pprint
import pandas as pd

from data import patter_name as p_name, patter_phone as p_phone
from data import replace_name as r_name, replace_phone as r_phone

class Phonebook:
    def __init__(self, phone_list):
        self.phone_list = phone_list

    def text(self, text):

        result_name = re.sub(p_name, r_name, ','.join(text[:2])).replace(' ','').split(',')
        if len(result_name) >= 4:
            result_name.remove("")
        for i in range(len(result_name)):
            text[i] = result_name[i]
        result_phone = re.sub(p_phone, r_phone, text[5])
        text[5] = result_phone

        return text
    def list_handler(self):

        for i in range(1, len(self.phone_list)):
            pre_res = self.text(self.phone_list[i])
            self.phone_list[i] = pre_res
    def list_clean(self):
        self.list_handler()
        temp_d = self.phone_list
        for i in range(len(temp_d)-1, 0, -1):
            for j in range(i-1, 1, -1):
                if temp_d[i][0] == temp_d[j][0] and temp_d[i][1] == temp_d[j][1]:
                    for k in range(7):
                        if temp_d[j][k] == temp_d[i][k]:
                            continue
                        else:
                            temp_d[j][k] += temp_d[i][k]
                    temp_d.pop(i)
                    break

        return temp_d

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

if __name__ == '__main__':
    nalog = Phonebook(phone_list = contacts_list)

    nalog.list_clean()

    pprint(pd.DataFrame(nalog.phone_list))

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(nalog.phone_list)