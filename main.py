from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from zip_code_checker import check
from find_element import find
from category_info import category_find, product_count
from search_asin import asin_finder
import pandas as pd

driver = webdriver.Chrome()

seller_id = 'A1DXN92KCKEQV4'
if seller_id:
    driver.get("https://www.amazon.com/s?rh=p_6%3A" + seller_id)
    while True:
        error_page = find(driver, By.XPATH, '/html/body/div/div/a/img')
        if error_page:
            driver.refresh()
        else:
            break
    check(driver)
    category_find(driver)
    product_count(driver)
    asin_finder(driver)
    print(asin_finder(driver))
