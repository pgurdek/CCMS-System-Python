import base64


class User:
    line = 0

    def __init__(self, password, first_name, last_name, telephone, mail):
        self.username = '{}.{}'.format(first_name, last_name)
        self.password = self.decodeBase64(password)
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.mail = mail

    @staticmethod
    def encodeBase64(password):
        encoded_pwd = base64.encodebytes(password.encode())
        encoded_pwd = str(encoded_pwd)

        return encoded_pwd

    @staticmethod
    def decodeBase64(password):
        passwd_striped = password.replace('\\n', '')
        passwd = passwd_striped[2:]
        passwd = passwd[:-1]
        passwd = passwd.encode()
        decoded_pwd = base64.standard_b64decode(passwd).decode()
        return decoded_pwd

    @classmethod
    def log_in(cls, username, password):
        from mentor import Mentor
        from student import Student
        from manager import Manager

        users = [Mentor.mentors_list,
                 Student.list_of_students,
                 Employee.employee_list,
                 Manager.managers_list]

        for list_of_users in users:
            for person in list_of_users:
                if username == person.username:
                    if password == person.password:
                        return person
        return False

    @classmethod
    def sign_out(cls):
        # save data to file
        cls.log_in()


class Employee(User):
    employee_list = []

    @classmethod
    def create(cls, password, first_name, last_name, telephone='', mail=''):
        password_coded = cls.encodeBase64(password)
        empl = Employee(password_coded, first_name, last_name, telephone, mail)
        cls.employee_list.append(empl)

    @classmethod
    def add_employee(cls, password, first_name, last_name, telephone, mail):
        e = Employee(password, first_name, last_name, telephone, mail)
        cls.employee_list.append(e)

    @classmethod
    def list_employee(cls):
        return cls.employee_list
