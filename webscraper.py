from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import string
import openpyxl
import os
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)



url = "https://www.google.com/maps/@51.0611479,17.0123413,13z?hl=pl"


driver = webdriver.Firefox(service= Service("E:\Download\geckodriver-v0.30.0-win64"))
#driver = webdriver.Firefox(executable_path="E:\Download\geckodriver-v0.29.1-win64\geckodriver.exe")
#service= Service("E:\Download\geckodriver-v0.29.1-win64\geckodriver.exe")
wait = WebDriverWait(driver, 5)
print("gettng the url...")
driver.get(url)
time.sleep(3)

print("accepting cookies...")
driver.find_element_by_xpath("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div").click()
time.sleep(4)

print("writing text and searching...")

searchtext = "test"


canvas.grid(columnspan=3,rowspan=3)
label = tk.Label(text = "What are You looking for?")
label.grid(column=1,row=0)

entry = tk.Entry()
entry.grid(columnspan=3,column=0,row=1)

def get_text():
    print(entry.get())
    browse_text.set("Getting data...")
    searchtext = entry.get()
    searchbox = driver.find_element_by_id("searchboxinput")
    #searchtext = input("") # tutaj terzeba gui
    searchbox.send_keys(searchtext)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(10)
    wb = openpyxl.load_workbook('studia.xlsx')
    ws = wb.active
    ws.title = searchtext
    names_all = []
    i=0

    while (i<1):
        print("finding result list...")
        results = driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
        links = []
        names = []
        for result in results:
            #if (names_all.__contains__(result.get_attribute("aria-label") )) :
            links.append(result.get_attribute("href"))
            names.append(result.get_attribute("aria-label"))
        backurl = driver.current_url

        for result in results:

            driver.get(links.pop(0))
            print("clicking the result...")
            time.sleep(3)
            print("finding getting info ...")
            
            info = driver.find_elements_by_class_name("CsEnBe")
            starrs = driver.find_element_by_class_name("section-star-array")
            infos_to_exl = [names.pop(0)," "," "," ",starrs.get_attribute("aria-label").replace('-gwiazdkowy ','')]


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
            driver.get(backurl)
            time.sleep(3)
        i+=1
        time.sleep(5)
        print("next page..")
        driver.find_element_by_id("ppdPk-Ej1Yeb-LgbsSe-tJiF1e").click()
        time.sleep(5)

    driver.quit()
    wb.save(searchtext+".xlsx")


browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=lambda:get_text(), textvariable=browse_text, font="Arial",bg="#20bebe")
browse_text.set("Search")
browse_btn.grid(column=1, row=2)
root.mainloop()





"""
searchbox = driver.find_element_by_id("searchboxinput")
#searchtext = input("") # tutaj terzeba gui
searchbox.send_keys(searchtext)
searchbox.send_keys(Keys.ENTER)
time.sleep(10)
wb = openpyxl.load_workbook('studia.xlsx')
ws = wb.active
ws.title = searchtext
names_all = []
i=0

while (i<1):
    print("finding result list...")
    results = driver.find_elements_by_class_name("a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
    links = []
    names = []
    for result in results:
        #if (names_all.__contains__(result.get_attribute("aria-label") )) :
        links.append(result.get_attribute("href"))
        names.append(result.get_attribute("aria-label"))
    backurl = driver.current_url

    for result in results:

        driver.get(links.pop(0))
        print("clicking the result...")
        time.sleep(3)
        print("finding getting info ...")
        
        info = driver.find_elements_by_class_name("CsEnBe")
        starrs = driver.find_element_by_class_name("section-star-array")
        infos_to_exl = [names.pop(0)," "," "," ",starrs.get_attribute("aria-label").replace('-gwiazdkowy ','')]


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
        driver.get(backurl)
        time.sleep(3)
    i+=1
    time.sleep(5)
    print("next page..")
    driver.find_element_by_id("ppdPk-Ej1Yeb-LgbsSe-tJiF1e").click()
    time.sleep(5)

driver.quit()
wb.save(searchtext+".xlsx")
"""