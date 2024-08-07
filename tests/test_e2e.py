#chrome driver

#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    #anything in class use self parameter
    def test_e2e(self):
        log=self.getLogger()
        homePage = HomePage(self.driver)
        #  //a[contains(@href,'shop')]    a[href*='shop']
        checkoutPage=homePage.shopItems()
        log.info("getting all the cart items")
        # checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getProducts()
        i=-1
        for product in products:
            i=i+1
            #productName = product.find_element(By.XPATH, "div/h4/a").text
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                #product.find_element(By.XPATH, "div/button").click()
                checkoutPage.getAddToCart()[i].click()

        checkoutPage.getCheckoutBtn1().click()
        confirm = checkoutPage.getCheckoutBtn2()
        log.info("Entering country name as ind")
        confirm.getDeliveryLocation().send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        confirm.getTermandCondition().click()
        confirm.submitButton().click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("text received from the application is "+successText)
        assert "Success! Thank you!" in successText
