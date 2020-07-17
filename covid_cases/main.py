from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D://corovirus map//icon.ico",
        timeout = 28

    )

def getData(url):
    #driver.get(url)
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
   while True:
       # notifyMe("Ria" ,"Lets stop the spread of the virus together")   
        myHtmlData = getData("https://www.mohfw.gov.in/")   


        soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())  
        myDataStr = ""
        for tr in soup.find_all('tbody'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]    
        #myDataStr = myDataStr[:1]
        itemList = myDataStr.split("\n\n")    

        states = ['Goa', 'Gujarat','Delhi']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[2] in states:
                print(dataList)   
                ntittle = 'cases of COVID-19' 
                ntext = f"STATE : {(dataList[2])}\nTotal cases : {(dataList[3])}\nCaured : {(dataList[4])}\nDeath : {(dataList[5])}"
                notifyMe(ntittle, ntext)
                time.sleep(3)
        time.sleep(3600)        