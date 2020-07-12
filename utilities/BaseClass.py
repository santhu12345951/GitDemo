import inspect
import logging

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class InstantClass:


    def getlogger(self):


        loggerName= inspect.stack()[1][3]
        logger= logging.getLogger(loggerName)
        formatter= logging.Formatter("%(asctime)s  :%(levelname)s  :%(name)s  :%(message)s")
        filehandler= logging.FileHandler('logfile.log')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)   #filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def VerifyLinkPresence(self, text):

        wait = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, text)))


    def selectoptionbyText(self,locator,text):

        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)