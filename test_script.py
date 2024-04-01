from selenium import webdriver

def test_website_load():
    driver = webdriver.Chrome()  # or any other WebDriver you prefer
    driver.get("https://atg.world/")
    if "ATG - Discover new worlds" in driver.title:
        print("Website loaded successfully")
        assert True
    else:
        print("Website didn't load properly")
        assert False
    driver.quit()

if __name__ == "__main__":
    test_website_load()
