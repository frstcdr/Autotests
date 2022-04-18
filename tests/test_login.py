import pytest
import time

from pom.login_to_eljur import LoginToEljur
from base.seleniumbase import SeleniumBase


@pytest.mark.usefixtures('setup')
class TestLogin():
    
    @pytest.mark.xfail
    def test_login_and_password_is_right(self):
        login_page = LoginToEljur(self.driver)

        expected_element = login_page.is_text_on_page('Вход в систему')
        assert expected_element, "Page is not available"

        login_page.add_input_username('sysadmin')
        login_page.add_input_password()
        login_page.get_login_button().submit()

        expected_element = login_page.is_text_on_page('Сайт Э.1')

        #screen = SeleniumBase(self.driver)
        #screen.make_screensot()

        assert expected_element, "Wrong user, page loading too slow, page is not available"

    def test_login_is_wrong(self):
        login_page = LoginToEljur(self.driver)

        expected_element = login_page.is_text_on_page('Вход в систему')
        assert expected_element, "Page is not available"

        login_page.add_input_username('admin22n')
        login_page.add_input_password()
        login_page.get_login_button().submit()

        expected_element = login_page.is_text_on_page("Неверный логин или пароль")

        #screen = SeleniumBase(self.driver)
        #screen.make_screensot()

        assert expected_element, "Enter with wrong login was accepted"

    def test_password_is_wrong(self):
        login_page = LoginToEljur(self.driver)

        expected_element = login_page.is_text_on_page('Вход в систему')
        assert expected_element, "Page is not available"

        login_page.add_input_username('admin')
        login_page.add_input_password('12345678')
        login_page.get_login_button().submit()

        expected_element = login_page.is_text_on_page("Неверный логин или пароль")

        #screen = SeleniumBase(self.driver)
        #screen.make_screensot()

        assert expected_element, "Enter with wrong password was accepted"