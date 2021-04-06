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

        mail_res = driver.find_element_by_link_text("Mail Restaurants")
        mail_res.click()
        time.sleep(1)

        mlres_to = driver.find_element_by_xpath("//option[@value='12']")
        mlres_to.click()

        ml_sub = driver.find_element_by_id("subject")
        ml_sub.send_keys("subscription fee")
        time.sleep(2)

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Rich text editor, content1, press ALT 0 for help.']"))
        ml_contnt = driver.find_element_by_xpath("//html")
        ml_contnt.send_keys("pay your subscription fee")
        driver.switch_to.default_content()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,500)")

        ml_save = driver.find_element_by_name("submitBtn")
        ml_save.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
