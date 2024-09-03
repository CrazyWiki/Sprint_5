from selenium.webdriver.common.by import By


class MainPageLocators:
    mp_constructor_button = (By.XPATH, ".//p[text()='Конструктор' and contains(@class,'AppHeader')]/parent::*")
    mp_order_feed_button = (By.XPATH, ".//p[text()='Лента заказов' and contains(@class,'AppHeader')]")
    mp_personal_account_button = (By.XPATH, ".//p[text()='Личный Кабинет' and contains(@class,'AppHeader')]")
    mp_logo_header = (By.XPATH, ".//a//parent::*/div[contains(@class,'AppHeader_header__logo')]")
    mp_login_to_account_button=(By.XPATH,".//button[text()='Войти в аккаунт']")
    mp_text=(By.XPATH,".//h1[text()='Соберите бургер']")
    mp_place_order_button=(By.XPATH,".//button[text()='Оформить заказ']")

    mp_sauce_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    mp_ban_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    mp_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    mp_h_sauces = (By.XPATH, ".//h2[contains(@class,'text text_type_main') and text()='Соусы']")
    mp_h_ban = (By.XPATH, ".//h2[contains(@class,'text text_type_main') and text()='Булки']")
    mp_h_filling = (By.XPATH, ".//h2[contains(@class,'text text_type_main') and text()='Начинки']")

    mp_img_fillings=(By.XPATH,".//img[text()='Говяжий метеорит (отбивная)']")
    mp_constructor_busket=(By.CLASS_NAME,"BurgerConstructor_basket__29Cd7 mt-25 ")


class PageToLoginLocators:
    ptl_text_entr = (By.XPATH, ".//h2[text()='Вход']")
    ptl_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    ptl_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    ptl_login_button = (By.XPATH, "//div/main/div/form/button")


class PersonalPageLocators:
    pp_logout_button = (By.XPATH, ".//button[text()='Выход']")
    pp_info_message = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    pp_navigtion_list=(By.XPATH,"//nav[contains(@class,'Account_nav')]")
    pp_history_shop_button = (By.XPATH,
                              ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")


class RegistrationPageLocators:
    reg_text_field_registration = (By.XPATH, ".//h2[text()='Регистрация']")
    reg_name_field = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    reg_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    reg_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    reg_register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    reg_error_message = (By.XPATH, ".//p[text()='Некорректный пароль' and contains(@class,'error text_type_main-default')]")
    reg_login_button = (By.XPATH, ".//a[text()='Войти' and contains(@class,'Auth_link')]")
class PasswordRecoveryPageLocators:
    rec_text_recovery_field=(By.XPATH,".//h2[text()='Восстановление пароля']")
    rec_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    rec_recovery_button=(By.XPATH,".//button[text()='Восстановить']")
    rec_login_button=(By.XPATH,".//a[text()='Войти' and contains(@class,'Auth_link')]")
#class OrderFeedPageLocators:
