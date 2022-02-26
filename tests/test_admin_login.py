from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_admin_login(driver):
    """Поиск элементов"""
    driver.get(driver.base_url + f"admin")
    wait = WebDriverWait(driver, 5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[title='OpenCart']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='panel-title']>[class='fa fa-lock']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[for='input-username']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class='fa fa-user']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[for='input-password']")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='input-group-addon']/*[@class='fa fa-lock']")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Forgotten Password")))
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[type='submit']")))
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "OpenCart")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='footer' and text()=' © 2009-2022 All Rights "
                                                           "Reserved.']")))
