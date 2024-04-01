from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def test_website_load():
    print("Starting the test...")
    
    try:
        # Open the browser
        driver = webdriver.Chrome()  # or any other WebDriver you prefer
        
        # Navigate to the website
        driver.get("https://atg.world/")
        print("Navigating to https://atg.world/...")
        
        # Check if the title contains the expected text
        if "ATG - Discover new worlds" in driver.title:
            print("Website loaded successfully!")
            assert True
        else:
            print("Website didn't load properly!")
            assert False
        
    except WebDriverException as e:
        print("An error occurred while trying to load the website:", e)
        assert False
    
    finally:
        # Close the browser
        if 'driver' in locals():
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    test_website_load()
