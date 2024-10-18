from pages.base import BasePage
from pages.locators import *
from tests.config import Config


class AuthPage(BasePage):
    """Создаем класс страницы "Авторизация" """
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = Config.BASE_URL or "https://b2c.passport.rt.ru/auth/"
        driver.get(url)
        #создаем нужные элементы
        self.login = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn_submit = driver.find_element(*AuthLocators.AUTH_BTN)
        self.mail_tab = driver.find_element(*AuthLocators.TAB_EMAIL)
        self.log_tab = driver.find_element(*AuthLocators.TAB_LOGIN)
        self.LS_tab = driver.find_element(*AuthLocators.TAB_LS)
        self.forgot_btn = driver.find_element(*AuthLocators.FORGOT_PASSWORD)

    def enter_login(self, value):
        """Ввести данные в поле логина"""
        self.login.send_keys(value)

    def enter_pass(self, value):
        """Ввести пароль"""
        self.password.send_keys(value)

    def btn_click(self):
        """Нажать на кнопку "Войти" """
        self.btn_submit.click()

    def get_right_elem_auth(self):
        """ Получаем текст правого блока страницы авторизация"""
        #Получить название блока страницы "Авторизация"
        title = self.find_element(AuthLocators.AUTH_TITLE)
        title = [''.join(title.text)]
        # Получаем названия табов
        right_block_auth = self.find_elements(AuthLocators.AUTH_BLOCK)
        tabs = "".join([x.text for x in right_block_auth]).split('\n')
        elements = title + tabs
        return elements

    def get_text_from_login(self):
        """ Получить текст из поля ввода логина"""
        text_login = self.find_element(AuthLocators.AUTH_LOGIN_TEXT)
        return text_login.text

    def check_info_about_slogan(self):
        """Получить слоган со страницы Авторизации"""
        tagline = self.find_element(GlobalLocators.TAGLINE)
        return tagline.text

    def click_email_tab(self):
        """Нажать на таб "Почта" """
        self.mail_tab.click()

    def click_login_tab(self):
        """Нажать на таб "Логин" """
        self.log_tab.click()

    def click_LS_tab(self):
        """Нажать на таб "ЛС" """
        self.LS_tab.click()


    def find_logout_btn(self):
        """Найти кнопку "Выйти" на странице личного кабинета"""
        button = self.find_element(AuthLocators.LOGOUT_BTN)

    def logout_btn_click(self):
        """Нажать на кнопку "Выйти" на странице личного кабинета"""
        button = self.find_element(AuthLocators.LOGOUT_BTN)
        button.click()

    def go_to_reg_page(self):
        """Перейти на страницу "Зарегистрироваться" со страницы "Авторизация" """
        reg_button = self.find_element(AuthLocators.REG_BTN)
        reg_button.click()

    def go_to_reset_password_page(self):
        self.forgot_btn.click()
