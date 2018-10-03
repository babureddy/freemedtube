from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import urllib
import os

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import subprocess
fVideos = open("videos.sh","a")
data = open("SearchFreeMedicalTubeFreeUSMLEVideosSharingsite.htm", "r").read()
soup = BeautifulSoup(data,features="html5lib")
a = []
driver = webdriver.Chrome()
for link in soup. find_all('a'):
    if "watch" in link.get('href'):
        if link.get('href') not in a:
            a.append(link.get('href'))
#print (a)
#exit(0)
for m in a:
    driver.get(m)
    time.sleep(10)
    video_title = m[29:]
    video_title = video_title[:-12]
    page_source = driver.page_source
    f = "content=\"http://freemedtube.com/play.php?id=" 
    if f in page_source:
        x = page_source.find(f)+len(f)
        y = page_source.find('"',x)
        s = "wget http://freemedtube.com/play.php?id=" + page_source[x:y] + " -o " + video_title+".mp4\n" 
        print (s)
        fVideos.write(s)
fVideos.close()
driver.close()
exit(0)

