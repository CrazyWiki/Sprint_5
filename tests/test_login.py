from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from urls_stellarburgers import Urls_burger
from locators import *
from data import FirstPersonData
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class TestLoginStellarBurger:
    def test_login_with_correct_login_password_main_page_success(self, driver):
        #вход по кнопке «Войти в аккаунт» на главной
        driver.get(Urls_burger.url_main)
        driver.find_element(*MainPageLocators.mp_personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageToLoginLocators.ptl_text_entr))
        driver.find_element(*PageToLoginLocators.ptl_email_field).send_keys(FirstPersonData.first_person_email)
        driver.find_element(*PageToLoginLocators.ptl_password_field).send_keys(FirstPersonData.first_person_password)
        driver.find_element(*PageToLoginLocators.ptl_login_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.mp_place_order_button))
        assert driver.current_url == Urls_burger.url_main+'/'
    def test_login_with_correct_login_password_personal_account_succes(self, driver):
        #вход по кнопке «Личный кабинет» на главной
        driver.get(Urls_burger.url_main)
        driver.find_element(*MainPageLocators.mp_personal_account_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageToLoginLocators.ptl_text_entr))
        driver.find_element(*PageToLoginLocators.ptl_email_field).send_keys(FirstPersonData.first_person_email)
        driver.find_element(*PageToLoginLocators.ptl_password_field).send_keys(FirstPersonData.first_person_password)
        driver.find_element(*PageToLoginLocators.ptl_login_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(MainPageLocators.mp_place_order_button))

        assert driver.current_url == Urls_burger.url_main+'/'

    def test_login_with_correct_login_password_from_registration_page_success(self, driver):
        #вход через кнопку в форме регистрации,
        driver.get(Urls_burger.url_registation_page)
        driver.find_element(*RegistrationPageLocators.reg_login_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageToLoginLocators.ptl_text_entr))
        driver.find_element(*PageToLoginLocators.ptl_email_field).send_keys(FirstPersonData.first_person_email)
        driver.find_element(*PageToLoginLocators.ptl_password_field).send_keys(FirstPersonData.first_person_password)
        driver.find_element(*PageToLoginLocators.ptl_login_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(MainPageLocators.mp_place_order_button))

        assert driver.current_url == Urls_burger.url_main+'/'
    def test_login_with_correct_login_password_from_recovery_password_page_succes(self, driver):
        #вход через кнопку в форме восстановления пароля.
        driver.get(Urls_burger.url_password_recovery_page)
        driver.find_element(*PasswordRecoveryPageLocators.rec_login_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageToLoginLocators.ptl_text_entr))
        driver.find_element(*PageToLoginLocators.ptl_email_field).send_keys(FirstPersonData.first_person_email)
        driver.find_element(*PageToLoginLocators.ptl_password_field).send_keys(FirstPersonData.first_person_password)
        driver.find_element(*PageToLoginLocators.ptl_login_button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located(MainPageLocators.mp_place_order_button))

        assert driver.current_url == Urls_burger.url_main + '/'
