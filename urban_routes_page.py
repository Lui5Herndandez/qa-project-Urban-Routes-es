import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import urban_selectors
from retrieve_phone import retrieve_phone_code
import data


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.to_field).send_keys(to_address)

    def get_from_address(self):
        from_field = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(urban_selectors.UrbanRoutesSelectors.from_field)
        )
        return from_field.get_attribute('value')

    def get_to_address(self):
        from_field = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(urban_selectors.UrbanRoutesSelectors.to_field)
        )
        return from_field.get_attribute('value')

    def test_orden_a_taxi(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(urban_selectors.UrbanRoutesSelectors.order_a_taxi))
        orde_taxi = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.order_a_taxi)
        orde_taxi.click()
        assert (orde_taxi.is_displayed(), "El botón de orden_taxi no se encontró o no es visible.")

    def test_select_comfort_fare(self):
        comfort = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.comfort_tariff_button)
        comfort.click()
        assert (comfort.is_displayed(), "El botón de Comfort no se encontró o no es visible.")

    def test_fill_phone_number(self, number_phone):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.phone_field).click()
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.add_number_phone).send_keys(number_phone)
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.submit_number_phone).click()
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.code_phone_number).send_keys(phone_code)
        confirm_number = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.confirm_phone_number)
        confirm_number.click()
        assert (confirm_number.is_displayed(), "El botón de confirm_number no se encontró o no es visible.")

    def test_add_credit_card(self, card_number, card_code):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.payment_method).click()
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.add_card_button).click()
        element = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.card_number)
        element.send_keys(card_number)
        element = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.card_cvv_field)
        element.send_keys(card_code)
        element.send_keys(Keys.TAB)
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.submit_card_button).click()
        finish_add_card = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.close_payment_method)
        finish_add_card.click()
        assert (finish_add_card.is_displayed(), "El botón finish_add_card no se encontró o no es visible")

    def test_mesagge_for_driver(self, message):
        message_to_driver = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.message_field)
        message_to_driver.send_keys(message)
        assert (message_to_driver.is_displayed(), "El botón de Comfort no se encontró o no es visible.")

    def test_select_blanket_and_tissues(self):
        blanket = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.blanket_button)
        blanket.click()
        assert (blanket.is_displayed(), "El botón de blanket_and_tissues no se encontró o no es visible.")

    def test_select_two_ice_cream(self, quantity):
        for _ in range(quantity):
            ice_crem = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.ice_cream_button)
            ice_crem.click()
            assert (ice_crem.is_displayed(), "El botón de ice_crem no se encontró o no es visible.")

    def test_select_modal_taxi(self):
        wait_info = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.search_taxi_modal)
        wait_info.click()
        assert (wait_info.is_displayed(), "El modal de wait_for_driver_info no se encontró o no es visible.")

    def test_driver_info(self):
        time.sleep(30)
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(urban_selectors.UrbanRoutesSelectors.driver_info_modal))
        info_taxi_driver = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.driver_info_modal)
        assert info_taxi_driver.is_displayed(), "El modal info_taxi_driver no se encontró o no es visible."
