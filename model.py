from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import string
import openpyxl
import os

class Model:

    #options = FirefoxOptions()
    #options.browser_version = '92'
    #options.platform_name = 'Windows 10'
    #cloud_options = {}
    #cloud_options['build'] = my_test_build
    #cloud_options['name'] = my_test_name
    #options.set_capability('cloud:options', cloud_options)
    
    url = "https://www.google.com/maps/@51.0611479,17.0123413,13z?hl=pl"
    driver = None
    searchtext = ""

    def __init__(self):
        #self.driver = webdriver.Firefox(options=self._options, executable_path="E:\Download\geckodriver-v0.29.1-win64\geckodriver.exe")
        self.driver = webdriver.Firefox()
        wait = WebDriverWait(self.driver, 5)
        self.driver.get(self.url)
        time.sleep(3)
        print("accepting cookies...")
        self.driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div").click()
        time.sleep(4)
    
    def main(self):
        pass


    def search(self, text):
        result = False
        print(f'gettin text to search from view to model: {text}')
        self.searchtext = text
        searchbox = self.driver.find_element(By.ID, value='searchboxinput')
        #searchtext = input("") # tutaj terzeba gui
        searchbox.send_keys(self.searchtext)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(10)
        wb = openpyxl.load_workbook('studia.xlsx')
        ws = wb.active
        ws.title = self.searchtext
        names_all = []
        i=0

        while (i<1):
            print("finding result list...")
            results = self.driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
            links = []
            names = []
            for result in results:
                #if (names_all.__contains__(result.get_attribute("aria-label") )) :
                links.append(result.get_attribute("href"))
                names.append(result.get_attribute("aria-label"))
            backurl = self.driver.current_url

            for result in results:

                self.driver.get(links.pop(0))
                print("clicking the result...")
                time.sleep(3)
                print("finding getting info ...")
                
                info = self.driver.find_elements_by_class_name("CsEnBe")
                #jak nie ma opniii to tego nie ma i wywala błąd
                try:
                    starrs = self.driver.find_element_by_class_name("section-star-array")
                    infos_to_exl = [names.pop(0)," "," "," ",starrs.get_attribute("aria-label").replace('-gwiazdkowy ','')]
                except NoSuchElementException as exception:
                    print('The objects does not have a starrs section.')
                    infos_to_exl = [names.pop(0)," "," "," ",'nie ma']
               
                


                infos_to_edit = [] # lista informacji
                for elem in info:
                    #print(elem.get_attribute("aria-label"))
                    infos_to_edit.append(elem.get_attribute("aria-label"))

                
                for str in infos_to_edit:
                    if (str.find('Adres: ')!=-1):
                        infos_to_exl[1] = str.replace('Adres: ','')
                    if (str.find('Telefon: ')!=-1):
                        infos_to_exl[2] = str.replace('Telefon: ','')
                    if (str.find('Witryna: ')!=-1):
                        infos_to_exl[3] = str.replace('Witryna: ','')
                try:
                    print(infos_to_exl)
                    ws.append(infos_to_exl)
                except IndexError:
                    pass


                print("getting brack from result ...")
                self.driver.get(backurl)
                time.sleep(3)
            i+=1
            time.sleep(5)
            print("next page..")
            self.driver.find_element_by_id("ppdPk-Ej1Yeb-LgbsSe-tJiF1e").click()
            time.sleep(5)

        self.driver.quit()
        wb.save(self.searchtext+".xlsx")
        result = True
        return result


