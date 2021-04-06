from selenium import webdriver
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

        user = driver.find_element_by_link_text("Users")
        user.click()

        add_rec = driver.find_element_by_link_text("Add Record")
        add_rec.click()
        time.sleep(2)

        usr_name = driver.find_element_by_id("first_name")
        usr_name.send_keys("Ameen")

        usr_email = driver.find_element_by_id("email")
        usr_email.send_keys("admin@gmail.com")

        usr_password = driver.find_element_by_id("password")
        usr_password.send_keys("admin")
        time.sleep(2)

        usr_phne = driver.find_element_by_id("phone")
        usr_phne.send_keys("9845617845")

        usr_status = driver.find_element_by_id("status")
        option = Select(usr_status)
        option.select_by_value("active")

        usr_save = driver.find_element_by_name("submit")
        usr_save.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
