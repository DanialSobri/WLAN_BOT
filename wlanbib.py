import os
import time 
import sys
import json
import subprocess


def getWifi():

    command = 'sudo iw dev wlan0 scan | egrep "^BSS | signal | SSID"'

    while(True):
        try:
            result = subprocess.check_output(command, shell=True)
            break
        except:
            continue


    result = str(result)[2::].replace('(on wlan0)',"")

    result = result.replace('\\n',' ')
    result = result.replace('\\t',' ').replace("dBm",' ').replace("SSID:"," ").replace("BSS"," ").replace("signal:"," ")

    result = result.split()[:-1]

    tempDict={}
    wifiList = []
    prevKey = ''
    i=0

    while i < len(result)-2:
        if (result[i].count(':')==5 ):
            if tempDict:
                wifiList.append(tempDict)

            tempDict = {}
            tempDict[’MAC’] = result[i]
            tempDict[’DBM’] = result[i+1]
            tempDict[’SSID’] = result[i+2]
            i += 3

# Handle cases where SSID has spaces
    else:
        tempDict[’SSID’] += ’ ’ + result[i]
        i += 1

return wifiList


print(getWifi())