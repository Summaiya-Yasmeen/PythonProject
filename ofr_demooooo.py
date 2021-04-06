from selenium import webdriver
import time
import unittest

class title(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:\\Python\\chromedriver_win32\\chromedriver.exe")
        url = "https://www.demo.iscripts.com/netmenus-enterprise/cms"
        driver.get(url)
        driver.maximize_window()

        name = driver.find_element_by_id("username")
        name.send_keys("admin")

        password = driver.find_element_by_id("inputPassword")
        password.send_keys("admin")

        lg = driver.find_element_by_name("submit")
        lg.click()

        driver.execute_script("window.scrollBy(0,500)")

        offr = driver.find_element_by_link_text("Offers")
        offr.click()

        driver.execute_script("window.scrollBy(0,700)")
        time.sleep(2)

        addrec = driver.find_element_by_xpath("//a[normalize-space()='Add Record']")
        addrec.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
