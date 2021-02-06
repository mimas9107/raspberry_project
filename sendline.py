#!/usr/bin/python3
import requests
import time
## chrome browser:
##      user-agent: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
## firefox browser:
##      "user-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"

headers ={
    "user-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
}

# header = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
while True:
    paras = {'value1':'50',
             'value2':'60'
            }
    requests.get("https://maker.ifttt.com/trigger/notify_line/with/key/bFJRg_iEGZJ6FSBLPJ1brr",
                  params=paras,
                  headers=headers)
    time.sleep(60)