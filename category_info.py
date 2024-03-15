from find_element import find
from selenium.webdriver.common.by import By
import re
import time
from zip_code_checker import check

categories = {
        "Appliances":"n/2619525011",
        "Arts, Crafts & Sewing": "n/2617941011",
        "Automotive": "n/15684181",
        "Baby Product": "n/165796011",
        "Beauty & Personal Care": "n/3760911",
        "Books": "n/283155",
        "CDs & Vinyl": "n/5174",
        "Cell Phones & Accessories": "n/2335752011",
        "Clothing, Shoes & Jewelry": "n/7141123011",
        "Electronics": "n/172282",
        "Everything Else": "n/10272111",
        "Grocery & Gourmet Food": "n/16310101",
        "Health & Household": "n/3760901",
        "Home & Business Services": "n/8098158011",
        "Home & Kitchen": "n/1055398",
        "Industrial & Scientific": "n/16310091",
        "Musical Instruments": "n/11091801",
        "Office Products": "n/1064954",
        "Patio, Lawn & Garden": "n/2972638011",
        "Pet Supplies": "n/2619533011",
        "Sports & Outdoors": "n/3375251",
        "Tools & Home Improvement": "n/228013",
        "Toys & Games": "n/165793011"
    }

found_categories = []
def category_find(driver):

    count = 0
    for category_name, content_id in categories.items():
        element = find(driver, By.XPATH, f'//*[@id="{content_id}"]',2)
        if element is not None:
            #print(f"'{category_name}' kategorisi bulundu.")
            found_categories.append((category_name, content_id))
            count += 1
        else:
            #print(f"'{category_name}' kategorisi bulunamadı.")
            break
    
    #print(f"{count} kategoriler bulundu.")
    
    return found_categories

def product_count(driver):
    count_products = 0
    for category_name, content_id in found_categories:
        #print(f"Kategori Adı: {category_name}, İçerik Kimliği: {content_id}")
        element = find(driver, By.XPATH, f'//*[@id="{content_id}"]/span/a')
        
        #print(element.text)
        
        if element is not None:
            time.sleep(2)
            element.click()
            text = find(driver, By.XPATH, '//*[@id="search"]/span[2]/div/h1/div/div[1]/div/div/span')
            match = re.search(r'\b\d+\b(?=\D*$)', text.text)

            if match:
                number = match.group()
                print(type(number))
                if number == '000':
                    match2 = re.finditer(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b', text.text)
                    count = 0
                    for m in match2:
                        count += 1
                        if count == 3:
                            num = m.group()
                            count_products += int(num.replace(",", ""))
                            #print("Bulunan sayı:", num)
                else:
                    count_products += int(number)
                    #print("Bulunan sayı:", number)
                driver.back()
                time.sleep(2)
            else:
                break
                #print("Sayı bulunamadı.")
            check(driver)
        else:
            #print(f"'{category_name}' kategorisi bulunamadı.")
            break
    
    return count_products
            
            