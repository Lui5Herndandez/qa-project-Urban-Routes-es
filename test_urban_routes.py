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
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

    def test_order_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_tariff()
        routes_page.set_phone_number(data.phone_number)
        routes_page.add_card(data.card_number, data.card_code)
        routes_page.set_message(data.message_for_driver)
        routes_page.order_blanket_and_tissues()
        routes_page.order_ice_cream(2)
        routes_page.wait_for_driver_info()
        routes_page.driver_info()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
