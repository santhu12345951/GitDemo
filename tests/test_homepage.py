import pytest
from selenium import webdriver
#Through selenium we should execute executable file
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import InstantClass


class TestHomePage(InstantClass):


    def testformsubmission(self,getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info("values5")
        log.info("the firstname is"+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.checkBox().click()
        self.selectoptionbyText(homepage.getdropdown(), getData["Gender"])
        homepage.clickSubmit().click()
        message = homepage.successMessage().text
        assert "success" in message
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.gettestdata("TestCase2"))
    def getData(self, request):
        return request.param



