# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Mentor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login_mentor(self):
        print('\tlogin test start')
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("mateusz.ostafil")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kkk")
        driver.find_element_by_name("submit").click()
        print('\tlogin success')

    def list_students(self, test_student=False):
        print('\tlist student start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        if test_student:
            print('\tcheck if test student exist start')
            try:
                driver.find_element_by_xpath(
                    '//*[@id="homepage"]/section/div/table/tbody/tr[3]/td[2]').text == "test test"
            except:
                raise ValueError('there is no test student')
            print('\tcheck if test student exist success')
        print('\tlist student success')

    def add_assignments(self):
        print('\tadd assignments start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List assignments").click()
        driver.find_element_by_css_selector("input.sub-right.main-button").click()
        driver.find_element_by_id("main-form-title").clear()
        driver.find_element_by_id("main-form-title").send_keys("test")
        driver.find_element_by_id("main-form-desc").clear()
        driver.find_element_by_id("main-form-desc").send_keys("test")
        driver.find_element_by_id("main-form-date").send_keys("10/10/2012")
        driver.find_element_by_id("main-sub-button").click()
        print('\tadd assignments success')

    def list_assignments(self, test_assignments=False):
        print('\tlist assignments start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List assignments").click()
        if test_assignments:
            print('\t\tcheck if test assignments exist start')
            try:
                driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[1]').text == "test"
            except:
                raise ValueError('there is no test assignments')
            print('\t\tcheck if test assignments exist success')
        print('\tlist assignments success')

    def remove_assignments(self):
        print('\tremove assignments start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List assignments").click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[6]/a').click()
        print('\tremove assignments success')

    def attendance(self):
        print('\tattendance test start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Check attendance").click()
        driver.find_element_by_css_selector("span").click()
        driver.find_element_by_xpath(
            "//body[@id='homepage']/section/form/div/table/tbody/tr[2]/td[2]/label/span").click()
        driver.find_element_by_id("attendance-sub-button").click()
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Show student statistics").click()
        print('\t\tcheck if students have correct attendance % start')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr[1]/td[3]').text == "100.0"
        except:
            raise ValueError('no visable present %% in piotrek')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr[2]/td[3]').text == "100.0"
        except:
            raise ValueError('no visable present %% in monika')
        print('\t\tcheck if students have correct attendance % success')
        print('\tattendance test success')

    def add_student(self):
        print('\tadd student start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        driver.find_element_by_css_selector("input.sub-right.main-button").click()
        driver.find_element_by_name("first-name").clear()
        driver.find_element_by_name("first-name").send_keys("test")
        driver.find_element_by_name("last-name").clear()
        driver.find_element_by_name("last-name").send_keys("test")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("test")
        driver.find_element_by_name("mail").clear()
        driver.find_element_by_name("mail").send_keys("test@test.test")
        driver.find_element_by_name("phone-number").clear()
        driver.find_element_by_name("phone-number").send_keys("123456789")
        driver.find_element_by_name("submition").click()
        try:
            print("\t\tcheck if test student exist start")
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr[3]/td[2]') == "test test"
        except:
            raise ValueError('there is no test student')
        print("\t\tcheck if test student exist success")
        print('\tadd student success')

    def remove_student(self):
        print('\tremove student start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[3]/td[7]/a/i").click()
        print('\tremove student success')

    def edit_student(self):
        print('\tedit student start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        driver.find_element_by_xpath("//body[@id='homepage']/section/div/table/tbody/tr[3]/td[6]/a/i").click()
        driver.find_element_by_name("first-name").clear()
        driver.find_element_by_name("first-name").send_keys("edited")
        driver.find_element_by_name("last-name").clear()
        driver.find_element_by_name("last-name").send_keys("edited")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("edited")
        driver.find_element_by_name("mail").clear()
        driver.find_element_by_name("mail").send_keys("edited@edited.com")
        driver.find_element_by_name("submition").click()
        try:
            print("\t\tcheck if edited test student exist start")
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr[3]/td[2]') == "edited edited"
        except:
            raise ValueError('there is no test student')
        print("\t\tcheck if test edited student exist success")
        print('\tedit student success')

    def add_team(self):
        print('\tadd team start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List teams").click()
        driver.find_element_by_css_selector("input.sub-right.main-button").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("test")
        driver.find_element_by_css_selector("input.main-button").click()
        print('\t\tcheck if added team exist start')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[1]').text == "test"
        except:
            raise ValueError('there is no test team')
        print('\t\tcheck if added team exist success')
        print('\tadd team success')

    def remove_team(self):
        print('\tremove team start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List teams").click()
        driver.find_element_by_css_selector("i.fa.fa-trash").click()
        print('\tremove team success')

    def edit_team(self):
        print('\tedit team start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List teams").click()
        driver.find_element_by_css_selector("i.fa.fa-pencil-square-o").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("edit")
        driver.find_element_by_css_selector("input.main-button").click()
        print('\tedit team success')

    def add_student_to_team(self, test_student=False):
        print('\tadd student to team start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        number_of_student = 2
        if test_student:
            number_of_student = 3
        for i in range(1, number_of_student + 1):
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr[{}]/td[6]/a'.format(i)).click()
            Select(driver.find_element_by_name("team")).select_by_visible_text("test")
            driver.find_element_by_name("submition").click()
            print('\t\tcheck if student of id {} have team start'.format(i))
            try:
                driver.find_element_by_xpath(
                    '//*[@id="homepage"]/section/div/table/tbody/tr[{}]/td[5]'.format(i)) == 'test'
            except:
                raise ValueError('there is no test in student ')
            print('\t\tcheck if student of id {} have team success'.format(i))

    def check_student_team_status(self, test_student=False):
        print('\tcheck student team status start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List students").click()
        number_of_student = 2
        if test_student:
            number_of_student = 3
        for i in range(1, number_of_student + 1):
            print('\t\tcheck if student of id {} have team start'.format(i))
            try:
                driver.find_element_by_xpath(
                    '//*[@id="homepage"]/section/div/table/tbody/tr[{}]/td[5]'.format(i)) == 'test'
            except:
                raise ValueError('there is no test in student ')
            print('\t\tcheck if student of id {} have team success'.format(i))

        print('\tcheck student team status success')

    def add_checkpoint(self):
        print('\tadd checkpoint start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List checkpoints").click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div/a/input').click()
        driver.find_element_by_xpath('//*[@id="main-form-title"]').clear()
        driver.find_element_by_xpath('//*[@id="main-form-title"]').send_keys('test')
        driver.find_element_by_xpath('//*[@id="main-form-date"]').send_keys('12/12/2012')
        driver.find_element_by_xpath('//*[@id="main-sub-button"]').click()
        print('\t\tcheck if checkpoint exist start')
        try:
            driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[1]').text == 'test'
        except:
            raise ValueError('there is no checkpoint')
        print('\t\tcheck if checkpoint exist success')
        print('\tadd checkpoint success')

    def remove_checkpoint(self):
        print('\tremove checkpoint start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List checkpoints").click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[4]/form/button').click()
        print('\t\tcheck if checkpoint still exist start')
        try:
            driver.find_element_by_xpath(
                '//*[@id="homepage"]/section/div/div/p') == 'There is no Checkpoints. Please add checkpoint.'
        except:
            raise ValueError('there is still checkpoint')
        print('\t\tcheck if checkpoint still exist success')
        print('\tremove checkpoint success')

    def rate_checkpoint(self, test_student=False):
        print('\trate checkpoint start')
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("List checkpoints").click()
        driver.find_element_by_xpath('//*[@id="homepage"]/section/div/table/tbody/tr/td[3]/a/i').click()
        Select(driver.find_element_by_name("checkpoint-grade[]")).select_by_visible_text("Red")
        Select(driver.find_element_by_xpath("(//select[@name='checkpoint-grade[]'])[2]")).select_by_visible_text(
            "Yellow")
        if test_student:
            Select(driver.find_element_by_xpath("(//select[@name='checkpoint-grade[]'])[3]")).select_by_visible_text(
                "Green")
        driver.find_element_by_css_selector("button[type=\"submit\"]").click()
        driver.find_element_by_link_text("List checkpoints").click()
        print('\trate checkpoint success')

    # ------------ TESTS -----------


    def test_login(self):
        print('test login')
        Mentor.login_mentor(self)

    def test_list_students(self):
        print('test list students')
        Mentor.login_mentor(self)
        Mentor.list_students(self)

    def test_add_assignments(self):
        print('test add assignemts')
        Mentor.login_mentor(self)
        Mentor.add_assignments(self)
        Mentor.list_assignments(self, test_assignments=True)
        Mentor.remove_assignments(self)

    def test_attendance(self):
        print('test attendance')
        Mentor.login_mentor(self)
        Mentor.attendance(self)

    def test_add_student(self):
        print('test add student')
        Mentor.login_mentor(self)
        Mentor.add_student(self)
        Mentor.list_students(self, test_student=True)
        Mentor.remove_student(self)

    def test_edit_student(self):
        print('test edit student')
        Mentor.login_mentor(self)
        Mentor.add_student(self)
        Mentor.edit_student(self)
        Mentor.remove_student(self)

    def test_remove_student(self):
        print('test remove student')
        Mentor.login_mentor(self)
        Mentor.add_student(self)
        Mentor.remove_student(self)

    def test_add_team(self):
        print('test add team')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.remove_team(self)

    def test_add_student_to_team(self):
        print('test add student to team')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.add_student_to_team(self)

    def test_edit_team(self):
        print('test edit team')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.edit_team(self)
        Mentor.remove_team(self)

    def test_remove_team(self):
        print('test remove team')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.remove_team(self)

    def test_remove_team_with_students(self):
        print('test remove team with students')
        Mentor.login_mentor(self)
        Mentor.add_team(self)
        Mentor.add_student(self)
        Mentor.add_student_to_team(self, test_student=True)
        Mentor.remove_team(self)
        Mentor.check_student_team_status(self, test_student=True)

    def test_add_checkpoint(self):
        print('test add checkpoint')
        Mentor.login_mentor(self)
        Mentor.add_checkpoint(self)
        Mentor.remove_checkpoint(self)

    def test_rate_checkpoint(self):
        print('test rate checkpoint')
        Mentor.login_mentor(self)
        Mentor.add_checkpoint(self)
        Mentor.rate_checkpoint(self)
        Mentor.remove_checkpoint(self)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
