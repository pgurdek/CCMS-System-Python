from model.mentor import Mentor
from model.student import Student
from model.manager import Manager
from model.user import Employee


class UserController:

    def __init__(self, user):
        '''
        Constructor of user controller.

        Arguments:user object
        '''
        self.user = user

    @classmethod
    def log_in(cls, username, password):
        users = [Mentor.list_mentors(),
                 Student.list_student(), Employee.list_employee(), Manager.list_manager()]

        for list_of_users in users:
            for person in list_of_users:
                if username == person.username:
                    if password == person.password:
                        return person
        return None

    @classmethod
    def sign_out(cls):
        # save data to file
        # call main() function
        pass