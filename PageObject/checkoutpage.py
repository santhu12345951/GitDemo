from selenium.webdriver.common.by import By

from PageObject.ConfirmPage import ConfirmPage


class CheckOutPage:
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    AddProduct = (By.XPATH, "div/button")
    BlackBerry = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    Confirm = (By.CSS_SELECTOR, "button[class*='btn-success']")


    def __init__(self, driver):

        self.driver = driver





    def mobileelements(self):

        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def mobilename(self):

        return self.driver.find_element(*CheckOutPage.productName)

    def AddMobile(self):

        return self.driver.find_element(*CheckOutPage.AddProduct)

    def AddBlackBerry(self):

        return self.driver.find_element(*CheckOutPage.BlackBerry)

    def ConfirmCheckOut(self):


         self.driver.find_element(*CheckOutPage.Confirm).click()
         return ConfirmPage(self.driver)













