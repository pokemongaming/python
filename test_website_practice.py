import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url="https://practicetestautomation.com/practice-test-login/"
base_url1="https://practicetestautomation.com/logged-in-successfully/"

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.quit()

def login_and_get_error(driver,username,password):
    wait=WebDriverWait(driver,30)
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"submit").click()

def error(driver):   
    wait=WebDriverWait(driver,30) 
    errorMessage=wait.until(EC.visibility_of_element_located((By.ID,"error")))
    return errorMessage.text

def test_valid(driver):
    login_and_get_error(driver,"student","Password123")
    url=driver.current_url
    assert url==base_url1
    text1=driver.find_element(By.CSS_SELECTOR,".has-text-align-center.wp-block-paragraph").text
    print(text1)
    assert "Congratulations" in text1 or "successfully logged in" in text1
    assert text1=="Congratulations student. You successfully logged in!"
    assert driver.find_element(By.LINK_TEXT,"Log out").is_displayed()
    driver.find_element(By.LINK_TEXT,"Log out").click()

def test_invalid_username(driver):
    login_and_get_error(driver,"invalidUsername","Password123")
    errorMessage=error(driver)
    assert errorMessage=="Your username is invalid!"

def test_invalid_password(driver):
    login_and_get_error(driver,"student","invalidPassword")
    errorMessage=error(driver)
    assert errorMessage=="Your password is invalid!"
    