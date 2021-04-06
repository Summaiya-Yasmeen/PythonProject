from selenium import webdriver
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

        fd_itms = driver.find_element_by_link_text("Food Items")
        fd_itms.click()

        driver.execute_script("window.scrollBy(0,500)")

        add_record = driver.find_element_by_xpath("//a[normalize-space()='Add Record']")
        add_record.click()
        time.sleep(2)

        food_items = driver.find_element_by_id("product_name")
        food_items.send_keys("Burger")

        topping = driver.find_element_by_id("is_topping")
        topping.click()

        publish = driver.find_element_by_id("published")
        publish.click()

        save = driver.find_element_by_name("submit")
        save.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
