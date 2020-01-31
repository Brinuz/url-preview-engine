from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
driver.save_screenshot("google.png")
