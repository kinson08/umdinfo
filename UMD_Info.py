# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:20:40 2018

@author: kinso
"""

import requests,bs4
import json,time
import feedparser
#from translate_api.translate_api import api as translate
#import translate_api
import copy
#from translate import translator


#获取警示信息
def getalerts():
    global EAlertStr,TextClass
    alerturl='https://alert.umd.edu/alerts/'
    alertres=requests.get(alerturl)
    alertsoup=bs4.BeautifulSoup(alertres.text,'html5lib')
    submitsoup=alertsoup.find_all('div',{'class':'meta submitted'})

    alerthtml=alertsoup.find_all('div',{'class':'field-item even'})
    c=1
    mystr=''
    for myalert in alerthtml:
        text1=''
        text2=''
        text3=''
        text4=''

        text1=myalert.get_text()
        breakpos=text1.find('Safety Resources:')
        text2=text1[0:breakpos]
        p=''
        text3=text2.split('\n')
        for t in text3:
            tmpstr=t.rstrip()
            if not tmpstr=='':
                text4=text4+tmpstr

        tstr1=submitsoup[c-1].get_text()
        tpos=tstr1.find('on')
        tstr2=tstr1[tpos+2:len(tstr1)]
        tstr2=tstr2.strip()
        s='[%s]----%s'%(tstr2,text4)
        #print(str(c)+'.'+tstr2+'  '+text4)
        mystr=mystr+s+'\n\n'+'='*30+'\n'
        c=c+1
    EAlertStr=mystr
    TextClass=1
    return(mystr)


def getnews():
    global ENewsStr,TextClass
    myurl='https://www.umdrightnow.umd.edu/feed/latest-news'

    try:
        myres=requests.get(myurl)

        mydict=feedparser.parse(myres.text)

        news_c=1
        info=''
        for a in mydict['entries']:
            info=info+str(news_c)+'. '+a['title']+'\n'
            tmp=bs4.BeautifulSoup(a['summary_detail']['value'],'html5lib')
            info=info+tmp.get_text()+'='*30+'\n'
            news_c=news_c+1

    except ConnectionError:
        info='连接失败，请稍后再试！'#ios
    ENewsStr=info
    TextClass=2
    return(info)

if __name__=='__main__':
    umd_news=getnews()
    print(umd_news)
#    print(translate(umd_news))
    
#    umd_alerts=getalerts()
#    print(umd_alerts)
