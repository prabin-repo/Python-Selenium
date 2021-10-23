from selenium.webdriver.common.by import By


class shopPage:
    def __init__(self,driver):
        self.driver = driver

    Item_Nokia = (By.XPATH, "//a[text()='Nokia Edge']/following::button")
    CheckOut = (By.XPATH,"//a[contains(text(),'Checkout')]")

    def items(self):
        return self.driver.find_element(*shopPage.Item_Nokia)

    def checkout(self):
        return self.driver.find_element(*shopPage.CheckOut)

