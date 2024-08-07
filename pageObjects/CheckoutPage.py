from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self,driver):
        self.driver=driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    #button=(By.XPATH, "div/button")
    checkout_btn1=(By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_btn2=(By.XPATH, "//button[@class='btn btn-success']")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCheckoutBtn1(self):
        return self.driver.find_element(*CheckoutPage.checkout_btn1)

    def getAddToCart(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckoutBtn2(self):
        self.driver.find_element(*CheckoutPage.checkout_btn2).click()
        confirmPage=ConfirmPage(self.driver)
        return confirmPage


