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

        offr = driver.find_element_by_link_text("Offers")
        offr.click()

        driver.execute_script("window.scrollBy(0,500)")

        add_ofrrec = driver.find_element_by_css_selector("a[class='addrecord btn btn-info']")
        add_ofrrec.click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,500)")

        ofr_name = driver.find_element_by_id("offer_name")
        ofr_name.send_keys("Diwali special offer")
        time.sleep(2)

        offr_value = driver.find_element_by_id("offer_value")
        offr_value.send_keys("50%")

        ofr_img = driver.find_element_by_id("offer_image")
        ofr_img.send_keys("D:\download_img.png")

        ofr_save = driver.find_element_by_id("jqSubmitForm")
        ofr_save.click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
