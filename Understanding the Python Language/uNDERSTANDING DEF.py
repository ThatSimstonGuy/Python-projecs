def add_record():
    student_id = input('Enter student id: ')
    student_name = input('Enter student name: ')
    module = input('Enter module name: ')
    marks = input('Enter marks: ')

    with open('students.txt', 'a') as file:
        file.write(f'\n{student_id}, ')



