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
        assert routes_page.get_from_address() == data.address_from, (f"Expected: {data.address_from},"
                                                                     f""f" Actual: {routes_page.get_from_address()}")
        assert routes_page.get_to_address() == data.address_to, (f"Expected: {data.address_to}, "
                                                                 f""f"Actual: {routes_page.get_to_address()}")

    def test_orden_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        assert routes_page.get_orden_a_taxi() == True

    def test_comfort_mode(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        assert routes_page.get_comfort_fare_selected() == True

    def test_fill_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        assert routes_page.get_phone_number() == data.phone_number

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        assert routes_page.get_credit_card() == data.card_number

    def test_mesagge_for_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.mesagge_for_driver(data.message_for_driver)
        assert routes_page.get_mesage() == data.message_for_driver

    def test_select_blanket_and_tissues(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.mesagge_for_driver(data.message_for_driver)
        routes_page.select_blanket_and_tissues()
        assert routes_page.get_select_blanket_and_tissues() == True

    def test_select_two_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.mesagge_for_driver(data.message_for_driver)
        routes_page.select_two_ice_cream(2)
        assert routes_page.get_selected_ice_cream_count() == 2

    def test_select_modal_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.mesagge_for_driver(data.message_for_driver)
        routes_page.select_modal_taxi()
        assert routes_page.get_modal_taxi_selected() == True

    def test_driver_info(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.mesagge_for_driver(data.message_for_driver)
        routes_page.select_modal_taxi()
        routes_page.driver_info()
        assert routes_page.get_driver_info() == True

    def test_order_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        routes_page.orden_a_taxi()
        routes_page.select_comfort_fare()
        routes_page.phone_number(data.phone_number)
        routes_page.add_credit_card(data.card_number, data.card_code)
        routes_page.mesagge_for_driver(data.message_for_driver)
        routes_page.select_modal_taxi()
        routes_page.driver_info()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
