from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#driver = webdriver.Chrome(r"C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe") 
emotion=str(input("Enter the emotion : "))

if emotion == "HAPPY":
    wrds = ["The cure- Friday i'm in love", "The Beatles i want to hold your hand", "Beautiful day"]
    kwrd = ["Cure", "Beatles", "Beautiful"]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(r"C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe",chrome_options=chrome_options)

    for i, j in zip(wrds, kwrd):
       driver.get("https://www.youtube.com/")
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
       driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
       WebDriverWait(driver, 10).until(EC.title_contains(j))
       print(driver.current_url)
       driver.quit()

elif emotion == "ANGRY":
    wrds = ["Maroon 5 - Memories", "The Weeknd - Blinding Lights", "Lloyd P White - Burst Part 2"]
    kwrd = ["maroon", "weeknd", "lloyd"]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(r"C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe",chrome_options=chrome_options)

    for i, j in zip(wrds, kwrd):
       driver.get("https://www.youtube.com/")
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
       driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
       WebDriverWait(driver, 10).until(EC.title_contains(j))
       print(driver.current_url)
       driver.quit()

elif emotion == "SAD":
    wrds = ["I'll Meet You There - Sapajou", "Relax - Markvard", "Wake Up (feat. ROMY DYA) - Wataboi"]
    kwrd = ["I'll Meet You There", "Relax", "Wake Up"]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(r"C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe",chrome_options=chrome_options)

    for i, j in zip(wrds, kwrd):
       driver.get("https://www.youtube.com/")
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
       driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
       WebDriverWait(driver, 10).until(EC.title_contains(j))
       print(driver.current_url)
       driver.quit()

elif emotion == "NEUTRAL":
    wrds = ["Becky Hill - Space", "Justin Bieber & benny blanco - Lonely", "Little Mix - Happiness"]
    kwrd = ["Becky Hill", "Justin Bieber & benny blanco", "Little Mix"]
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(r"C:\Users\Harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe",chrome_options=chrome_options)

    for i, j in zip(wrds, kwrd):
       driver.get("https://www.youtube.com/")
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
       driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
       WebDriverWait(driver, 10).until(EC.title_contains(j))
       print(driver.current_url)
       driver.quit()
            


