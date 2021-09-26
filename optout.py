from optout_utils import selenium_wrapper, optout_url

def main():
    browser = "chrome"
    first_name = "yvon"
    last_name = "nimda"
    email_address = "yvon.nimda@gmail.com"
    student_id = "12345678"
    credits = "15"
    schedule_image = ""
    student_card_image = ""

    driver = selenium_wrapper.instantiate_webdriver(browser)

    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button")
    for i in range(5):
        selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure/form/div[1]/div[1]/div[2]/textarea", first_name)
    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure/form/div[2]/div[1]/div[2]/textarea", last_name)
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure/form/div[1]/div[1]/div[2]/span/input", email_address)
    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure/form/div[2]/div[1]/div[2]/span/input", email_address)
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure/form/div[1]/div[1]/div[3]/input", student_id)
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure/form/div[1]/div[1]/div[2]/input", credits)
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

    selenium_wrapper.click_by_xpath(driver, "//*[@id='richEditor']/div[1]/div/div/div/figure/form/div[1]/div[1]/div[2]/div/div/div[3]") # eventually add a selection for all faculties this is hardcoded
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

    # http://allselenium.info/file-upload-using-python-selenium-webdriver/
    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure[1]/form/div[1]/div[1]/div[3]/div/input", schedule_image)
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

    selenium_wrapper.send_keys_by_xpath(driver, "/html/body/div/div/div[4]/div[1]/div/div/div/figure[1]/form/div[1]/div[1]/div[3]/div/input", student_card_image)
    selenium_wrapper.click_by_xpath(driver, "/html/body/div/div/div[4]/div[2]/button[2]")

if __name__ == "__main__":
    main()