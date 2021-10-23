from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver

    btn_checkout = (By.XPATH,"//button[@class='btn btn-success']")

    def cart_checkout(self):
        return self.driver.find_element(*CheckoutPage.btn_checkout)
