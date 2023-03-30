from selenium.webdriver.common.by import By
from locators.main_page_locators import Locators
import allure


# Класс главной страницы с вопросами
class MainPage:

    # метод добавления конструктора класса
    def __init__(self, driver):
        self.driver = driver

    # метод скроллинга до последнего вопроса
    @allure.step("Скролл до последнего вопроса")
    def scroll_live_to_behind_mkad(self):
        element = self.driver.find_element(By.XPATH, Locators.live_behind_mkad)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод раскрывает первый вопрос "Сколько это стоит? И как оплатить?"
    @allure.step("Раскрывает первый вопрос 'Сколько это стоит? И как оплатить?'")
    def push_how_much(self):
        self.driver.find_element(By.XPATH, Locators.how_much).click()

    # метод проверяет наличие надписи при раскрытии вопроса
    @allure.step("Проверяет наличие надписи при раскрытии первого вопроса")
    def check_how_much(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.how_much_open).text
        expected_value = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод раскрывает второй вопрос "Хочу сразу несколько самокатов! Так можно?"
    @allure.step("Раскрывает второй вопрос 'Хочу сразу несколько самокатов! Так можно?'")
    def push_want_more_bikes(self):
        self.driver.find_element(By.XPATH, Locators.want_more_bikes).click()

    # метод проверяет наличие надписи при раскрытии второго вопроса
    @allure.step("Проверяет наличие надписи при раскрытии второго вопроса")
    def check_want_more_bikes(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.want_more_bikes_open).text
        expected_value = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод раскрывает третий вопрос "Как рассчитывается время аренды?"
    @allure.step("Раскрывает третий вопрос 'Как рассчитывается время аренды?'")
    def push_how_count_time(self):
        self.driver.find_element(By.XPATH, Locators.how_count_time).click()

    # метод проверяет наличие надписи при раскрытии вопроса
    @allure.step("Проверяет наличие надписи при раскрытии третьего вопроса")
    def check_how_count_time(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.how_count_time_open).text
        expected_value = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод раскрывает четвертый вопрос "Можно ли заказать самокат прямо на сегодня?"
    @allure.step("Раскрывает четвертый вопрос 'Можно ли заказать самокат прямо на сегодня?'")
    def push_can_order_now(self):
        self.driver.find_element(By.XPATH, Locators.can_order_now).click()

    # метод проверяет наличие надписи при раскрытии вопроса
    @allure.step("Проверяет наличие надписи при раскрытии четвертого вопроса")
    def check_can_order_now(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.can_order_now_open).text
        expected_value = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод раскрывает пятый вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    @allure.step("Раскрывает пятый вопрос 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def push_can_prolong_order(self):
        self.driver.find_element(By.XPATH, Locators.can_prolong_order).click()

    # метод проверяет наличие надписи при раскрытии пятого вопроса
    @allure.step("Проверяет наличие надписи при раскрытии пятого вопроса")
    def check_can_prolong_order(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.can_prolong_order_open).text
        expected_value = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод раскрывает шестой вопрос "Вы привозите зарядку вместе с самокатом?"
    @allure.step("Раскрывает шестой вопрос 'Вы привозите зарядку вместе с самокатом?'")
    def push_charge_station(self):
        self.driver.find_element(By.XPATH, Locators.charge_station).click()

    # метод проверяет наличие надписи при раскрытии вопроса
    @allure.step("Проверяет наличие надписи при раскрытии шестого вопроса")
    def check_charge_station(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.charge_station_open).text
        expected_value = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод раскрывает седьмой вопрос "Можно ли отменить заказ?"
    @allure.step("Раскрывает седьмой вопрос 'Можно ли отменить заказ?'")
    def push_cancel_order(self):
        self.driver.find_element(By.XPATH, Locators.cancel_order).click()

    # метод проверяет наличие надписи при раскрытии вопроса
    @allure.step("Проверяет наличие надписи при раскрытии седьмого вопроса")
    def check_cancel_order(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.cancel_order_open).text
        expected_value = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод раскрывает восьмой вопрос "Я жизу за МКАДом, привезёте?"
    @allure.step("Раскрывает восьмой вопрос 'Я жизу за МКАДом, привезёте?'")
    def push_live_behind_mkad(self):
        self.driver.find_element(By.XPATH, Locators.live_behind_mkad).click()

    # метод проверяет наличие надписи при раскрытии вопроса
    @allure.step("Проверяет наличие надписи при раскрытии восьмого вопроса")
    def check_live_behind_mkad(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.live_behind_mkad_open).text
        expected_value = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод проверяет активна ли кнопка "Заказать" в header'е
    @allure.step("Проверяет активна ли кнопка 'Заказать' в header'е")
    def check_order_header_btn_enabled(self):
        return self.driver.find_element(By.XPATH, Locators.order_header_btn).is_enabled()

    # метод кликает по кнопке "Заказать" в header'е
    @allure.step("Нажатие на кнопку 'Заказать' в header'е")
    def push_order_header_btn(self):
        self.driver.find_element(By.XPATH, Locators.order_header_btn).click()

    # метод проверяет ведет ли кнопка "Заказать" в header'е на форму заказа
    @allure.step("Проверка оформлен ли заказ через кнопку 'Заказать' в header'е")
    def check_order_header_btn_to_order_form(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.for_who_title).text
        expected_value = 'Для кого самокат'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод скроллинга до кнопки 'Заказать' в середине страницы
    @allure.step("Скролл до кнопки 'Заказать' в середине страницы")
    def scroll_to_order_middle_btn_button(self):
        element = self.driver.find_element(By.XPATH, Locators.order_middle_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # метод проверяет активна ли кнопка "Заказать" в середине страницы
    @allure.step("Проверка активна ли кнопка 'Заказать' в середине страницы")
    def check_order_middle_btn_enabled(self):
        return self.driver.find_element(By.XPATH, Locators.order_middle_btn).is_enabled()

    # метод кликает по кнопке "Заказать" в середине страницы
    @allure.step("Нажатие на кнопку 'Заказать' в середине страницы")
    def push_order_middle_btn(self):
        self.driver.find_element(By.XPATH, Locators.order_middle_btn).click()

    # метод проверяет ведет ли кнопка "Заказать" в середине страницы на форму заказа
    @allure.step("Проверка оформлен ли заказ через кнопку 'Заказать' вв середине страницы")
    def check_order_middle_btn_to_order_form(self):
        actually_value = self.driver.find_element(By.XPATH, Locators.for_who_title).text
        expected_value = 'Для кого самокат'
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'

    # метод кликает по логотипу "Яндекс"
    @allure.step("Нажатие на лого 'Яндекс'")
    def push_yandex_logo(self):
        self.driver.find_element(By.XPATH, Locators.logo_ya).click()

    # метод проверяет ведет ли кнопка "Заказать" в середине страницы на форму заказа
    @allure.step("Проверка оформлен ли заказ через кнопку 'Заказать' вв середине страницы")
    def check_yandex_link(self):
        assert len(self.driver.window_handles) == 2

    # метод кликает по логотипу "Самокат"
    @allure.step("Нажатие на лого 'Самокат'")
    def push_logo_samokat(self):
        self.driver.find_element(By.XPATH, Locators.logo_samokat).click()

    # метод проверяет ведет ли кнопка "Заказать" в середине страницы на форму заказа
    @allure.step("Проверка оформлен ли заказ через кнопку 'Заказать' вв середине страницы")
    def check_samokat_link(self):
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

