from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Path to your Chrome profile
profile_path = "/Users/sharvil/Library/Application Support/Google/Chrome/Profile 3"  # Ensure this path is correct

options = Options()
options.add_argument(f"user-data-dir={profile_path}")

try:
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open google.com
    driver.get("https://www.google.com")

    # Keep the browser open for 10 seconds
    time.sleep(10)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()