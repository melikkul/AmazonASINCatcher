from selenium.webdriver.common.by import By
from category_info import category_find
from find_element import find
from zip_code_checker import check
import time
from selenium.webdriver.common.action_chains import ActionChains

seller_id = 'A1DXN92KCKEQV4'
def asin_finder(driver):
    found_categories = category_find(driver)
    
    for category_name, content_id in found_categories:
        print(f"'{category_name}' kategorisi bulundu.")
        
        while True:
            # Hedef pencerenin açık olduğunu kontrol edin
            if driver.current_window_handle:
                element = find(driver, By.XPATH, f'//*[@id="{content_id}"]/span/a', 10)
                if element is not None:
                    #time.sleep(2)
                    element.click()
                    #time.sleep(3)
                    while True:
                        asins = driver.find_elements(By.XPATH, '//div[@data-asin]')
                        
                        for asin in asins:    
                            data_asin = asin.get_attribute('data-asin')
                            if data_asin:
                                return data_asin
                        
                        next_button = find(driver, By.XPATH, "//a[contains(@class, 's-pagination-next')]")
                        continue_button = find(driver, By.XPATH, "//a[contains(@class, 's-pagination-next s-pagination-disabled')]")
                        if next_button:
                            #time.sleep(2)
                            ActionChains(driver).move_to_element(next_button).click().perform()
                            # Yeni sayfanın yüklenmesini bekleyin
                            #time.sleep(3)
                        elif continue_button:
                            break
                        else:
                            print('Son sayfaya ulaşıldı')
                            
                            break
                else:
                    print('Element bulunamadı.')
                    break
            else:
                print('Hedef pencere kapalı.')
                # WebDriver'ı yeniden başlatın veya başka bir eylem yapın
                break
        driver.get("https://www.amazon.com/s?rh=p_6%3A" + seller_id)
        check(driver)
