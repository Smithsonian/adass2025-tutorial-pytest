import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# -------------------------------
# Selenium Setup
# -------------------------------


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    # options.add_argument("--ignore-certificate-errors") # Only for local testing
    mydriver = webdriver.Chrome(options=options)
    yield mydriver
    mydriver.quit()  # Must close browser


# Exercise
# Navigate to "https://example.com" and assert "Example Domain"
# is in the driver's title property
# Hint:  dir(driver) to show different properties and methods
def test_title_example_com(driver):
    pass


# Exercise
# Navigate to "https://chandra.harvard.edu/photo"
# Apply a max 10 second wait condition until "title" is located By.CLASS_NAME
# from any element
# Assert the text 'Chandra' occurs somewhere in the page source content.
# Hint: WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located_by((By.<something>, <thingtofind>))
# Hint: EC.presence_of_element_located()
# Hint: By.CLASS_NAME
def test_wait_for_element(driver):
    pass


# Exercise
# Navigate to "https://cxc.cfa.harvard.edu/cda/"
# Assert an element with ID "upcoming" exists
# Assert a div element that contains text "Welcome to the Chandra Data Archive" exists
# Assert that both elements are the same.
def test_locate_elements(driver):
    pass


# Exercise
# Navigate to "https://cda.cfa.harvard.edu/chaser"
# Find the search by obsid form text box
# Clear any pre-existing text
# Enter obsid 1234
# Click Search
# Use a Webdriver wait with 5 second timeout to verify:
# (a) the new page title is 'Chandra Data Archive: Search Results'
# (b) the Search Results page returns obsid 1234
def test_chaser(driver):
    pass
