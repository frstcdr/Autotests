import os

from datetime import datetime

from selenium import webdriver

import hashlib


class Testeljur:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub",
            options=webdriver.ChromeOptions(),
        )

    def get_password():
        encode ='c0210sovsecontej2022' + datetime.datetime.now(tz=None).strftime("%Y%m%d")
        hash = hashlib.md5(str(encode).encode('utf-8')).hexdigest()
        master_password = hash[22:]
        return master_password

    def authorization(browser):
        browser.find_element_by_css_selector('[autocomplete="username"]').send_keys('sysadmin')
        browser.find_element_by_css_selector('[autocomplete="current-password"]').send_keys(master_password) 
        button = browser.find_element_by_css_selector("[type='submit']")
        button.click()
        file_name = datetime.now().strftime("%y%m%d_%H%M%S.png ")
        screenshot_path = os.path.join("/DockerPython/screenshots/", file_name)
        browser.get_screenshot_as_file(screenshot_path)

    def test_access_eljur(self):


        driver = Testeljur.driver
        driver.get("https://api-test.eljur.ru/authorize")
        assert driver.current_url == "https://api-test.eljur.ru/authorize"
        

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()