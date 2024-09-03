from urls_stellarburgers import Urls_burger
from locators import *

class TestConstructorBurgerStellarPage:
    def test_constructor_sauce_scroll(self,driver):
        """переход на соусы"""
        driver.get(Urls_burger.url_main)
        driver.find_element(*MainPageLocators.mp_constructor_button).click()
        driver.find_element(*MainPageLocators.mp_sauce_button).click()
        assert driver.find_element(*MainPageLocators.mp_h_sauces).text=='Соусы'

    def test_constructor_bun_scroll(self,driver):
        """переход на булки"""
        driver.get(Urls_burger.url_main)
        driver.find_element(*MainPageLocators.mp_constructor_button).click()
        driver.find_element(*MainPageLocators.mp_sauce_button).click()
        driver.find_element(*MainPageLocators.mp_ban_button).click()
        assert driver.find_element(*MainPageLocators.mp_h_ban).text==('Булки')
    def test_constructor_bun_scroll(self,driver):
        """переход на начинкаи"""
        driver.get(Urls_burger.url_main)
        driver.find_element(*MainPageLocators.mp_constructor_button).click()
        driver.find_element(*MainPageLocators.mp_filling_button).click()
        assert driver.find_element(*MainPageLocators.mp_h_filling).text==('Начинки')



