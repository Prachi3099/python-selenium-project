from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    delivery_location=(By.ID, "country")
    term_and_condition=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_btn=(By.CSS_SELECTOR, "[type='submit']")

    def getDeliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.delivery_location)

    def getTermandCondition(self):
        return self.driver.find_element(*ConfirmPage.term_and_condition)

    def submitButton(self):
        return self.driver.find_element(*ConfirmPage.submit_btn)


