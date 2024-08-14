import os
from datetime import datetime

import pytest
import pytest_html
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    chrome_options=Options()
    chrome_options.add_argument("--disable-headless")
    
    if browser_name=="chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    elif browser_name=="edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://rahulshettyacademy.com/angularpractice/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            driver = item.cls.driver
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras

def pytest_html_report_title(report):
    report.title="Python Selenium Automation Report"
