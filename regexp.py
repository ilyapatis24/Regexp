import csv,re

PATTERN_TEL = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
TEL_SUB = r'+7(\2)-\3-\4-\5 \6\7'

def basic(contacts_list):
    new_contacts = []
    for item in contacts_list:
        contact_fullname = ' '.join(item[:3]).split(' ')
        cont_result = [contact_fullname[0], contact_fullname[1], contact_fullname[2], item[3], item[4],
                    re.sub(PATTERN_TEL, TEL_SUB, item[5]),
                    item[6]]
        new_contacts.append(cont_result)
    return contacts_filter(new_contacts)

def contacts_filter(new_contacts):
    for contact in new_contacts:
        last_name = contact[0]
        first_name = contact[1]
        for new_contact in new_contacts:
                new_last_name = new_contact[0]
                new_first_name = new_contact[1]
                if first_name == new_first_name and last_name == new_last_name:
                    if contact[2] == "": contact[2] = new_contact[2]
                    if contact[3] == "": contact[3] = new_contact[3]
                    if contact[4] == "": contact[4] = new_contact[4]
                    if contact[5] == "": contact[5] = new_contact[5]
                    if contact[6] == "": contact[6] = new_contact[6]
    result_list = list()
    for i in new_contacts:
        if i not in result_list:
            result_list.append(i)
    return result_list

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        print(basic(contacts_list))

