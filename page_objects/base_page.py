import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем загрузку главной страницы')
    def wait_loading_main_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, MainPageLocators.live_behind_mkad)))
