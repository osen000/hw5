from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_catalog(driver):
    """Поиск элементов"""
    driver.get(driver.base_url + f"index.php?route=product/category&path=20")
    wait = WebDriverWait(driver, 5)
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Desktops")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='fa fa-home']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='product-category']//a[text()='Desktops']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']//h2[text()='Desktops']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "img[src$='.jpg'][title='Desktops']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']/h3[text()='Refine Search']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']//a[text()='PC (0)']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']//a[text()='Mac (1)']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='fa fa-th-list']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='fa fa-th']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[id='compare-total']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "label[for='input-sort']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "select[id='input-sort']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='input-sort']/option[text()='Default']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']//label[text()='Show:']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='input-limit']/option[text()='15']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='product-layout product-grid col-lg-4 col-md-4 "
                                                           "col-sm-6 col-xs-12']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']//div[text()='Showing 1 to 12 of 12 (1 "
                                                           "Pages)']")))
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "list-group")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[text()='Desktops (13)']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='list-group-item']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "img[src$='.jpg'][alt='HP Banner']")))
