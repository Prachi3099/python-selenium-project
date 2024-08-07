import logging

import pytest
import inspect

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        fileHandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger


    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByTxt(self,locator,text):
        sel=Select(locator)
        sel.select_by_visible_text(text)