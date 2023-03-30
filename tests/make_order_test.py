import allure
from page_objects.main_page import MainPage
from page_objects.order_form_order_page import OrderFormPage


class TestMakeOrder:
    # Проверка создания заказа по кнопке в шапке
    @allure.title('Cоздание заказа по кнопке в шапке')
    def test_make_order_header_btn(self, driver):
        order_form = OrderFormPage(driver)
        main_page = MainPage(driver)
        driver.implicitly_wait(3)
        main_page.push_order_header_btn()
        order_form.fill_name_field('Иван')
        order_form.fill_last_name_field('Иванов')
        order_form.fill_address_field('Москва')
        order_form.fill_metro_station_field('Лубянка')
        order_form.fill_phone_field('89000000711')
        order_form.check_next_btn_enabled()
        order_form.push_next_btn()
        order_form.check_about_rent_title_to_order_form_about_rent()
        order_form.fill_when_bring_field('01.05.2023')
        order_form.select_rent_time_field_1_day()
        order_form.choose_black_check_box()
        order_form.choose_grey_check_box()
        order_form.fill_comment_field('Не звонить')
        order_form.check_order_on_body_btn_enabled()
        order_form.push_to_order_btn()
        order_form.check_yes_btn_enabled()
        order_form.push_yes_btn()
        order_form.check_yes_btn_to_succesful()

    # Проверка создания заказа по кнопке в середине страницы
    @allure.title('Cоздание заказа по кнопке в середине страницы')
    def test_make_order_middle_btn(self, driver):
        order_form = OrderFormPage(driver)
        main_page = MainPage(driver)
        driver.implicitly_wait(3)
        main_page.scroll_to_order_middle_btn_button()
        main_page.push_order_middle_btn()
        order_form.fill_name_field('кирилл')
        order_form.fill_last_name_field('кириллов')
        order_form.fill_address_field('Москва, ул. Академика')
        order_form.fill_metro_station_field('Сокольники')
        order_form.fill_phone_field('89077000711')
        order_form.check_next_btn_enabled()
        order_form.push_next_btn()
        order_form.check_about_rent_title_to_order_form_about_rent()
        order_form.fill_when_bring_field('01.07.2023')
        order_form.select_rent_time_field_2_days()
        order_form.choose_black_check_box()
        order_form.choose_grey_check_box()
        order_form.fill_comment_field('Дратути')
        order_form.check_order_on_body_btn_enabled()
        order_form.push_to_order_btn()
        order_form.check_yes_btn_enabled()
        order_form.push_yes_btn()
        order_form.check_yes_btn_to_succesful()


