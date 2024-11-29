from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
import time
def Autoscroll(dfjdjf)

def DenAutoFill():
    driver = webdriver.Firefox()
    scroll_chains = ActionChains(driver=driver)
    driver.maximize_window()
    # Getting to gozdrav title page...
    driver.get("https://gorzdrav.spb.ru/")
    # Pressing the "Запись к врачу" button..
    signing = wd(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[10]/div/div[4]/div[1]/a"))).click()
    
    # Using the 'scroll' option of very powerful ActionChains class to imitate scrolling via keyboard keys
    for scroll1 in range(10):
        scroll_chains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
    visuability_event = EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[1]/div[2]/div[1]/div/div[1]/ul/li[14]"))
    #Selecting the "Petrodvortsoviy" distinct
    wd(driver, 5).until(visuability_event).click()
    # Another scroll...
    for scroll2 in range(10):
        scroll_chains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
    wd(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.service-mo-1:nth-child(7) > button:nth-child(3)"))).click()
    #Scrolling down until an option of select a dentist pops up
    for scroll2 in range(7):
        scroll_chains.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
    #wd(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[9]/button"))).click()
  
    #moving to dentis section
    Xpath= "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[contains(@class, 'service-block-1 service-speciality')][//*[contains(text(), 'СТОМАТОЛОГ')]]//button[contains(@class,\
     'button button--1 service-block-1__button service-speciality__button')]"
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[@data-speciality-name='ИНФЕКЦИОНИСТ']/button"))).click()
    
    stomatolog_xPath = '//*[@id="doctorsOutput"]/div[1]/div[1][.//ul[contains(@class, "service-doctor-top__col service-doctor-top__list service-doctor-top__list_numbers")]]//div[contains(@class, "service-block-1__button") and text()="Выбрать"]'

    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, stomatolog_xPath))).click()

    #Registr an appointment
    wd(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.slots__item:nth-child(1)"))).click()
    driver.execute_script("window.scrollBy(0,250)")
    wd(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.service-doctor:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)"))).click()
    l = ["Макаровский", "Лев", "Андреевич", "01.03.2006", "lev.makarovskiy@gmail.com", "9212405502"]
    for scroll2 in range(14):
        scroll_chains.key_down(Keys.ARROW_DOWN).pause(0.1).key_up(Keys.ARROW_UP).perform()
    for x in range(1, 7):
        if x == 4:
            continue
        pole = wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[2]/div[{x}]/input"))) 
        pole.clear(); pole.send_keys(l[x-1])                                    
        time.sleep(0.1)     
           
    pole = wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[2]/div[{4}]/div/input")))   
    scroll_chains.click(pole).pause(0.2).send_keys(l[3]).perform()
    checkbox = wd(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[3]/label/div[1]")))
    driver.execute_script("arguments[0].click();", checkbox)
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[3]/button"))).click()
    for scroll in range(15):
        scroll_chains.key_down(Keys.ARROW_DOWN).pause(0.1).key_up(Keys.ARROW_UP).perform()
    checkbox2 = wd(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[7]/div/div[3]/label/div[1]")))
    driver.execute_script("arguments[0].click();", checkbox2)
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="setAppointmentButton"]'))).click()
def main():
    DenAutoFill()                                                   
                                                                                
if __name__ == '__main__':
    main()
