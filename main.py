from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
import time


def DenAutoFill():
    driver = webdriver.Firefox()
    driver.maximize_window()
    try:
        # Getting to gozdrav title page...
        driver.get("https://gorzdrav.spb.ru/")
        wd(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[10]/div/div[4]/div[1]/a"))).click()
        
        scroll_chains = ActionChains(driver=driver)
        for scroll1 in range(100):
            scroll_chains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
        
        visuability_event = EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[1]/div[2]/div[1]/div/div[1]/ul/li[14]"))
        wd(driver, 5).until(visuability_event).click()
      
        for scroll2 in range(100):
            scroll_chains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
        wd(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.service-mo-1:nth-child(7) > button:nth-child(3)"))).click()
        time.sleep(5)

    finally:
        driver.close()

    
def main():
    DenAutoFill()



if __name__ == '__main__':
    main()
    