from selenium.webdriver.common.by import By
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

        restaurant = driver.find_element_by_link_text("Restaurants")
        restaurant.click()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,500)")

        #res_rec = driver.find_element_by_link_text("Add Record")
        #res_rec.click()

        add = driver.find_element(By.XPATH, "//a[normalize-space()='Add Record']")
        add.click()
        time.sleep(2)

        restaurant_name = driver.find_element_by_id("venue_name")
        restaurant_name.send_keys("THE FOOD VILLA")

        description = driver.find_element_by_id("venue_description")
        description.send_keys("Authentic Indian food, freshly prepared by one of our experienced chiefs")


        address = driver.find_element_by_id("venue_address_by_user")
        address.send_keys("Opposite kothari bhavan, New jevargi road, godutai nagar, gulbarga")


        zip = driver.find_element_by_id("zip_code")
        zip.send_keys("585104")
        time.sleep(2)


        phone = driver.find_element_by_id("phone")
        phone.send_keys("720456784")


        site_url = driver.find_element_by_id("site_url")
        site_url.send_keys("thefoodvilla4ugmail.com")


        cuisines = driver.find_element_by_id("tags")
        cuisines.send_keys("Indian")
        time.sleep(2)


        payment_option = driver.find_element_by_xpath("//input[@value='0']")
        payment_option.click()


        paymentoption = driver.find_element_by_xpath("//label[2]//input[1]")
        paymentoption.click()


        home_delivery = driver.find_element_by_id("delivery")
        home_delivery.click()


        restaurant_owner = driver.find_element_by_id("created_by")
        option = Select(restaurant_owner)
        option.select_by_visible_text("Issac Mathew")


        maneger = driver.find_element_by_id("store_manager")
        maneger.send_keys("Sameer")

        maneger_email = driver.find_element_by_id("store_manager_email")
        maneger_email.send_keys("sameer123@gamil.com")

        min_odr_amt = driver.find_element_by_id("min_order_amount")
        min_odr_amt.send_keys("100")


        cost_frto_prsn = driver.find_element_by_id("cost_for_two_person")
        cost_frto_prsn.send_keys("200")

        sales_tax = driver.find_element_by_id("sales_tax")
        sales_tax.send_keys("2")
        time.sleep(2)

        delivery_feetype = driver.find_element_by_id("delivery_fee_type")
        option = Select(delivery_feetype)
        option.select_by_visible_text("Flat")

        delivery_fee = driver.find_element_by_id("delivery_fee")
        delivery_fee.send_keys("2")

        delivery_area = driver.find_element_by_id("delivery_area_desc")
        delivery_area.send_keys("plot no 137, svp gda layout sangtrashwadi gulbarga")

        rate_commission = driver.find_element_by_id("commission")
        rate_commission.send_keys("50")

        save = driver.find_element_by_name("submit")
        save.click()
        time.sleep(2)

        offr = driver.find_element_by_link_text("Offers")
        offr.click()

        driver.execute_script("window.scrollBy(0,700)")
        time.sleep(2)

        addrec = driver.find_element_by_xpath("//a[normalize-space()='Add Record']")
        addrec.click()
        time.sleep(2)

        ofr_name = driver.find_element_by_xpath("//input[@id='offer_name']")
        ofr_name.send_keys("Diwali special offer")
        time.sleep(2)

        offr_value = driver.find_element_by_id("offer_value")
        offr_value.send_keys("50%")

        ofr_img = driver.find_element_by_id("offer_image")
        ofr_img.send_keys("D:\download_img.png")

        ofr_save = driver.find_element_by_id("jqSubmitForm")
        ofr_save.click()
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

        cuisine = driver.find_element_by_link_text("Cuisines")
        cuisine.click()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,500)")

        add_recrd = driver.find_element_by_link_text("Add Record")
        add_recrd.click()
        time.sleep(2)

        tag = driver.find_element_by_id("tag_name")
        tag.send_keys("Indian")

        cuisine_img = driver.find_element_by_id("tag_image")
        cuisine_img.send_keys("D:\download_img.jpg")
        time.sleep(2)

        cuisine_save = driver.find_element_by_id("jqSubmitForm")
        cuisine_save.click()
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

        img_save = driver.find_element_by_id("jqSubmitForm")
        img_save.click()
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

        fd_save = driver.find_element_by_id("jqSubmitForm")
        fd_save.click()
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

        driver.switch_to.frame(
        driver.find_element(By.XPATH, "//iframe[@title='Rich text editor, content, press ALT 0 for help.']"))
        mail_content = driver.find_element(By.XPATH, "//html")
        mail_content.send_keys("Demo")
        driver.switch_to.default_content()

        driver.execute_script("window.scrollBy(0,500)")

        mail = driver.find_element_by_xpath("//input[@name='submitBtn']")
        mail.click()
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

        driver.switch_to.frame(
        driver.find_element(By.XPATH, "//iframe[@title='Rich text editor, content1, press ALT 0 for help.']"))
        ml_contnt = driver.find_element_by_xpath("//html")
        ml_contnt.send_keys("pay your subscription fee")
        driver.switch_to.default_content()
        time.sleep(2)

        driver.execute_script("window.scrollBy(0,500)")

        ml_save = driver.find_element_by_name("submitBtn")
        ml_save.click()
        time.sleep(2)

        logout = driver.find_element_by_class_name("icon_logout")
        logout.click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
