import time

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urban_selectors
from retrieve_phone import retrieve_phone_code


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def clear_browser_cache(self):
        self.driver.delete_all_cookies()

    def set_from(self, from_address):
        from_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_selectors.UrbanRoutesSelectors.from_field)
        )
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.to_field).send_keys(to_address)

    def get_from_address(self):
        from_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_selectors.UrbanRoutesSelectors.from_field)
        )
        return from_field.get_attribute('value')

    def get_to_address(self):
        from_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(urban_selectors.UrbanRoutesSelectors.to_field)
        )
        return from_field.get_attribute('value')

    def orden_a_taxi(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(urban_selectors.UrbanRoutesSelectors.order_a_taxi))
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.order_a_taxi).click()

    def get_orden_a_taxi(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(urban_selectors.UrbanRoutesSelectors.order_a_taxi)
            )
            return True
        except TimeoutException:
            return False

    def select_comfort_fare(self):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.comfort_tariff_button).click()

    def get_comfort_fare_selected(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(urban_selectors.UrbanRoutesSelectors.comfort_select)
            )
            return True
        except TimeoutException:
            return False

    def phone_number(self, number_phone):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.phone_field).click()
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.add_number_phone).send_keys(number_phone)
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.submit_number_phone).click()
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.code_phone_number).send_keys(phone_code)
        confirm_number = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.confirm_phone_number)
        confirm_number.click()

    def get_phone_number(self):
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(urban_selectors.UrbanRoutesSelectors.confirm_phone)
        )
        return phone_field.text

    def add_credit_card(self, card_number, card_code):
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

    def get_credit_card(self):
        credit_card_element = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.card_number)
        return credit_card_element.get_attribute("value")

    def mesagge_for_driver(self, message):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.message_field).send_keys(message)

    def get_mesage(self):
        message = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.message_field)
        return message.get_attribute("value")

    def select_blanket_and_tissues(self):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.blanket_button).click()

    def get_select_blanket_and_tissues(self):
        botton = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.blanket_button)
        return botton.is_enabled()

    def select_two_ice_cream(self, quantity):
        for _ in range(quantity):
            ice_crem = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.ice_cream_button)
            ice_crem.click()

    def get_selected_ice_cream_count(self):
        selected_count = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.ice_cream_count)
        return int(selected_count.text)

    def select_modal_taxi(self):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.search_taxi_modal).click()

    def get_modal_taxi_selected(self):
        modal_taxi = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.search_taxi_modal)
        return modal_taxi.is_displayed()

    def driver_info(self):
        time.sleep(30)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(urban_selectors.UrbanRoutesSelectors.driver_info_modal))

    def get_driver_info(self):
        driver_info_modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(urban_selectors.UrbanRoutesSelectors.driver_info_modal)
        )
        return driver_info_modal.is_displayed()
