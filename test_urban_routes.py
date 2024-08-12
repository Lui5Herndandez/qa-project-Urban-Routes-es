from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from urban_routes_page import UrbanRoutesPage
import data


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        assert routes_page.set_from == data.address_from, (f"Expected: {data.address_from},"
                                                             f" Actual: {routes_page.set_from}")
        assert routes_page.set_to == data.address_to, (f"Expected: {data.address_to}, "
                                                       f"Actual: {routes_page.set_to}")

    def test_order_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.test_orden_a_taxi()
        routes_page.test_select_comfort_fare()
        routes_page.test_fill_phone_number(data.phone_number)
        routes_page.test_add_credit_card(data.card_number, data.card_code)
        routes_page.test_mesagge_for_driver(data.message_for_driver)
        routes_page.test_select_blanket_and_tissues()
        routes_page.test_select_two_ice_cream(2)
        routes_page.test_select_modal_taxi()
        routes_page.test_driver_info()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
