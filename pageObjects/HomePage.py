from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    shop=(By.CSS_SELECTOR, " a[href*='shop']")
    name=(By.CSS_SELECTOR,"[name='name']")
    email=(By.NAME,"email")
    chkBox=(By.ID,"exampleCheck1")
    gender=(By.ID,"exampleFormControlSelect1")
    submit=(By.XPATH,"//input[@value='Submit']")
    alert_Text=(By.CSS_SELECTOR,"[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage=CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def checkBox(self):
        return self.driver.find_element(*HomePage.chkBox)

    def genderSelect(self):
        return self.driver.find_element(*HomePage.gender)

    def submitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getText(self):
        return self.driver.find_element(*HomePage.alert_Text)
