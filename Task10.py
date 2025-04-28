import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup for Selenium WebDriver
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Positive Test Case: Check if the Title matches after login
def test_check_title(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")  # Sauce Demo URL
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    title = driver.title
    assert title == "Swag Labs"  # Expected Title after login

# Negative Test Case: Check if the Title matches an incorrect value
def test_check_invalid_title(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")  # Sauce Demo URL
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    title = driver.title
    assert title != "Incorrect Title"  # Test should fail

# Positive Test Case: Check the current URL of the Home Page before login
def test_check_home_page_url(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")  # Sauce Demo URL
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://www.saucedemo.com/"  # Home page URL

# Negative Test Case: Check the current URL (this should fail)
def test_check_invalid_home_page_url(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")  # Sauce Demo URL
    time.sleep(2)
    current_url = driver.current_url
    assert current_url != "https://www.invalid-url.com"  # Test should fail

# Positive Test Case: Check the dashboard URL after login
def test_check_dashboard_url_after_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")  # Sauce Demo URL
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    dashboard_url = driver.current_url
    assert dashboard_url == "https://www.saucedemo.com/inventory.html"  # Dashboard URL after login

# Negative Test Case: Check if the dashboard URL is incorrect after login
def test_check_invalid_dashboard_url_after_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")  # Sauce Demo URL
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    dashboard_url = driver.current_url
    assert dashboard_url != "https://www.saucedemo.com/inventory.html"  # Test should fail for invalid login

def test_page_extract(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")  # Sauce Demo URL
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    page_content = driver.page_source                          # Save content to a text file
    with open("webpage_task_qq.txt", "w", encoding="utf-8") as f:f.write(page_content)
    print("Webpage contents saved successfully to 'webpage_task_qq.txt'")
