from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import unittest

class title(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:\\Python\\chromedriver_win32\\chromedriver.exe")
        url = "https://www.demo.iscripts.com/netmenus-enterprise/cms"
        driver.get(url)
        driver.maximize_window()
        time.sleep(2)

        name = driver.find_element_by_id("username")
        name.send_keys("admin")

        password = driver.find_element_by_id("inputPassword")
        password.send_keys("admin")

        lg = driver.find_element_by_name("submit")
        lg.click()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,500)")

        mail_usr = driver.find_element_by_link_text("Mail Users")
        mail_usr.click()
        time.sleep(2)


        mail_to = driver.find_element_by_xpath("//option[@value='57']")
        mail_to.click()

        sub = driver.find_element_by_id("subject")
        sub.send_keys("Subscription fee")
        time.sleep(2)

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Rich text editor, content, press ALT 0 for help.']"))
        mail_content = driver.find_element(By.XPATH, "//html")
        mail_content.send_keys("Demo")
        driver.switch_to.default_content()

        driver.execute_script("window.scrollBy(0,500)")

        mail = driver.find_element_by_xpath("//input[@name='submitBtn']")
        mail.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
