from student_statistics import Statistics
from file import File

# searchs for the studend with desired code then returns the index for the student in the data list
# so I can use this index in other functions related to this specific student
def search_for_student_by_code(students_data, student_code):
    for index, student in enumerate(students_data):
        if student_code == student.code:
            return index
    
    return None


def main():

    file_path = 'project/data/fake-student.csv'
    file = File(file_path)
    students_data = file.load_data()
    statistics = Statistics(students_data)
    # statistics menue
    # statistics.get_num_of_students_in_each_country()
    # statistics.get_average_gpa_for_each_major()
    # statistics.get_num_of_students_in_each_major()
    # statistics.get_lowest_highest_gpa_for_each_major()
    # statistics.get_male_and_females()

    # student menue
    student_code = '455234617349'
    wanted_student_index = search_for_student_by_code(students_data,student_code)
    if wanted_student_index is not None:
        student = students_data[wanted_student_index]

        # student.describe_student()
        
        # major = 'sleeping'
        # student.change_major(major)
        # file.update_file_data()
    else:
        print('Student code provided is incorrect !!!')
    


if __name__ == '__main__':
    main()