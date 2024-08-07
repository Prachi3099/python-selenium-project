import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homePage=HomePage(self.driver)
        log.info("first name is " + getData["name"])
        homePage.getName().send_keys(getData["name"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.checkBox().click()
        self.selectOptionByTxt(homePage.genderSelect(),getData["gender"])
        homePage.submitButton().click()
        alert_Text=homePage.getText().text
        assert ("Success" in alert_Text)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param

