#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from bs4 import BeautifulSoup
import urllib.request

# const
LOOP_INTERVAL = 1.0
LOOO_DURATION = 180.0

# global
loopCount = 0
lastStatus = 'WJ'


def printWaitJudge():

    status_text = lastStatus

    spinner_chars = ['-', '\\', '|', '/']

    msg = '\r Status: ' 
    if ' ' in status_text:
        msg += "\033[1;37;41m" + status_text + "\033[0m"
    else:
        msg += status_text

    msg += ' ' + spinner_chars[loopCount%4]
    
    print( '\r                    ', end='', flush=True ) 
    print( msg, end='', flush=True )



def printResult(soup, td_tag):

    results = []
    for _ in range(3):
        if td_tag:
            results.append(td_tag.get_text(strip=True))
            td_tag = td_tag.find_next('td')

    if results[0] == 'CE':
        status_text = "\033[1;37;41m" + results[0] + "\033[0m"
        print( '\r                    ', end='', flush=True ) 
        print( "\r Status:" + status_text, flush=True )
        return


    if results[0] == 'AC':
        status_text = "\033[1;37;42m" + results[0] + "\033[0m"
    else:
        status_text = "\033[1;37;41m" + results[0] + "\033[0m"

    print( '\r                    ', end='', flush=True ) 
    print( "\r Status:" + status_text + "  Time:" + results[1] + "  Mem:" + results[2], flush=True )




def loadUrl(url):
    global lastStatus

    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    # td id="judge-status" 
    td_tag = soup.find('td', id='judge-status')
    text_judge_status = td_tag.find('span').get_text() if td_tag else None

    lastStatus = text_judge_status

    if '/' in text_judge_status:
        printWaitJudge()
        return 0
        
    else:
        if text_judge_status == "WJ":
            printWaitJudge()
            return 0
        else:
            printResult(soup, td_tag)
            return 1



def main():

    global loopCount

    url = sys.argv[1]

    startTime = time.time()
    while time.time() - startTime < LOOO_DURATION:
        loopCount += 1
        time.sleep(LOOP_INTERVAL)

        if loopCount % 3 == 1:
            ret = loadUrl(url)
            if ret == 1:
                break
        else:
            printWaitJudge()



if __name__ == "__main__":
    main()



