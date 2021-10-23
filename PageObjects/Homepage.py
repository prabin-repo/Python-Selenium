from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop_link = (By.LINK_TEXT, "Shop")
    Name_txt = (By.NAME, "name")
    Email_txt = (By.NAME, "email")
    pwd_txt = (By.ID, "exampleInputPassword1")
    chkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop_link)

    def name(self):
        return self.driver.find_element(*HomePage.Name_txt)

    def email(self):
        return self.driver.find_element(*HomePage.Email_txt)

    def password(self):
        return self.driver.find_element(*HomePage.pwd_txt)

    def checkbox(self):
        return self.driver.find_element(*HomePage.chkbox)

    def gender_check(self):
        return self.driver.find_element(*HomePage.gender)

    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)