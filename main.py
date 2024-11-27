from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
import time


def DenAutoFill():
    driver = webdriver.Firefox()
    driver.maximize_window()
    # Getting to gozdrav title page...
    driver.get("https://gorzdrav.spb.ru/")
    # "Запись к врачу" button..
    wd(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[10]/div/div[4]/div[1]/a"))).click()
    scroll_chains = ActionChains(driver=driver)
    #"Petrogradskiy"
    for scroll1 in range(10):
        scroll_chains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
    visuability_event = EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[1]/div[2]/div[1]/div/div[1]/ul/li[14]"))
    wd(driver, 5).until(visuability_event).click()
    # Policlinics
    for scroll2 in range(10):
        scroll_chains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
    wd(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.service-mo-1:nth-child(7) > button:nth-child(3)"))).click()
    #Scrolling down till dentist
    for scroll2 in range(7):
        scroll_chains.key_down(Keys.ARROW_DOWN).pause(0.5).key_up(Keys.ARROW_UP).perform()
    #wd(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[9]/button"))).click()
  
    #moving to dentis section
    Xpath= "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[contains(@class, 'service-block-1 service-speciality')][//*[contains(text(), 'СТОМАТОЛОГ')]]//button[contains(@class,\
     'button button--1 service-block-1__button service-speciality__button')]"
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[@data-speciality-name='СТОМАТОЛОГ']/button"))).click()
    
def main():
    DenAutoFill()

if __name__ == '__main__':
    main()
    