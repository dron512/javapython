from tqdm import tqdm 
import time
from urllib.request import urlretrieve

mylist = [3,4,5,6,7]
for index,value in enumerate(mylist):
    print(index,value)

for index,i in tqdm(enumerate(range(10))):
    print(index)
    print(i)
    time.sleep(0.1)

link = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA2MjRfMTMy%2FMDAxNjU2MDQ4MzA1OTI0.__5_L58WLUPLwICITVBcFUa-4yYQnrftKvKnFi2x3xsg.y8fuxFcAH8SDAP-cAZWpLXNbDHcSBn6RLkpGLMGY0VYg.JPEG.gidal441%2FKakaoTalk_20220624_134836284_19.jpg&type=a340'

urlretrieve(link,'./aa/myimg.jpg')
