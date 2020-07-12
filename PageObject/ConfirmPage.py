from selenium.webdriver.common.by import By


class ConfirmPage:
    Country =(By.ID, "country")
    CountryLinkText= (By.LINK_TEXT, "India")
    CheckOutBox = (By.CSS_SELECTOR, "div[class*= 'checkbox-primary']")
    PurchaseProduct = (By.CSS_SELECTOR, "input[type='submit']")
    AlertMessage = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver= driver


    def CountryName(self):

        return self.driver.find_element(*ConfirmPage.Country)

    def ProvideCountry(self):

        return self.driver.find_element(*ConfirmPage.CountryLinkText)

    def AcceptConditions(self):

        return self.driver.find_element(*ConfirmPage.CheckOutBox)

    def Purchase(self):

        return self.driver.find_element(*ConfirmPage.PurchaseProduct)

    def Alert(self):

        return self.driver.find_element(*ConfirmPage.AlertMessage)


