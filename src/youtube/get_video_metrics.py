from imports import *
from comment import load_chrome_profile

def get_metrics(video_url, profile_dir):
    driver = load_chrome_profile(profile_dir)
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds for elements
    
    try:
        # Navigate to the YouTube video
        driver.get(video_url)
        time.sleep(15)  # Ensure profile is fully loaded and any manual login is completed
        
        # Wait until the video title is present to ensure the page has loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.title yt-formatted-string')))
        
        time.sleep(2) 

        # Locate and retrieve the likes count using the new selector
        likes_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#top-level-buttons-computed > segmented-like-dislike-button-view-model > yt-smartimation > div > div > like-button-view-model > toggle-button-view-model > button-view-model > button')
        ))

        likes = likes_button.text
        
        comments_section = driver.find_element(By.TAG_NAME, 'ytd-comments')
        driver.execute_script("window.scrollBy(0, arguments[0].getBoundingClientRect().top - 100);", comments_section)

        views = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#info > span:nth-child(1)'))).text
        
        comments = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#count > yt-formatted-string > span:nth-child(1)'))).text
        
        print(f"Views: {views}")
        print(f"Likes: {likes}")
        print(f"Comments: {comments}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot("error_screenshot.png")  # Save a screenshot for debugging
        with open("error_log.txt", "w") as f:
            f.write(str(e))  # Write the error message to a log file
    
    finally:
        # Optional: Keep the browser open for a while to see the result
        #time.sleep(30)
        
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=06kJXhOZhLU"
    profile_dir = "/Users/sharvil/Library/Application Support/Google/Chrome/Profile 1"  # Path to your Chrome profile
    
    get_metrics(video_url, profile_dir)