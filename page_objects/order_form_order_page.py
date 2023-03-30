import allure
from locators.order_form_order_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OrderFormPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение поля 'Имя'")
    def fill_name_field(self, name):
        self.driver.find_element(By.XPATH, OrderPageLocators.name_field).send_keys(name)

    @allure.step("Заполнение поля 'Фамилия'")
    def fill_last_name_field(self, last_name):
        self.driver.find_element(By.XPATH, OrderPageLocators.last_name_field).send_keys(last_name)

    @allure.step("Заполнение поля 'Адрес'")
    def fill_address_field(self, address):
        self.driver.find_element(By.XPATH, OrderPageLocators.address_field).send_keys(address)

    @allure.step("Заполнение поля 'Станция метро'")
    def fill_metro_station_field(self, metro):
        self.driver.find_element(By.XPATH, OrderPageLocators.metro_station_field).send_keys(metro)
        self.driver.find_element(By.CLASS_NAME, OrderPageLocators.metro_first).click()

    @allure.step("Заполнение поля 'Телефон'")
    def fill_phone_field(self, phone_number):
        self.driver.find_element(By.XPATH, OrderPageLocators.phone_field).send_keys(phone_number)

    @allure.step("Проверка активна ли кнопка 'Далее'")
    def check_next_btn_enabled(self):
        return self.driver.find_element(By.XPATH, OrderPageLocators.next_btn).is_enabled()

    @allure.step("Нажатие на кнопку 'Далее'")
    def push_next_btn(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.next_btn).click()

    @allure.step("Проверка ведет ли кнопка 'Далее'на форму заказа 'Про аренду'")
    def check_about_rent_title_to_order_form_about_rent(self):
        actually_value = self.driver.find_element(By.XPATH, OrderPageLocators.about_rent_title).text
        expected_value = 'Про аренду'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step("Заполнение поля 'Когда привезти самокат?'")
    def fill_when_bring_field(self, when_bring):
        when = self.driver.find_element(By.XPATH, OrderPageLocators.when_bring_field)
        when.send_keys(when_bring)
        when.send_keys(Keys.ENTER)

    @allure.step("Выбор первого значения в поле 'Срок аренды'")
    def select_rent_time_field_1_day(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.rent_time_field).click()
        self.driver.find_element(By.XPATH, OrderPageLocators.rent_time_field_1_day).click()

    @allure.step("Выбор второго значения в поле 'Срок аренды'")
    def select_rent_time_field_2_days(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.rent_time_field).click()
        self.driver.find_element(By.XPATH, OrderPageLocators.rent_time_field_2_days).click()

    @allure.step("Нажатие на чек-бокс 'черный жемчуг'")
    def choose_black_check_box(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.black_check_box).click()

    @allure.step("Нажатие на чек-бокс 'серая безысходность'")
    def choose_grey_check_box(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.grey_check_box).click()

    @allure.step("Заполнение поля 'Комментарий для курьера'")
    def fill_comment_field(self, comment_field):
        self.driver.find_element(By.XPATH, OrderPageLocators.comment_field).send_keys(comment_field)

    @allure.step("Проверка активна ли кнопка 'Заказать'")
    def check_order_on_body_btn_enabled(self):
        return self.driver.find_element(By.XPATH, OrderPageLocators.order_on_body_btn).is_enabled()

    @allure.step("Нажатие на кнопку 'Заказать'")
    def push_to_order_btn(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.order_on_body_btn).click()

    @allure.step("Проверяет ведет ли кнопка 'Заказать' на форму заказа 'Хотите оформить заказ?'")
    def check_order_on_body_btn_want_to_finish_title(self):
        actually_value = self.driver.find_element(By.XPATH, OrderPageLocators.want_to_finish_title).text
        expected_value = 'Хотите оформить заказ?'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    @allure.step("Проверка активна ли кнопка 'Да'")
    def check_yes_btn_enabled(self):
        return self.driver.find_element(By.XPATH, OrderPageLocators.yes_btn).is_enabled()

    @allure.step("Нажатие на кнопку 'Да'")
    def push_yes_btn(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.yes_btn).click()

    @allure.step("Проверяет ведет ли кнопка 'Да' на форму заказа 'Заказ оформлен'")
    def check_yes_btn_to_succesful(self):
        actually_value = self.driver.find_element(By.XPATH, OrderPageLocators.order_processed_title).text
        expected_value = 'Заказ оформлен'
        assert expected_value in actually_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'
