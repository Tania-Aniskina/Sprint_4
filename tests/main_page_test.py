import allure
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage


class TestQuestions:
    @allure.title('Раскрываем первый вопрос "Сколько это стоит? И как оплатить?"')
    def test_how_much(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_how_much()
        main_page.check_how_much()

    @allure.title('Раскрываем второй вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def test_want_more_bikes(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_want_more_bikes()
        main_page.check_want_more_bikes()

    @allure.title('Раскрываем третий вопрос "Как рассчитывается время аренды?"')
    def test_push_how_count_time(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_how_count_time()
        main_page.check_how_count_time()

    @allure.title('Раскрываем четвертый вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_can_order_now(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_can_order_now()
        main_page.check_can_order_now()

    @allure.title('Раскрываем пятый вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_can_prolong_order(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_can_prolong_order()
        main_page.check_can_prolong_order()

    @allure.title('Раскрываем шестой вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_charge_station(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_charge_station()
        main_page.check_charge_station()

    @allure.title('Раскрываем седьмой вопрос "Можно ли отменить заказ?"')
    def test_cancel_order(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_cancel_order()
        main_page.check_cancel_order()

    @allure.title('Раскрываем восьмой вопрос "Я жизу за МКАДом, привезёте?"')
    def test_live_behind_mkad(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_live_to_behind_mkad()
        main_page.push_live_behind_mkad()
        main_page.check_live_behind_mkad()


class TestOrderBtn:
    @allure.title('Нажимаем на кнопку "Заказать" в header')
    def test_order_header_btn_to_order_form(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.check_order_header_btn_enabled()
        main_page.push_order_header_btn()
        main_page.check_order_header_btn_to_order_form()

    @allure.title('Нажимаем на кнопку "Заказать" в середине страницы')
    def test_order_middle_btn_to_order_form(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.scroll_to_order_middle_btn_button()
        main_page.check_order_middle_btn_enabled()
        main_page.push_order_middle_btn()
        main_page.check_order_middle_btn_to_order_form()

    @allure.title('Нажимаем на лого "Яндекс"')
    def test_push_yandex_logo(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.push_yandex_logo()
        main_page.check_yandex_link()

    @allure.title('Нажимаем на лого "Самокат"')
    def test_push_logo_samokat(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.wait_loading_main_page()
        main_page.push_order_header_btn()
        main_page.check_order_header_btn_to_order_form()
        main_page.push_logo_samokat()
        main_page.check_samokat_link()
