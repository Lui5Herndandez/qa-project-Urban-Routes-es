from selenium.webdriver.common.by import By


class UrbanRoutesSelectors:
    from_field = (By.CSS_SELECTOR, '[id="from"]')
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
