from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.morele.net/'
driver.get(url)

#Getting categorys names of the products
try:
    menu_items = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cn-departments-menu-item.cn-menu-item.cn-menu-item-hover.has-submenu"))
    )

    for item in menu_items:
        try:
            link = item.find_element(By.TAG_NAME, "a") 
            print(link.text)
        except Exception as e:
            print(f"Error getting text from link: {e}")
            traceback.print_exc()

except Exception as e:
    print(f"An error occurred: {type(e).__name__}: {e}")
    traceback.print_exc()

finally:
    driver.quit()