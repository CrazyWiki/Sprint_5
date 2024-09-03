from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls_stellarburgers import Urls_burger
from locators import *

class TestForTransiteFromProfileAccountPage:
    def test_open_personal_account(self,input_user_data):
        driver=input_user_data
        driver.find_element(*MainPageLocators.mp_personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(PersonalPageLocators.pp_navigtion_list))

        assert driver.current_url==Urls_burger.url_personal_account and driver.find_element(*PersonalPageLocators.pp_history_shop_button).text=='История заказов'
    def test_for_transite_to_constructor_page(self,input_user_data):
        driver=input_user_data
        driver.find_element(*MainPageLocators.mp_personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(PersonalPageLocators.pp_navigtion_list))
        driver.find_element(*MainPageLocators.mp_constructor_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(MainPageLocators.mp_text))
        assert driver.current_url==Urls_burger.url_main+'/'

    def test_for_transite_to_constructor_page_by_logo(self, input_user_data):
        driver = input_user_data
        driver.find_element(*MainPageLocators.mp_personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(PersonalPageLocators.pp_navigtion_list))
        driver.find_element(*MainPageLocators.mp_logo_header).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(MainPageLocators.mp_text))
        assert driver.current_url == Urls_burger.url_main + '/'
    #Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.
    def test_logout(self,input_user_data):
        driver=input_user_data
        driver.find_element(*MainPageLocators.mp_personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(PersonalPageLocators.pp_navigtion_list))
        driver.find_element(*PersonalPageLocators.pp_logout_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(PageToLoginLocators.ptl_login_button))
        assert driver.current_url==Urls_burger.url_login_to_page
