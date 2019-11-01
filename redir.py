from bot import Bot
import csv
import json
import time

bot = Bot()
bot.load_driver()
log=[]
with open("log.csv") as logfile:
    reader=csv.reader(logfile)
    for line in reader:
        log.append(line)

redir=[]
with open("redir.csv") as f:
    reader=csv.reader(f)
    for line in reader:
        redir.append(line)
try:
    for url in redir[1:]:
        if url not in log:
            try:
                print("add item")
                bot.open_additem()
                time.sleep(3)
            except:
                print("exception add item")
                time.sleep(5)
                bot.open_additem()
                time.sleep(3)
            try:
                bot.add_redirect(old=url[0], new=url[1])
                log.append(url)
            except:
                print("not added")
            time.sleep(2)
except Exception as e:
    print(f"{e} outer")
finally:
    with open("log.csv", 'w', newline='') as my:
        wr=csv.writer(my)
        wr.writerows(log)
