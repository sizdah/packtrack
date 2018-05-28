from bs4 import BeautifulSoup
import requests
from time import sleep
from telegram import Bot
TOKEN = "618659314:AAFXCs3GtDYB-2_hyn3MQtqAAbrKf873HTE"
bot = Bot(TOKEN)

while True:
   try:
    base = "https://www.aramex.com/track/results?mode=0&ShipmentNumber=31101462490"
    r = requests.get(base)
    page = r.content
    soup = BeautifulSoup(page, 'html.parser')

    vids = soup.findAll('div', attrs={'class': "amx-responsive-table-faux-cell"})
    raw =str (vids[1].text)
    #first_sp = raw.partition("Invalid")[0]
    #sec_sp = raw.partition("available")[2]
    #raw=raw.replace(first_sp,"").replace(sec_sp,"")
    if 'Invalid number' not in raw:
        bot.send_message(chat_id=34015964, text=raw)
        print("good")
    else:
        print("still invalid")
        sleep(600)
   except:
       sleep(600)
