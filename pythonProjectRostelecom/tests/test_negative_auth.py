import pytest
import time

from pages.auth_page import AuthPage, GlobalLocators
from pages.locators import AuthLocators
from tests.config import Config


def test_login_with_invalid_phone(chrome_browser):
    """ TC-019 Авторизация по номеру телефона при использовании невалидного номера телефона """
    page = AuthPage(chrome_browser)
    page.enter_login(Config.INVALID_PHONE)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(25) # Ввод капчи в ручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

def test_login_with_invalid_email(chrome_browser):
    """ TC-020 Авторизация по e-mail при использовании невалидного e-mail """
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.INVALID_EMAIL)
    page.enter_pass(Config.VALID_PASSWORD)
    time.sleep(25)  # Ввод капчи в ручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

def test_login_with_valid_email_invalid_pass(chrome_browser):
    """ TC-023 Авторизация по e-mail при использовании невалидного пароля """
    page = AuthPage(chrome_browser)
    page.click_email_tab()
    page.enter_login(Config.VALID_EMAIL)
    page.enter_pass(Config.INVALID_PASSWORD)
    time.sleep(25)  # Ввод капчи в ручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'

def test_login_with_valid_phone_invalid_pass(chrome_browser):
    """ TC-022 Авторизация по номеру телефона при использовании невалидного пароля """
    page = AuthPage(chrome_browser)
    page.enter_login(Config.VALID_PHONE)
    page.enter_pass(Config.INVALID_PASSWORD)
    time.sleep(25) # Ввод капчи в ручную
    page.btn_click()
    error_mess = page.find_element(AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = page.find_element(AuthLocators.FORGOT_PASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'
