import pytest
import time

from pages.auth_page import *
from pages.register_page import RegPage
from config import Config


def test_create_new_acc(chrome_browser):
    """ ТС-024 Регистрация нового пользователя через e-mail при использовании валидных данных """
    page = AuthPage(chrome_browser)
    page.go_to_reg_page()
    chrome_browser.implicitly_wait(5)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(chrome_browser)
    # Вводим имя
    page.enter_firstname(Config.FIRSTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим фамилию:
    page.enter_lastname(Config.LASTNAME)
    chrome_browser.implicitly_wait(5)
    # Вводим адрес почты/Email:
    page.enter_email(Config.NEW_EMAIL)
    chrome_browser.implicitly_wait(3)
    # Вводим пароль:
    page.enter_password(Config.NEW_PASSWORD)
    chrome_browser.implicitly_wait(3)
    # Вводим подтверждение пароля:
    page.enter_pass_conf(Config.NEW_PASSWORD)
    chrome_browser.implicitly_wait(3)
    page.btn_click()
    time.sleep(60)

    """Проверяем, что регистрация пройдена и пользователь перенаправлен в личный кабинет"""
    assert page.get_relative_link() != '/account_b2c/page', 'Регистрация НЕ пройдена'
    page.driver.save_screenshot('reg_done.png')
