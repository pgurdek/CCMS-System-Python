from model.user import User
from model.sqlRequest import SqlRequest


class Employee(User):
    """
    This class representing Employee class
    """
    employee_list = []

    def save(self):
        """ Saves/updates employee in database """
        is_exist_record = SqlRequest.sql_request("SELECT * FROM employee WHERE id='{}'".format(self.id))
        if is_exist_record:
            SqlRequest.sql_request(
                "UPDATE employee SET first_name='{}', last_name='{}', telephone='{}', mail='{}', salary='{}' WHERE id='{}'".format(
                    self.first_name, self.last_name, self.telephone, self.mail, self.salary, self.id))
        else:
            SqlRequest.sql_request(
                "INSERT INTO employee (first_name, last_name, password, telephone, mail, username, salary, position) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    self.first_name, self.last_name, self.telephone, self.mail, self.salary, self.position))

    def delete(self):
        """ Removes employee from the database """
        SqlRequest.sql_request("DELETE FROM employee WHERE id='{}'".format(self.id))

    @classmethod
    def add_employee(cls, password, first_name, last_name, telephone="", mail=""):
        """
        Add new employee
        Add employee objc.
        :param password (str):
        :param first_name (str):
        :param last_name (str):
        :param telephone (str):
        :param mail (str):
        """
        username = '{}.{}'.format(first_name, last_name)
        SqlRequest.sql_request(
            'INSERT OR IGNORE INTO  employee (first_name,last_name,password,username,position) VALUES ("{}","{}","{}","{}","{}")'.format(
                first_name, last_name, password, username, 'employee'))

    @classmethod
    def list_employee(cls):
        """
        Class method for return list of employers (assistants)
        :return: (list) list of employers
        """
        query = 'SELECT * FROM employee WHERE position = "employee"'
        employeeSqlList = SqlRequest.sql_request(query)
        employeeObjectList = []
        for element in employeeSqlList:
            employeeObject = cls(id=element[0], first_name=element[1], last_name=element[2], password=element[3],
                                 telephone=element[4], mail=element[5])
            employeeObject.salary = element[-2]
            employeeObjectList.append(employeeObject)
        return employeeObjectList
