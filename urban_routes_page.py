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

    def set_from(self, address_from):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(urban_selectors.
                                                                            UrbanRoutesSelectors.from_field))
        start_journey = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.from_field)
        start_journey.send_keys(address_from)
        address = start_journey.get_attribute('value')
        assert address == data.address_from, f"Expected: {data.address_from}, Actual: {address}"
        print("Se añadió la dirección de inicio")

    def set_to(self, address_to):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(urban_selectors.
                                                                            UrbanRoutesSelectors.to_field))
        finish_journey = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.to_field)
        finish_journey.send_keys(address_to)
        address = finish_journey.get_attribute('value')
        assert address == data.address_to, f"Expected: {data.address_to}, Actual: {address}"
        print("Se añadió la dirección de destino")

    def set_route(self, address_from, address_to):
        pass

    def orden_a_taxi(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(urban_selectors.UrbanRoutesSelectors.order_a_taxi))
        orde_taxi = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.order_a_taxi)
        orde_taxi.click()
        assert (orde_taxi.is_displayed(), "El botón de orden_taxi no se encontró o no es visible.")
        print("Se confirmó la ruta del viaje")

    def select_comfort_tariff(self):
        comfort = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.comfort_tariff_button)
        comfort.click()
        assert (comfort.is_displayed(), "El botón de Comfort no se encontró o no es visible.")
        print("Se seleccionó la tarifa comfort")

    def set_phone_number(self, number_phone):
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.phone_field).click()
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.add_number_phone).send_keys(number_phone)
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.submit_number_phone).click()
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.code_phone_number).send_keys(phone_code)
        confirm_number = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.confirm_phone_number)
        confirm_number.click()
        assert (confirm_number.is_displayed(), "El botón de confirm_number no se encontró o no es visible.")
        print("Se agregó el número de teléfono")

    def add_card(self, card_number, card_code):
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
        print("Se agregó la tarjeta de crédito")

    def set_message(self, message):
        message_to_driver = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.message_field)
        message_to_driver.send_keys(message)
        assert (message_to_driver.is_displayed(), "El botón de Comfort no se encontró o no es visible.")
        print("Se envió un mensaje al conductor")

    def order_blanket_and_tissues(self):
        blanket = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.blanket_button)
        blanket.click()
        assert (blanket.is_displayed(), "El botón de blanket_and_tissues no se encontró o no es visible.")
        print("Se pidió una manta para el viaje")

    def order_ice_cream(self, quantity):
        for _ in range(quantity):
            ice_crem = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.ice_cream_button)
            ice_crem.click()
            assert (ice_crem.is_displayed(), "El botón de ice_crem no se encontró o no es visible.")
        print("Se pidió helado")

    def wait_for_driver_info(self):
        wait_info = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.search_taxi_modal)
        wait_info.click()
        assert (wait_info.is_displayed(), "El modal de wait_for_driver_info no se encontró o no es visible.")
        print("Aparece el modal para la espera sobre la información de nuestro conductor")

    def driver_info(self):
        time.sleep(30)
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(urban_selectors.UrbanRoutesSelectors.driver_info_modal))
        info_taxi_driver = self.driver.find_element(*urban_selectors.UrbanRoutesSelectors.driver_info_modal)
        assert info_taxi_driver.is_displayed(), "El modal info_taxi_driver no se encontró o no es visible."
        print("Se muestra el modal con la información del taxi asignado")
