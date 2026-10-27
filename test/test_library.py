import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver= webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()

def test_home_page_loads_with_stats(driver):
    driver.get("http://localhost:5001/")

    assert "Library" in driver.page_source

    
    page = driver.page_source
    assert "Total" in page
    assert "Available" in page
    assert "Issued" in page

def test_add_book_and_view(driver):
    
    driver.get("http://localhost:5001/add")

    driver.find_element(By.NAME, "title").send_keys("Selenium Test Book")
    driver.find_element(By.NAME, "author").send_keys("Test Author")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    assert "/books" in driver.current_url

    assert "Selenium Test Book" in driver.page_source
    assert "Test Author" in driver.page_source