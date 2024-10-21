import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def load_chrome_profile(profile_dir):
    profile_dir = os.path.abspath(profile_dir)
    
    if not os.path.exists(profile_dir):
        raise Exception(f"Profile directory does not exist: {profile_dir}")
    
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={profile_dir}")
    chrome_options.add_argument("--disable-notifications")  # Optional: Disable notifications
    chrome_options.add_argument("--start-maximized")  # Optional: Start maximized
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def post_youtube_comment(video_url, comment_text, profile_dir):
    driver = load_chrome_profile(profile_dir)
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds for elements
    
    try:
        # Navigate to the YouTube video
        driver.get(video_url)

        time.sleep(30)  # Ensure profile is fully loaded and any manual login is completed
        
        # Wait until the video title is present to ensure the page has loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.title yt-formatted-string')))
        
        # Scroll down to the comments section
        # Comments are typically loaded after some time, so wait for the comment section to be present
        # Use JavaScript to scroll to the comment box
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'ytd-comments')))
        comments_section = driver.find_element(By.TAG_NAME, 'ytd-comments')
        driver.execute_script("arguments[0].scrollIntoView();", comments_section)
        
        # Wait for the "Add a public comment..." box to be clickable
        comment_box_placeholder = wait.until(EC.element_to_be_clickable((By.ID, "placeholder-area")))
        comment_box_placeholder.click()
        
        # Wait for the active comment input box to be present
        active_comment_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#contenteditable-root")))
        
        # Click the active comment box to ensure it's focused
        active_comment_box.click()
        
        # Enter the comment text
        active_comment_box.send_keys(comment_text)
        
        # **Updated XPath Selector for the "Comment" Button**
        comment_button = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//ytd-button-renderer[@id='submit-button']//button[@aria-label='Comment']"
        )))
        
        # **Attempt to Click the "Comment" Button with Fallback**
        try:
            comment_button.click()
        except Exception as e:
            print(f"Standard click failed: {e}. Attempting JavaScript click.")
            driver.execute_script("arguments[0].click();", comment_button)
        
        print("Comment posted successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Optional: Keep the browser open for a while to see the result
        # time.sleep(5)
        
        # Close the browser
        driver.quit()

# Example usage:
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=UbZlYl92OGU"
    comment_text = "Great video! Thanks for sharing."
    profile_dir = "C:/Users/theal/school/econ_data_lab_judiciary/src/chrome_profiles/mike_ross"  # Path to your Chrome profile
    
    post_youtube_comment(video_url, comment_text, profile_dir)
