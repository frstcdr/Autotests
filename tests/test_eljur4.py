import os

from datetime import datetime

from selenium import webdriver


class TestGoogle:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub",
            options=webdriver.ChromeOptions(),
        )

    def test_access_eljur(self):


        driver = TestGoogle.driver

        file_name = datetime.now().strftime("%y%m%d_%H%M%S.png ")
        screenshot_path = os.path.join("/DockerPython/screenshots/", file_name)

        driver.get("https://api-test.eljur.ru/authorize")
        driver.get_screenshot_as_file(screenshot_path)

        assert driver.current_url == "https://api-test.eljur.ru/authorize"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()