from selenium import webdriver

def test_load_atg_website():
    # Open a Chrome browser
    driver = webdriver.Chrome()
    
    try:
        # Navigate to the atg.world website
        driver.get("https://atg.world/")
        
        # Check if the website title contains the expected text
        assert "ATG - Discover new worlds" in driver.title
        
        print("Website loaded successfully")
    
    except Exception as e:
        # Print error message if website doesn't load properly
        print("Website loading failed:", e)
        raise
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_load_atg_website()
