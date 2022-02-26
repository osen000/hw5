from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_item_post(driver):
    """Поиск элементов"""
    driver.get(driver.base_url + f"index.php?route=product/product&path=20&product_id=42&sort=p.sort_order&order=ASC")
    wait = WebDriverWait(driver, 5)
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Desktops")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='product-product']//a[text()='Apple Cinema 30\"']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='image-additional']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='thumbnails']//img[@title='Apple Cinema 30\"']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='nav nav-tabs']//a[text()='Description']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='nav nav-tabs']//a[text()='Specification']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='nav nav-tabs']//a[text()='Reviews (0)']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='fa fa-heart']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='fa fa-exchange']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']//*[text()='Apple Cinema 30\"']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='col-sm-4']//*[text()='Brand: ']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='col-sm-4']//h2[text()='$110.00']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='product']//*[text()='Available Options']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='product']//*[text()='Radio']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='product']//*[text()='Checkbox']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='input-option208']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-option217']>[value='3']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-option209']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='button-upload222']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-option219']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-option221']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-option220']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='input-quantity']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='button-cart' and text()='Add to Cart']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='alert alert-info'][text()=' This product has a "
                                                           "minimum quantity of 2']")))
