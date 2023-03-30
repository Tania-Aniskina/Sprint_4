import allure
from locators.order_form_order_locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Класс первой страницы формы заказа
class OrderFormPage:

    # метод добавления конструктора класса
    def __init__(self, driver):
        self.driver = driver

    # метод заполняет поле "Имя"
    @allure.step("Заполнение поля 'Имя'")
    def fill_name_field(self, name):
        self.driver.find_element(By.XPATH, Locators.name_field).send_keys(name)

    # метод заполняет поле "Фамилия"
    @allure.step("Заполнение поля 'Фамилия'")
    def fill_last_name_field(self, last_name):
        self.driver.find_element(By.XPATH, Locators.last_name_field).send_keys(last_name)

    # метод заполняет поле "Адрес"
    @allure.step("Заполнение поля 'Адрес'")
    def fill_address_field(self, address):
        self.driver.find_element(By.XPATH, Locators.address_field).send_keys(address)

    # метод заполняет поле "Станция метро"
    @allure.step("Заполнение поля 'Станция метро'")
    def fill_metro_station_field(self, metro):
        self.driver.find_element(By.XPATH, Locators.metro_station_field).send_keys(metro)
        self.driver.find_element(By.CLASS_NAME, Locators.metro_first).click()

    # метод заполняет поле "Телефон"
    @allure.step("Заполнение поля 'Телефон'")
    def fill_phone_field(self, phone_number):
        self.driver.find_element(By.XPATH, Locators.phone_field).send_keys(phone_number)

    # метод проверяет активна ли кнопка "Далее"
    @allure.step("Проверка активна ли кнопка 'Далее'")
    def check_next_btn_enabled(self):
        return self.driver.find_element(By.XPATH, Locators.next_btn).is_enabled()

    #  метод кликает на кнопку "Далее"
    @allure.step("Нажатие на кнопку 'Далее'")
    def push_next_btn(self):
        self.driver.find_element(By.XPATH, Locators.next_btn).click()

    # метод проверяет ведет ли кнопка "Далее" на форму заказа "Про аренду"
    @allure.step("Проверка ведет ли кнопка 'Далее'на форму заказа 'Про аренду'")
    def check_about_rent_title_to_order_form_about_rent(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.about_rent_title).text
        expected_value = 'Про аренду'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод заполняющий поле "Когда привезти самокат?"
    @allure.step("Заполнение поля 'Когда привезти самокат?'")
    def fill_when_bring_field(self, when_bring):
        when = self.driver.find_element(By.XPATH, Locators.when_bring_field)
        when.send_keys(when_bring)
        when.send_keys(Keys.ENTER)

    # метод заполняющий поле "Срок аренды" 1 сутки
    @allure.step("Выбор первого значения в поле 'Срок аренды'")
    def select_rent_time_field_1_day(self):
        self.driver.find_element(By.XPATH, Locators.rent_time_field).click()
        self.driver.find_element(By.XPATH, Locators.rent_time_field_1_day).click()

    # метод заполняющий поле "Срок аренды" 2 суток
    @allure.step("Выбор второго значения в поле 'Срок аренды'")
    def select_rent_time_field_2_days(self):
        self.driver.find_element(By.XPATH, Locators.rent_time_field).click()
        self.driver.find_element(By.XPATH, Locators.rent_time_field_2_days).click()

    # метод кликающий на чек-бокс "черный жемчуг"
    @allure.step("Нажатие на чек-бокс 'черный жемчуг'")
    def choose_black_check_box(self):
        self.driver.find_element(By.XPATH, Locators.black_check_box).click()

    # метод кликающий на чек-бокс "серая безысходность"
    @allure.step("Нажатие на чек-бокс 'серая безысходность'")
    def choose_grey_check_box(self):
        self.driver.find_element(By.XPATH, Locators.grey_check_box).click()

    # метод заполняющий поле "Комментарий для курьера"
    @allure.step("Заполнение поля 'Комментарий для курьера'")
    def fill_comment_field(self, comment_field):
        self.driver.find_element(By.XPATH, Locators.comment_field).send_keys(comment_field)

    # метод проверяет активна ли кнопка "Заказать"
    @allure.step("Проверка активна ли кнопка 'Заказать'")
    def check_order_on_body_btn_enabled(self):
        return self.driver.find_element(By.XPATH, Locators.order_on_body_btn).is_enabled()

    #  метод кликает на кнопку "Заказать"
    @allure.step("Нажатие на кнопку 'Заказать'")
    def push_to_order_btn(self):
        self.driver.find_element(By.XPATH, Locators.order_on_body_btn).click()

    # метод проверяет ведет ли кнопка "Заказать" на форму заказа "Хотите оформить заказ?"
    @allure.step("Проверяет ведет ли кнопка 'Заказать' на форму заказа 'Хотите оформить заказ?'")
    def check_order_on_body_btn_want_to_finish_title(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.want_to_finish_title).text
        expected_value = 'Хотите оформить заказ?'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод проверяет активна ли кнопка "Да"
    @allure.step("Проверка активна ли кнопка 'Да'")
    def check_yes_btn_enabled(self):
        return self.driver.find_element(By.XPATH, Locators.yes_btn).is_enabled()

    #  метод кликает на кнопку "Да"
    @allure.step("Нажатие на кнопку 'Да'")
    def push_yes_btn(self):
        self.driver.find_element(By.XPATH, Locators.yes_btn).click()

    # метод проверяет ведет ли кнопка "Да" на форму заказа "Заказ оформлен"
    @allure.step("Проверяет ведет ли кнопка 'Да' на форму заказа 'Заказ оформлен'")
    def check_yes_btn_to_succesful(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.order_processed_title).text
        expected_value = 'Заказ оформлен'
        assert expected_value in actually_value , f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

















