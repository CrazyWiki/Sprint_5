import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions

from urls_stellarburgers import Urls_burger
from data import FirstPersonData
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from time import sleep

@pytest.fixture
def driver():
    """Инициализация Chrome WebDriver."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def input_user_data(driver):
    """вход в аккаунт в правильным логином и паролем"""
    driver.get(Urls_burger.url_login_to_page)
    driver.find_element(*PageToLoginLocators.ptl_email_field).send_keys(FirstPersonData.first_person_email)
    driver.find_element(*PageToLoginLocators.ptl_password_field).send_keys(FirstPersonData.first_person_password)
    driver.find_element(*PageToLoginLocators.ptl_login_button).click()
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*PageToLoginLocators.ptl_login_button))
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(MainPageLocators.mp_place_order_button))
    return driver

