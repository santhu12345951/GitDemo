from selenium.webdriver.common.by import By

from PageObject.checkoutpage import CheckOutPage


class HomePage:
    def __init__(self, driver):

        self.driver = driver


    shop=  (By.CSS_SELECTOR, "a[href*=shop]")

    name = (By.CSS_SELECTOR, "input[name='name']")

    email = (By.NAME, "email")

    checkbox = (By.ID, "exampleCheck1")

    dropdown = (By.ID, "exampleFormControlSelect1")

    submit = (By.XPATH, "//input[@type='submit']")

    classname = (By.CLASS_NAME, "alert-success")










    def shopItems(self):



        self.driver.find_element(*HomePage.shop).click()
        checkoutpage= CheckOutPage(self.driver)
        return checkoutpage

        #self.driver.find_element_by_css_selector("a[href*=shop]").click()

    def getName(self):

        return self.driver.find_element(*HomePage.name)


    def getEmail(self):

        return self.driver.find_element(*HomePage.email)

    def checkBox(self):

        return self.driver.find_element(*HomePage.checkbox)

    def getdropdown(self):

        return self.driver.find_element(*HomePage.dropdown)

    def clickSubmit(self):

        return self.driver.find_element(*HomePage.submit)

    def successMessage(self):

        return self.driver.find_element(*HomePage.classname)


