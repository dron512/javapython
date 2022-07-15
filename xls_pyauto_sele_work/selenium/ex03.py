from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = './xls_pyauto_sele_work/chromedriver.exe'

web = webdriver.Chrome(url)
web.get("http://www.naver.com")
web.maximize_window()

search = web.find_element(By.ID,'query')
search.send_keys('여행사')
search.send_keys(Keys.ENTER)
time.sleep(2)

element = web.find_element(By.CSS_SELECTOR,'.ad_section .lst_type .lst.type_more .lnk_head')
element.click()
time.sleep(4)

#현재 마지막 탭으로 이동
web.switch_to.window(web.window_handles[-1])

inputelement = web.find_element(By.CSS_SELECTOR,'.airSearchWrap .airSearchForm .filterWrap .schForm .flightDes .rowEl input')
inputelement.click()
time.sleep(2)

listelement = web.find_elements(By.CSS_SELECTOR,'.searchLayer .searchLayerInner .travelselectCity dl dd')
for i in listelement:
    if i.text =='대구':
        i.click()
        break
time.sleep(3)
listelement = web.find_elements(By.CSS_SELECTOR,'.searchLayer .searchLayerInner .travelselectCity dl dd')
for i in listelement:
    if i.text =='제주':
        i.click()
        break
time.sleep(3)

listelement = web.find_elements(By.CSS_SELECTOR,'.calBox .calendar td button .day')
for i in listelement:
    print(i.text)
    if i.text =='15':
        i.click()
        time.sleep(1)
        i.click()
        time.sleep(1)
    if i.text =='20':
        i.click()
        time.sleep(2)
        break
        
elem = web.find_element(By.CSS_SELECTOR,'#rank > div.searchLayerInner > dl:nth-child(1) > dd > div > button.controller.plus')
elem.click()
time.sleep(1)

elem = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.airSearchArea > div.airSearchFormWrap > div > div.filterWrap > form > div.popup.peopNumSel.first.on > div > div.popupFooter > div.confirmBtn > button')
elem.click()
time.sleep(1)

elem = web.find_element(By.CSS_SELECTOR,'#__next > div > div > div.airSearchArea > div.airSearchFormWrap > div > div.filterWrap > form > fieldset > div > div.colWrap.peop > div > div.row.sehBtn > button')
elem.click()

time.sleep(7)
web.quit()