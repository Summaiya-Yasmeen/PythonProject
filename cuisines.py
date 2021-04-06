from selenium import webdriver
import time
import unittest

class title(unittest.TestCase):
    def test(self):
        driver = webdriver.Chrome(executable_path="C:\\Python\\chromedriver_win32\\chromedriver.exe")
        url = "https://www.demo.iscripts.com/netmenus-enterprise/cms"
        driver.get(url)
        print("HURRAY.... Browser was opened")
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

        cuisine = driver.find_element_by_link_text("Cuisines")
        cuisine.click()

        add_recrd = driver.find_element_by_link_text("Add Record")
        add_recrd.click()

        tag = driver.find_element_by_id("tag_name")
        tag.send_keys("Indian")

        cuisine_img = driver.find_element_by_id("tag_image")
        cuisine_img.send_keys("D:\download_img.jpg")
        time.sleep(2)

        cuisine_save = driver.find_element_by_id("jqSubmitForm")
        cuisine_save.click()

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
