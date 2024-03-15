from selenium.webdriver.common.by import By
from find_element import find

def check(driver):
    #/html/body/div[1]/header/div/div[1]/div[1]/div[2]/span/a/div[2]/span[2]
    
    zip_button = find(driver, By.XPATH, '/html/body/div[1]/header/div/div[1]/div[1]/div[2]/span/a/div[2]/span[2]')
    if "New York 10001" not in zip_button.text:
        zip_button.click()
        enter_zip_code = find(driver, By.ID, 'GLUXZipUpdateInput')
        enter_zip_code.send_keys("10001")
        
        apply_button = find(driver, By.ID, 'GLUXZipUpdate')
        apply_button.click()

        continue_button = find(driver, By.XPATH, '/html/body/div[6]/div/div/div[2]/span/span')
        continue_button.click()
    else:
        print("Zip code already entered")
    
