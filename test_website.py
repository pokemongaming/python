import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

base_url="https://www.letskodeit.com/practice"

def test_get():
    
        driver=webdriver.Chrome()
        driver.get(base_url)
        url=driver.current_url
        print(url)
        title=driver.title
        print(title)

        #radio button selection

        bmwradio=driver.find_element(By.ID,"bmwradio")
        bmwradio.click()
        benzradio=driver.find_element(By.ID,"benzradio")
        if bmwradio.is_selected():
            print("Yes, Bmw radio is selected")
        else:
            print("No, Bmw radio button is not selected") 
        if benzradio.is_selected():
            print("Yes, Benz radio button is selected")
        else:
            print("No, Benz radio button is not selected")
        benzradio.click()
        assert benzradio.is_selected()==True
        assert bmwradio.is_selected()==False   
        
        # checkbox selection
        #bmwcheck=driver.find_element(By.ID,"bmwcheck")
        #benzcheck=driver.find_element(By.ID,"benzcheck")
        #bmwcheck.click()
        #benzcheck.click()
        #if bmwcheck.is_selected and benzcheck.is_selected():
        #    print("yes, bmw and benz are selected")
        #else:
        #    print("no , they are not selected")     
 
        #hceckbox difference
        bmwcheck1=driver.find_element(By.ID,"bmwcheck")
        benzcheck1=driver.find_element(By.ID,"benzcheck")
        bmwcheck1.click()
        assert bmwcheck1.is_selected()==True
        benzcheck1.click()
        assert bmwcheck1.is_selected() and benzcheck1.is_selected()==True
        bmwcheck1.click()
        assert not bmwcheck1.is_selected() 
        assert benzcheck1.is_selected()==True
        parent_window=driver.current_window_handle

        #open window 
        owindow=driver.find_element(By.ID,"openwindow")
        owindow.click()
        handles=driver.window_handles
        for i in handles:
            driver.switch_to.window(i)
            url1=driver.current_url
            print(url1)
            title1=driver.title
            print(title1)
        driver.switch_to.window(parent_window)   
        url11=driver.current_url
        print(url11)
        title11=driver.title
        print(title11) 

        #open a new tab
        original_tab=driver.current_window_handle
        driver.find_element(By.ID,"opentab").click()
        all_tab=driver.window_handles
        for tab in all_tab:
            if tab!=original_tab:
                driver.switch_to.window(tab)
                break

        print(driver.title)
        print(driver.current_url)
        assert driver.current_url != base_url
        driver.switch_to.window(original_tab) 
        print("Original Tab Title:", driver.title)       

        #select
        x=driver.find_element(By.ID,"carselect")
        drop=Select(x)
        drop.select_by_index(2) 

        #select multiple
        select_element=Select(driver.find_element(By.ID,"multiple-select-example"))
        if select_element.is_multiple:
            select_element.select_by_visible_text("Apple")
            select_element.select_by_index(2) 