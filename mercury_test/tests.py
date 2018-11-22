from .page_objects import pageReservation, pageAction, pageReservation2


class loginTests(pageAction):

    def test_login_fail(self):
        self.invalid_login()
        self.assert_element_not_visible(pageReservation.passenger_dropdown)

    def test_login_pass(self):
        self.valid_login()
        self.assert_element_present(pageReservation.passenger_dropdown)


class reservationTests(pageAction):

    def test_book_a_flight(self):
        self.valid_login()
        self.click(pageReservation.one_way_trip_radio)
        self.select_option_by_index(pageReservation.passenger_dropdown, '1')
        self.select_option_by_value(pageReservation.from_dropdown, 'Paris')
        self.select_option_by_value(pageReservation.from_month_dropdown, '1')
        self.select_option_by_value(pageReservation.from_day_dropdown, '1')
        self.select_option_by_value(pageReservation.to_dropdown, 'Sydney')
        self.select_option_by_value(pageReservation.to_month_dropdown, '3')
        self.select_option_by_value(pageReservation.to_day_dropdown, '10')
        self.click(pageReservation.continue_button)
        title = self.get_page_title()
        self.assertTrue("Select a Flight" in title)
