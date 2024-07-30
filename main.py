import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import data


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
        Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
        El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
                if code:
                    break
        except WebDriverException as e:
            time.sleep(1)
            continue
        if code:
            break

    if not code:
        raise Exception("No se encontró el código de confirmación del teléfono.\n"
                        "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
    return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_a_taxi = (By.XPATH, "//button[@type='button' and @class='button round']")
    comfort_tariff_button = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_field = (By.XPATH, "//div[@class='np-text' and text()='Número de teléfono']")
    number_phone_modal = (By.XPATH, "(//div[contains(@class, 'section') and contains(@class, 'active')])[1]")
    add_number_phone = (By.XPATH, "//input[@id='phone' and @class='input' and @name='phone']")
    submit_number_phone = (By.XPATH, "//button[@type='submit' and @class='button full' and contains(text(), "
                                     "'Siguiente')]")
    code_phone_number = (By.XPATH, "//input[@id='code' and @class='input']")
    confirm_phone_number = (By.XPATH, "//button[@type='submit' and @class='button full' and text()='Confirmar']")
    payment_method = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number = (By.XPATH, "//input[@type='text' and @id='number' and @name='number' and @placeholder='1234 4321 "
                             "1408' and @class='card-input']")
    card_cvv_field = (By.XPATH, "//input[@type='text' and @id='code' and @name='code' and @placeholder='12' and "
                                "@class='card-input']")
    submit_card_button = (By.XPATH, "//button[@type='submit' and contains(text(),'Agregar')]")
    close_payment_method = (By.XPATH,
                            "(//div[@class='section active']//button[contains(@class, 'close-button') and "
                            "contains(@class, 'section-close')])[2]")
    message_field = (By.XPATH, "//input[@id='comment' and @class='input']")
    blanket_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div["
                                "2]/div/span")
    ice_cream_button = (By.XPATH, "//div[@class='counter-plus']")
    search_taxi_modal = (By.XPATH, "//button[@type='button' and @class='smart-button']")
    driver_info_modal = (By.XPATH, "//div[@class='order-header-title']")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, address_from):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def set_route(self, address_from, address_to):
        pass

    def orden_a_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_a_taxi))
        self.driver.find_element(*self.order_a_taxi).click()

    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff_button).click()

    def set_phone_number(self, number_phone):
        self.driver.find_element(*self.phone_field).click()
        self.driver.find_element(*self.add_number_phone).send_keys(number_phone)
        self.driver.find_element(*self.submit_number_phone).click()
        phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.code_phone_number).send_keys(phone_code)
        self.driver.find_element(*self.confirm_phone_number).click()

    def add_card(self, card_number, card_code):
        self.driver.find_element(*self.payment_method).click()
        self.driver.find_element(*self.add_card_button).click()
        element = self.driver.find_element(*self.card_number)
        element.send_keys(card_number)
        element = self.driver.find_element(*self.card_cvv_field)
        element.send_keys(card_code)
        element.send_keys(Keys.TAB)
        element = self.driver.find_element(*self.submit_card_button)
        element.click()
        self.driver.find_element(*self.close_payment_method).click()

    def set_message(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def order_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_button).click()

    def order_ice_cream(self, quantity):
        for _ in range(quantity):
            self.driver.find_element(*self.ice_cream_button).click()


    def wait_for_driver_info(self):
        self.driver.find_element(*self.search_taxi_modal).click()

    def driver_info(self):
        time.sleep(50)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.driver_info_modal))


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de
        # confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

    def test_order_taxi(cls):
        routes_page = UrbanRoutesPage(cls.driver)
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
