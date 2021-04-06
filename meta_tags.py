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

        metatag = driver.find_element_by_link_text("Meta Tags")
        metatag.click()

        add_rec = driver.find_element_by_link_text("Add Record")
        add_rec.click()
        time.sleep(2)

        meta_title = driver.find_element_by_id("meta_title")
        meta_title.send_keys("netmenus")

        meta_keywd = driver.find_element_by_id("meta_keyword")
        meta_keywd.send_keys("restaurant,bar")

        meta_des = driver.find_element_by_id("meta_description")
        meta_des.send_keys("restaurant,bar")
        time.sleep(2)

        url = driver.find_element_by_id("url")
        url.send_keys("netmenus123@gmail.com")

        publish = driver.find_element_by_id("published")
        publish.click()

        save = driver.find_element_by_name("submit")
        save.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
