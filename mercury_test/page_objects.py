from seleniumbase import BaseCase
from selenium import webdriver


class pageLogin(object):
    base_url = 'http://newtours.demoaut.com/'
    user_field = 'input[name="userName"]'
    pass_field = 'input[name="password"]'
    submit_button = 'input[name="login"]'


class pageReservation(object):
    passenger_dropdown = 'select[name="passCount"]'


class actionLogin:

    def __init__(self, myDriver):
        self.driver = myDriver

    def login(self, user_field, password):
        self.driver.get(pageLogin.base_url)
        self.driver.find_element_by_css_selector(pageLogin.user_field).send_keys(user_field)
        self.driver.find_element_by_css_selector(pageLogin.pass_field).send_keys(password)
        self.driver.find_element_by_css_selector(pageLogin.submit_button).click()
