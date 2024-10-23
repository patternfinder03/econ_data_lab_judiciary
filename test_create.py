from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Function to create and store a new Chrome profile
def create_chrome_profile(profile_name="new_profile"):
    # Define the path to store Chrome profiles
    profile_dir = os.path.join(os.getcwd(), "chrome_profiles", profile_name)
    
    # Create the directory if it doesn't exist
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
    
    # Set Chrome options to use the new profile
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={profile_dir}")
    
    # Launch Chrome with the specified profile
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Navigate to a page to make sure the profile is working
    driver.get("https://www.google.com")
    
    print(f"New Chrome profile created at: {profile_dir}")
    
    return profile_dir

# Function to load an existing Chrome profile
def load_chrome_profile(profile_dir):
    if not os.path.exists(profile_dir):
        raise Exception("Profile directory does not exist.")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-data-dir={profile_dir}")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    return driver

# Create a new Chrome profile (replace 'my_profile' with any profile name you prefer)
profile_path = create_chrome_profile("my_profile")

# To load the profile later, you can call load_chrome_profile with the saved path:
# driver = load_chrome_profile(profile_path)
