from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_main_page(driver):
    """Поиск элементов"""
    driver.get(driver.base_url)
    wait = WebDriverWait(driver, 5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='123456789']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='My Account']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Wish List (0)']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Shopping Cart']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='Checkout']")))
    wait.until(ec.visibility_of_element_located((By.ID, "search")))
    wait.until(ec.visibility_of_element_located((By.ID, "cart")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Your Store")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Desktops")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Laptops & Notebooks")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Components")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Tablets")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Software")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Phones & PDAs")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Cameras")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "MP3 Players")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "img[src$='.jpg'][alt='iPhone 6']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h3")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='content' and @class='col-sm-12']/h3[text()"
                                                           "='Featured']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='content']//i[@class='fa fa-shopping-cart']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='carousel0']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//footer//h5[text()='Information']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//footer//h5[text()='Customer Service']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//footer//h5[text()='Extras']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//footer//h5[text()='My Account']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//footer//h5[text()='My Account']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//footer//p[text()='Powered By ']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//footer//p[text()=' Your Store © 2022']")))
