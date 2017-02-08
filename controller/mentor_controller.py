from model import student
from model import attendance
from model.assignment import Assignment
from controller.employee_controller import EmployeeController
from controller.user_controller import UserController
import view
from model.student import Student
from .user_controller import UserController


class MentorController(EmployeeController):

    def list_assignment(self):
        assignment_list = []
        for assignment in Assignment.get_list():
            assignment_list.append(str(assignment).split())
        return assignment_list

    def add_assiment(self, title, description, due_date):
        if Assignment.create(title, description, due_date):
            return True
        return False

    def grade_assignment(self, assiment_title, student_username, grade):
        for assiment in Assignment.get_list():
            if assiment.get_title() == assiment_title:
                try:
                    if assiment.grade_assigment(student_username, grade):
                        return True
                except:
                    return False

    @staticmethod
    def check_attendence(day):
        atta = attendance.Attendance(day, {})
        for person in student.Student.list_of_students:
            print('{} {}'.format(person.first_name, person.last_name))
            while True:
                ask = input('0 or 1')
                if ask == '0' or ask == '1':
                    break
            atta.check_attendance(person.username, ask)
        atta.add()

    def add_student(self, first_name, last_name, password):
        student.Student.add_student(password, first_name, last_name)

    def edit_student(self, number, telep, mai):
        for index, stu in enumerate(student.Student.list_of_students):
            if str(index) == number:
                stu.edit_student(telephone=telep, mail=mai)

    def remove_student(self, number):
        for index, stu in enumerate(student.Student.list_of_students):
            if str(index) == number:
                student.Student.delete_student(stu.username)

    def view_presence_statistic(self):
        return attendance.Attendance.present_statistic()

    def view_details(self, number):
        for index, assignment in enumerate(Assignment.list_assignment):
            if str(index) == number:
                return assignment.view_details()
        return None

    @staticmethod
    def mentor_session(user):
        session = MentorController(user)
        while True:
            view.View.mentor_menu()
            option = input('\nChoose the option:')
            if option == '1':
                view.View.clear()
                day = input('write day "day.month.year"')
                MentorController.check_attendence(day)

            elif option == '2':
                view.View.clear()
                title = input('Enter assignment title: ')
                description = input('Enter assignment description: ')
                due_date = input('Enter assignment due date:')
                if session.add_assiment(title, description, due_date):
                    print('Assignment was added.')
                else:
                    print('Assignment was\'t added. Try again.')
                input('\nEnter some key to get back:')

            elif option == '3':
                view.View.clear()
                assignment_list = session.list_assignment()
                view.View.print_two_demention_list(assignment_list)
                number = input('Enter index of assigment: ')
                details = session.view_details(number)
                if details:
                    view.View.print_two_demention_list(details)
                    title = details[0]
                    u_name = input('\nSelect username:')
                    grade = input('\nEnter grade:')
                    if session.grade_assignment(title, u_name, grade):
                        print('You grade assigment.')
                        input('\nEnter some key to get back:')
                    else:
                        print('There is no student with given username.')
                        input('\nEnter some key to get back:')

            elif option == '4':
                view.View.clear()
                first_name = input('First name: ')
                last_name = input('Last name: ')
                password = input('Password: ')
                session.add_student(first_name, last_name, password)
                input('\nEnter some key to get back:')

            elif option == '5':
                view.View.clear()
                view.View.print_user_list(student.Student.list_of_students)
                number = input('Select number of student: ')
                telephone = input('Telephone: ')
                mail = input('Mail: ')
                session.edit_student(number, telephone, mail)
                input('\nEnter some key to get back:')

            elif option == '6':
                view.View.clear()
                view.View.print_user_list(Student.list_of_students)
                number = input('number of student: ')
                session.remove_student(number)
                input('\nEnter some key to get back:')

            elif option == '7':
                view.View.clear()
                view.View.display_static_present(session.view_presence_statistic())
                input('\nEnter some key to get back:')

            elif option == '0':
                UserController.sign_out()
                return
            else:
                print('Enter valid option.')
                continue
