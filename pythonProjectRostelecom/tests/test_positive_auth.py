import pytest
import time
from tenacity import sleep
from pages.auth_page import AuthPage, GlobalLocators
from pages.locators import AuthLocators
from tests.config import Config


def test_check_elem_auth_form(chrome_browser):
    """ ТС-001 Загрузка страницы авторизации сайта "Ростелеком" """
    page = AuthPage(chrome_browser)
    assert page.get_right_elem_auth() == Config.REQ_ELEMENTS_AUTH

def test_default_login(chrome_browser):
    """ ТС-002, Форма авторизации через "Телефон" выбрана по умолчанию """
    page = AuthPage(chrome_browser)
    assert page.get_text_from_login() == Config.DEFAULT_LOGIN_TEXT

def test_check_about_slogan(chrome_browser):
    """ TC-003a На странице Авторизации присутствует продуктовый слоган ЛК "Ростелеком ID" """
    page = AuthPage(chrome_browser)
    assert page.check_info_about_slogan() == Config.TAGLINE_TEXT

def test_check_info_for_users(chrome_browser):
    """ TC-003b На странице Авторизации присутствует вспомогательная информация для клиента в левой части страницы """
    page = AuthPage(chrome_browser)
    assert "Пользовательское соглашение" in page.find_element(GlobalLocators.LEFT_BLOCK).text.split('\n'), \
        "В левой части страницы отсутствует вспомогательная информация для клиентов"

def test_active_tab_1(chrome_browser):
    """ TC-004 При вводе почты, "Таб" автоматически переключается с "Телефона" на "Почту """
    page = AuthPage(chrome_browser)
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Электронная почта'

def test_active_tab_2(chrome_browser):
    """ TC-005 При вводе номера телефона, "Таб" автоматически переключается с "Почты" на "Телефон" """
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Мобильный телефон'

def test_active_tab_3(chrome_browser):
    """ TC-006 При вводе номера телефона, "Таб" автоматически переключается с "Логина" на "Телефон" """
    page = AuthPage(chrome_browser)
    page.click_login_tab()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(5)
    print(AuthLocators.TAB_TEL)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Мобильный телефон'

def test_active_tab_4(chrome_browser):
    """ TC-007 При вводе номера телефона, "Таб" автоматически переключается с "Лицевого счета" на "Телефон" """
    page = AuthPage(chrome_browser)
    page.click_LS_tab()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(2)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Мобильный телефон'

def test_active_tab_5(chrome_browser):
    """ TC-008 При вводе почты, "Таб" автоматически переключается с "Логина" на "Почту" """
    page = AuthPage(chrome_browser)
    page.click_login_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    assert page.find_element(AuthLocators.AUTH_placeholder).text == 'Электронная почта'

def test_login_with_valid_phone(chrome_browser):
    """ TC-009 Авторизация по номеру телефона при использовании валидных данных """
    page = AuthPage(chrome_browser)
    page.find_captcha()
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(25) # Ввод капчи в ручную
    page.btn_click()
    page.find_logout_btn()
    assert page.get_relative_link() == '/account_b2c/page'
    page.logout_btn_click()

def test_login_with_valid_email(chrome_browser):
    """ TC-010 Авторизация по e-mail при использовании валидных данных """
    page = AuthPage(chrome_browser)
    page.find_captcha()
    page.click_email_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(25)  # Ввод капчи в ручную
    page.btn_click()
    page.find_logout_btn()
    assert page.get_relative_link() == '/account_b2c/page', "Пользователь не авторизован"
    page.logout_btn_click()
