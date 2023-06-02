# this file was used to clean the data from txt then store it csv, the file is not used by the programm any more!!

import csv
import random

def pull_data_into_lst(file):
    lst_of_lines = []
    for line in file:
        lst_of_lines.append(line.strip())

    return lst_of_lines

def get_lst_of_major_2nd_word(lst):
    lst_of_11_len_words = []
    for line in lst:
        words = line.split()
        if len(words) == 11:
            lst_of_11_len_words.append(words)

    tmp_lst = [x[5] for x in lst_of_11_len_words]
    tmp_lst = set(tmp_lst)
    tmp_lst.remove('New')
    return tmp_lst

def generate_unique_numbers():
    numbers = set()

    while len(numbers) < 1000:
        number = random.randint(10**11, (10**12)-1)
        numbers.add(number)

    return list(numbers)

with open('project/data/fake-student.csv','w') as fh:
    writer = csv.writer(fh)
    students_data = []

    # get data and store it in a list
    with open('project/data before cleaning/students-fake-data.txt') as file:

        file_data = pull_data_into_lst(file)
        fillter_major = get_lst_of_major_2nd_word(file_data)

        x = 0
        for line in file_data:
            words = line.strip().split()
            
            if len(words) == 12:
                name = words[2] + ' ' + words[3]
                major = words[4] + ' ' + words[5]
                country = words[6] +  ' ' + words[7]
                gpa = words[9]
                gender = words[10]

            if len(words) == 11:
                if words[5] in fillter_major:
                    name = words[2] + ' ' + words[3]
                    major = words[4] + ' ' + words[5]
                    country = words[6] 
                    gpa = words[8]
                    gender = words[9]
                else:
                    name = words[2] + ' ' + words[3]
                    major = words[4]
                    country = words[5] + ' ' + words[6]
                    gpa = words[8]
                    gender = words[9]  

            if len(words) == 10:
                name = words[2] + ' ' + words[3]
                major = words[4]
                country = words[5]
                gpa = words[7]
                gender = words[8]

            list_of_codes = generate_unique_numbers()
            students_data.append({'name':name,'major':major,'country':country,'gpa':gpa,'gender':gender,'code':list_of_codes[x]})

        
    writer.writerow(['name','major','country','gpa','gender','code'])
    for student in students_data:
        writer.writerow([student['name'],student['major'],student['country'],student['gpa'],student['gender'],student['code']])
