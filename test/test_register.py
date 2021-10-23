from PageObjects.Homepage import HomePage
from utilities.BaseClass import BaseClass


class Registration(BaseClass):
    def test_fillform(self):
        homepage = HomePage(self.driver)
        homepage.name().send_keys("Prabin")
        homepage.email().send_keys("Prabin.behera@gmail.com")
        homepage.password().send_keys("Prabin@123")
