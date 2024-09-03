from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from urls_stellarburgers import Urls_burger
from locators import *
from data import FirstPersonData
from data import RandomiseData


class TestRegistrationStellarBurger:
    def test_registration_with_correct_login_password_success(self, driver):
        driver.get(Urls_burger.url_registation_page)
        driver.find_element(*RegistrationPageLocators.reg_name_field).send_keys(RandomiseData.random_person_user_full_name)
        driver.find_element(*RegistrationPageLocators.reg_email_field).send_keys(RandomiseData.random_person_email)
        driver.find_element(*RegistrationPageLocators.reg_password_field).send_keys(
            RandomiseData.random_person_password)
        driver.find_element(*RegistrationPageLocators.reg_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PageToLoginLocators.ptl_text_entr))
        assert driver.current_url == Urls_burger.url_login_to_page

    @pytest.mark.parametrize('wrong_passwords', ['123', 'e', 'i8u7'])
    def test_registration_with_incorrect_password_error(self, driver,wrong_passwords):
        driver.get(Urls_burger.url_registation_page)
        driver.find_element(*RegistrationPageLocators.reg_name_field).send_keys(FirstPersonData.first_person_user_name)
        driver.find_element(*RegistrationPageLocators.reg_email_field).send_keys('hfhfhf@ura.ru')
        driver.find_element(*RegistrationPageLocators.reg_password_field).send_keys(wrong_passwords)
        driver.find_element(*RegistrationPageLocators.reg_login_button).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.reg_error_message))
        assert driver.find_element(*RegistrationPageLocators.reg_error_message).text == 'Некорректный пароль'
