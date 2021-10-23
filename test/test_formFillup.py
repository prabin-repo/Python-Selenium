import time

import pytest

from PageObjects.Homepage import HomePage
from TestData.HomepageData import HomepageData
from utilities.BaseClass import BaseClass, selectOptionByText, getLogger
from selenium.webdriver.support.select import Select


class TestHomePage(BaseClass):
    def test_formSubmission(self, getdata):
        homepage = HomePage(self.driver)
        log = getLogger(self)
        homepage.name().send_keys(getdata["firstname"])

        homepage.email().send_keys(getdata["email"])
        homepage.password().send_keys(getdata["password"])
        homepage.checkbox().click()
        selectOptionByText(self, homepage.gender_check(), getdata["gender"])
        homepage.submit_form().click()
        message = homepage.getSuccessMessage().text
        log.info(message)
        print(message)
        time.sleep(3)
        assert "success" in message
        self.driver.refresh()


    @pytest.fixture(params= HomepageData.test_homepage_data)
    def getdata(self, request):
        return request.param
