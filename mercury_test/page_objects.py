from seleniumbase import BaseCase


class pageAction(BaseCase):

    def valid_login(self):
        self.driver.get(pageLogin.base_url)
        self.send_keys(pageLogin.user_field, 'mercury')
        self.send_keys(pageLogin.pass_field, 'mercury')
        self.click(pageLogin.submit_button)
        pass

    def invalid_login(self):
        self.driver.get(pageLogin.base_url)
        self.send_keys(pageLogin.user_field, 'invalid')
        self.send_keys(pageLogin.pass_field, 'invalid')
        self.click(pageLogin.submit_button)
        pass


class pageLogin(object):
    base_url = 'http://newtours.demoaut.com/'
    user_field = 'input[name="userName"]'
    pass_field = 'input[name="password"]'
    submit_button = 'input[name="login"]'


class pageReservation(object):
    passenger_dropdown = 'select[name="passCount"]'
    round_trip_type_radio = 'input[value="roundtrip"]'
    one_way_trip_radio= 'input[value="oneway"]'
    from_dropdown = 'select[name="fromPort"]'
    from_month_dropdown = 'select[name="fromMonth"]'
    from_day_dropdown = 'select[name="fromDay"]'
    to_dropdown = 'select[name="toPort"]'
    to_month_dropdown = 'select[name="toMonth"]'
    to_day_dropdown = 'select[name="toDay"]'
    continue_button = 'input[name="findFlights"]'
    economy_class_radio = 'input[value="Coach"]'
    business_class_radio = 'input[value="Business"]'
    first_class_radio = 'input[value="First"]'
    airline_dropdown = 'select[name="airline"]'


class pageReservation2(object):
    assert_result_page = 'from[name="results"]'