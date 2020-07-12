from selenium import webdriver
#Through selenium we should execute executable file
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pytest

from PageObject.ConfirmPage import ConfirmPage
from PageObject.HomePage import HomePage
from PageObject.checkoutpage import CheckOutPage
from utilities.BaseClass import InstantClass


class TestOne(InstantClass):

    def test_e2e(self):

        log= self.getlogger()

        homePage = HomePage(self.driver)
        log.info("get all the items of mobiles")
        log.info("getall items of all mobiles")
        log.info("print all demos")
        log.info("values1")
        log.info("values2")
        log.info("values3")
        log.info("values4")
        checkoutPageObject = homePage.shopItems()
        products = checkoutPageObject.mobileelements()
        for product in products:
            productscheck= CheckOutPage(product)
            productname = productscheck.mobilename().text
            log.info(productname)
            if (productname == "Blackberry"):

                productscheck.AddMobile().click()
                break;

        checkoutPageObject.AddBlackBerry().click()
        ConfirmOrder = checkoutPageObject.ConfirmCheckOut()
        log.info("enter country Name as India ")
        ConfirmOrder.CountryName().send_keys("ind")
        self.VerifyLinkPresence("India")
        ConfirmOrder.ProvideCountry().click()
        ConfirmOrder.AcceptConditions().click()
        ConfirmOrder.Purchase().click()
        textMatch= ConfirmOrder.Alert().text
        #print(textMatch)
        #log.info("Text received from application is "+textMatch)
        assert "Success!" in textMatch
        # driver.get_screenshot_as_file("success.png")













