from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from urllib.request import urlretrieve # 이미지 파일 다운로드에 사용
from tqdm import tqdm
import os

findstr = '문도박사'

url= './xls_pyauto_sele_work/chromedriver.exe'

web = Chrome(url)
web.get('http://www.naver.com')

elem = web.find_element(By.ID,'query')
elem.send_keys(findstr)
time.sleep(1)
elem.send_keys(Keys.ENTER)
time.sleep(1)
elem = web.find_element(By.LINK_TEXT,'이미지')
elem.click()
time.sleep(1)

elem = web.find_elements(By.CSS_SELECTOR,'.sp_nimage .photo_tile .photo_bx .link_thumb>img')

for i in range(3):
    elem[i].click()
    time.sleep(1)

result = []
for img in tqdm(elem):
    if "http" in img.get_attribute("src"):
        result.append(img.get_attribute("src"))

print(result)

if not os.path.isdir(f"./{findstr}"):
        os.mkdir("./{}".format(findstr))

'''
https://search.pstatic.net/common/?
src=http%3A%2F%2Fblogfiles.naver.
net%2FMjAyMjA2MzBfOSAg%2FMDAxNjU2NTk3MDA3NDUz.
Vi9Xv0BuSCcYSsjiCDxKnUh3D9kwHrP188wG8lMQ14Yg.
a9GyiPU4eBKmhiU_4Kh743mx3HbcCwgMTHyAm8dNovog.
JPEG.semi3242%2FIMG_5308.jpg&type=a340
'''
for index, link in tqdm(enumerate(result)):
    start = link.rfind(".")
    print('start = ',start)
    end = link.rfind("&")
    print('end = ',end)
    filetype = link[start:end]
    
    urlretrieve(link, f"./{findstr}/{findstr}{index}{filetype}")

time.sleep(3)
web.quit()