import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from urllib3.exceptions import MaxRetryError, NewConnectionError
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from datetime import datetime

@pytest.fixture(scope='function')
def setup(request):
    global driver
    url = "https://api-test.eljur.ru/"
    try:
        driver = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub",
            options=webdriver.ChromeOptions(),
        )
    except MaxRetryError or NewConnectionError:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = False
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://sprint.moravis.com/run/val/adchef/a0bfkgb"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname("./screenshots/")
            file_name = datetime.now().strftime("%y%m%d_%H%M%S.png")
            #file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src ="../screenshots/%s" alt="screenshot" style="width:300px; height:200px;" onclick ="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Report By Tests"