from seleniumbase import BaseCase
from .page_objects import actionLogin, pageReservation


class loginTests(BaseCase):

    def test_login_fail(self):
        self.action_login = actionLogin(self.driver)
        self.action_login.login('test', 'test')
        self.assert_element_not_visible(pageReservation.passenger_dropdown)

    def test_login_pass(self):
        self.action_login = actionLogin(self.driver)
        self.action_login.login('mercury', 'mercury')
        self.assert_element_present(pageReservation.passenger_dropdown)
