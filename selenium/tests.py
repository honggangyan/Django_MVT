import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By  # Add this import
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# Selenium: A tool for web browser automation and testing.
# It allows programmatic interaction with web pages.

# WebDriver: The core component of Selenium.
# It provides a unified API to control different web browsers.

# This test suite uses Selenium WebDriver to automate 
# and test our counter application.


def file_uri(file_name):
    return pathlib.Path(os.path.abspath(file_name)).as_uri()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

class Webpagetest(unittest.TestCase):
    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")


    def test_increment(self):
        driver.get(file_uri("counter.html"))
        increment = driver.find_element(By.ID, "increment")
        increment.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "1")

    def test_decrement(self):
        driver.get(file_uri("counter.html"))
        decrement = driver.find_element(By.ID, "decrement")
        decrement.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increments(self):
        driver.get(file_uri("counter.html"))
        increment = driver.find_element(By.ID, "increment")
        for i in range(10):
            increment.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "10")

if __name__ == "__main__":
    unittest.main()
