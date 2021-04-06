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

        food_catgry = driver.find_element_by_link_text("Food Category")
        food_catgry.click()

        fd_rec = driver.find_element_by_link_text("Add Record")
        fd_rec.click()
        time.sleep(2)

        fd_tag = driver.find_element_by_id("tag_name")
        fd_tag.send_keys("Burger")

        fd_img = driver.find_element_by_id("tag_image")
        fd_img.send_keys("D:\download_imag.jpg")

        #fd_act = driver.find_element_by_id("published")
        #fd_act.click()

        fd_save = driver.find_element_by_id("jqSubmitForm")
        fd_save.click()


if __name__ == '__main__':
    unittest.main()
