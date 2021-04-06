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

        img_slidr = driver.find_element_by_link_text("Image Slider Manager")
        img_slidr.click()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,500)")

        img_rec = driver.find_element_by_link_text("Add Record")
        img_rec.click()
        time.sleep(2)

        bg_img = driver.find_element_by_id("imgPhotoId")
        bg_img.send_keys("D:\download_imag.jpg")

        #img_act = driver.find_element_by_id("imgStatus")
        #img_act.click()

        img_save = driver.find_element_by_id("jqSubmitForm")
        img_save.click()

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
