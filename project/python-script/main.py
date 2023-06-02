from student import Student
from student_statistics import Statistics

# loads the data from the csv file and stores it in a list of Student objects
def load_data(file_path):
    try:
        with open(file_path,'r') as fh:
            students = []
            next(fh)
            for line in fh:
                student_data = line.split(',')
                name = student_data[0]
                major = student_data[1]
                country = student_data[2]
                gpa = student_data[3]
                gender = student_data[4]
                code = student_data[5].strip()
                students.append(Student(name,gpa,country,major,gender,code))
            return students
    except FileNotFoundError:
        print('Error check the file path main function in main.py!!!')

# searchs for the studend with desired code then returns the index for the student in the data list
# so I can use this index in other functions related to this specific student
def search_for_student_by_code(students_data, student_code):
    for index, student in enumerate(students_data):
        if student_code == student.code:
            return index
    
    print('Code is incorrect!')
    return None


def main():

    students_data = load_data(file_path='project/data/fake-student.csv')
    statistics = Statistics(students_data)
    # statistics.get_num_of_students_in_each_country()
    # statistics.get_average_gpa_for_each_major()
    # statistics.get_num_of_students_in_each_major()
    # statistics.get_lowest_highest_gpa_for_each_major()
    # statistics.get_male_and_females()
    student_code = input('Please provide us with the student code!\ncode: ')
    wanted_student_index = search_for_student_by_code(students_data,student_code)
    student = students_data[wanted_student_index]
    student.describe_student()

    


if __name__ == '__main__':
    main()