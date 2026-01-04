# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Optional for CI or faster tests
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Auto-download driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
