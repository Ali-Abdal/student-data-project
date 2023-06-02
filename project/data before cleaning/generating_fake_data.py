# used it to generate the fake data of 1000 student

import random


file_name = 'project/data/students-fake-data.txt'

names = ['Ali','Sara','Zainab','Fatima',"Mohammed",'Khalid','Mansour','Jassim','Abdullah','Jawan','Mariam',
'Hussain','Abdulaziz','Hassan','Asmaa','Wrood','Yousif','Ahmad','Noor',"Munir",'Hamad','Thamer','Haider',
'Salman','Mahdi','Omar','Habiba','Norah','Nancy','Hajer','Hind','Abdulmohsen','Moath','Aisha','Farah',
'Hashim','Rashid','Hamza']

female_names = ['Sara','Zainab',"Fatima",'Jawan','Mariam','Asmaa','Wrood','Noor','Habiba','Norah','Nancy'
,'Hajer','Hind','Aisha','Farah']

last_names = ['Abdal','Mousawi','Gambar','Azmi','Elenzi','Shimery','Refai','Jawahery','Fozan','Tuneb',
'Fadlhi','Al-Bannai','Ghanim','Mutairi','Bloushy','Bahbhani','Marafi','Hulail','Ajmi','Ramadan','Habib',
'Hashimy','Dashti']

contries = ["UK","USA","Irland","Australia",'France','UAE','Saudi','Bahrain','Canada','New Zealand']

majors = ['Medicine','Dentistry','Pharmacy','Civil Engineering','Chemical Engineering','Mechanical Engineering',
'Medical Engineering','Aerospace Engineering', 'Cyber Security','Computer Science','English','Data Science',
'Media','business','Marketing','French','Art', 'Graphical Designing','Robotics','Computer Engineering',
'Physics','Chemistry','Biology']


def generate_fake_gpa():
    
    random_float = round(random.uniform(80, 100), 2)
    return random_float

def generate_fake_gpa_med():

    random_float = round(random.uniform(95, 100), 2)
    return random_float

def generate_fake_msg_id():

    random_number = random.randint(10000000, 99999999)
    return random_number


# KCOK@kuwait.com accepted 'Student name' 'major' 'country' with 'gpa' 'gender' 'random hashtag'
with open(file_name,'a') as fh:
    
    for i in range(1000):

        student_name = random.choice(names) + " " + random.choice(last_names)
        major = random.choice(majors)
        country = random.choice(contries)
        gpa = generate_fake_gpa_med() if major in ['Medicine','Dentistry','Pharmacy'] else generate_fake_gpa()
        gender = 'Female' if (student_name.split())[0] in female_names else 'Male'
        random_hashtag = '#@' + str(generate_fake_msg_id())

        fh.write(f'KCOK@kuwait.com accepted {student_name} {major} {country} with {gpa} {gender} {random_hashtag}\n')