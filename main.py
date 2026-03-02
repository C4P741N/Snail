import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_driver():
    """Sets up a headless Chrome driver for the container."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

if __name__ == "__main__":
    print("🚀 Starting bot...")
    try:
        driver = create_driver()
        print("✅ Driver created successfully")
        
        # Test navigation
        driver.get("https://www.noirconsulting.co.uk/job-search/")
        print(f"📄 Page title: {driver.title}")
        
        time.sleep(5)

        # Optional: take a screenshot to verify
        driver.save_screenshot("screenshot.png")
        print("📸 Screenshot saved")



        # Find the first "Apply now" button
        print("🔍 Looking for 'Apply now' button...")
        # Wait up to 10 seconds for at least one apply button to be present
        apply_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.noir-link[href$='#apply']"))
                )
         # Scroll the button into view just in case
        driver.execute_script("arguments[0].scrollIntoView();", apply_button)
        time.sleep(1)
        
        # Click the button
        print("🖱️ Clicking 'Apply now'...")
        apply_button.click()
        
        # Wait for the next page to load – look for a common element on application pages
        # For example, wait for a form element or a specific heading
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))  # adjust as needed
        )
        print("✅ Application page loaded")
        
        # Take a screenshot of the application page
        driver.save_screenshot("application_page3.png")
        print("📸 Screenshot of application page saved")




        #scrolls down
        print("⬇️ Scrolling to bottom...")
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scrolls to the bottom of the page
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        time.sleep(5)  # Allow time for potential new content
        driver.save_screenshot("screenshot2.png")

        driver.scrolldown()
        
        driver.quit()
        print("👋 Done")
    except Exception as e:
        print(f"❌ Error: {e}")