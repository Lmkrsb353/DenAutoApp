from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as EC
import time

def AutoScroll(ActionChain, times, seconds):
    for scroll in range(times):
        if seconds == 0:
            ActionChain.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_UP).perform()
        else:
            ActionChain.key_down(Keys.ARROW_DOWN).pause(seconds).key_up(Keys.ARROW_UP).perform()

def DenAutoFill():
    driver = webdriver.Firefox()
    scroll_chains = ActionChains(driver=driver)
    driver.maximize_window()
    # Getting to gozdrav title page...
    driver.get("https://gorzdrav.spb.ru/")
    # Pressing the "Запись к врачу" button..
    signing = wd(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[10]/div/div[4]/div[1]/a"))).click()
    
    # Using the 'scroll' option of very powerful ActionChains class to imitate scrolling via keyboard keys
    AutoScroll(scroll_chains, 10, 0)
    visuability_event = EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[1]/div[2]/div[1]/div/div[1]/ul/li[14]"))
    #Selecting the "Petrodvortsoviy" doctor
    wd(driver, 5).until(visuability_event).click()
    # Another scroll...
    AutoScroll(scroll_chains, 10, 0)
    wd(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.service-mo-1:nth-child(7) > button:nth-child(3)"))).click()
    # Scrolling down until an option of select a doctor pops up
    AutoScroll(scroll_chains, 7, 0)
    # moving on to the doctor section
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[@data-speciality-name='ИНФЕКЦИОНИСТ']/button"))).click()
    
    # Xpath is being combined from very difficult conditions due to the neccesity of checking doctor's qualification
    # And making sure that there are available tichets for sign to
    stomatolog_xPath1 = '//*[@id="doctorsOutput"]/div[1]/div[1][.//ul[contains(@class, "service-doctor-top__col service-doctor-top__list service-doctor-top__list_numbers")]]'
    stomatolog_xPath2 = '//div[contains(@class, "service-block-1__button") and text()="Выбрать"]'
    stomatolog_xPath = stomatolog_xPath1 + stomatolog_xPath2
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, stomatolog_xPath))).click()
    # Registr on  an appointment
    wd(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.slots__item:nth-child(1)"))).click()
    # Scrolling inside embedded window in browser is only available like this
    driver.execute_script("window.scrollBy(0,250)")
    # Doesn't have a clue for that...
    wd(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.service-doctor:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)"))).click()
    l = ["Макаровский", "Лев", "Андреевич", "01.03.2006", "lev.makarovskiy@gmail.com", "9212405502"]

    AutoScroll(scroll_chains, 14, 0.1)
    # The following 'for' loop executes insetion into data field one after another
    for x in range(1, 7):
        if x == 4:
            continue
        pole = wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[2]/div[{x}]/input"))) 
        pole.clear()
        scroll_chains.click(pole).pause(0.1).send_keys(l[x-1]).pause(0.1).perform()

    # a pole has diverse absoly com path so it need to be processed separately       
    extra_pole = wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[2]/div[{4}]/div/input")))   
    scroll_chains.click(extra_pole).pause(0.2).send_keys(l[3]).perform()
    # Selecting in a checkbox as we agree
    checkbox = wd(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[3]/label/div[1]")))
    driver.execute_script("arguments[0].click();", checkbox)
    # Confirmation
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[6]/div/form/div[3]/button"))).click()
    AutoScroll(scroll_chains, 15, 0.1)
    # Same series of actions
    checkbox2 = wd(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[7]/div/div[3]/label/div[1]")))
    driver.execute_script("arguments[0].click();", checkbox2)
    wd(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="setAppointmentButton"]'))).click()
def main():
    DenAutoFill()                                                   
                                                                                
if __name__ == '__main__':
    main()
