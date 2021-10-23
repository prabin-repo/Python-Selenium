import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
#@pytest.mark.usefixtures("setup")
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.Homepage import HomePage
from PageObjects.shopPage import shopPage
from utilities.BaseClass import BaseClass, getLogger


class Test(BaseClass):

    def test_TC01(self):
        log = getLogger(self)
        homePage = HomePage(self.driver)
        homePage.shop_items().click()

        shoppage = shopPage(self.driver)

        checkoutPage = CheckoutPage(self.driver)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Blackberry")))

        #self.driver.find_element_by_xpath("//a[text()='Nokia Edge']/following::button").click()
        shoppage.items().click()
        #self.driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
        shoppage.checkout().click()
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        checkoutPage.cart_checkout().click()
        self.driver.find_element_by_id("country").send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element_by_link_text("India").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        text_msg = self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
        log.info(text_msg)
        assert "Success! Thank yodfdf!" in text_msg
        self.driver.get_screenshot_as_file("Success.png")



