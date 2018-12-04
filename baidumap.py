from selenium import webdriver
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import time
import datetime
import numpy
import json
#get a list of recorded data
class bdmap(object):
    def __init__(self):
        self.url='/home/pi/fortest.html'
        self.data=self.getdata()
        self.avetime=self.rtaverage()
        self.timeline=self.timeline()
        self.weekdata=self.costaw()
    def getdata(self):
        from data import record
        return record
    def getdate(self):
        now=datetime.datetime.now()
        date=now.strftime('%A')
        return date
    def gethour(self):
        now=datetime.datetime.now()
        hour=now.strftime('%H')
        return hour
    #get the time cost from web
    def getweb(self):
        driver=webdriver.PhantomJS()
        driver.get(self.url)
        time.sleep(2)
        soup=BeautifulSoup(driver.page_source,'html.parser')
        data=soup.find('div',{'id':'record'}).get_text()
        minute=self.sectomin(int(data))
        return minute
    #write to python file
    def sectomin(self,sec):
        minutes=sec//60
        return minutes
    def writedata(self,data):
        with open('data.py','w') as d:
            d.write('record='+str(data))
            d.close()
    #transfer and export the record in JSON 
    def exportjson(self):
        dic=self.data
        jsondata={}
        for i in dic.keys():
            alltime=[]
            for j in dic[i].keys():
                alltime.extend(dic[i][j])
            #print(alltime)
            try:
                maxnum=max(alltime)
                ave=numpy.mean(alltime)
            except ValueError:
                maxnum=0
                ave=0
            jsondata[i]=[int(ave),int(maxnum)]
        f=open('baidumap.json','w')
        json.dump(jsondata,f)
        
    #save data in data.py
    def exportdata(self):
        record=self.getdata()
        date=self.getdate()
        hour=self.gethour()
        #if no record befour, create this index
        try:
            if hour in record[date].keys():
                 record[date][hour].append(self.getweb())
                 if len(record[date][hour])>10:
                     record[date][hour].pop(0)
            else:
                record[date][hour]=[self.getweb()]
        except KeyError:
            record[date]={}
            record[date][hour]=[self.getweb()]
        self.writedata(record)
        
    def initlist(self,n):
        lst=[0 for i in range(n)]
        return lst
    #average timecost at every hour everyday
    def rtaverage(self):
        record=self.getdata()
        rt={}
        for i in record.keys():
            for j in record[i].keys():
                try:
                    rt[i][j]=int(round(numpy.mean(record[i][j])))
                except KeyError:
                    rt[i]={}
                    rt[i][j]=int(round(numpy.mean(record[i][j])))
        return rt
    #generate timecost at every hour everyday in list
    def timeline(self):
        rt=self.rtaverage()
        for i in rt.keys():
            lst=self.initlist(24)
            for j in rt[i]:
                lst[int(j)]=rt[i][j]
            yield lst
    #the average timecost every hour in one week
    def costaw(self):
        b=[]
        for i in self.timeline:
            b.append(i)
        #print(b)
        matrix=numpy.array(b).T
        
        #print(matrix)
        #print(matrix.shape)
        total=numpy.sum(matrix,axis=1)
        
        #print(type(total))
        divider=[]
        for i in range(matrix.shape[0]):
            divider.append(numpy.count_nonzero(matrix[i]))
        tc=numpy.divide(numpy.array(total),numpy.array(divider))
        tc=list(map(self.inftoint,tc))
        return tc
 #convert numpyfloat into integer,if NaN or INF,return 0
    def inftoint(self,i):
        try:
            return int(i)
        except:
            return 0
    def makegraph(self):
        fig=plt.figure()
        fig.suptitle('Hourly Timecosts',fontsize=25,fontweight='bold',color='green')
        yaxis=self.weekdata
        xaxis=list(range(24))
        plt.plot(xaxis,yaxis,linewidth=2)
        plt.ylabel('timecosts in minutes',fontsize=15)
        plt.xlabel('hours',fontsize=15)
        plt.xticks(numpy.arange(0,23,2))
        plt.yticks(numpy.arange(0,65,5))
        fig.savefig('timecost.jpg')
        #plt.show()
        
    
        


mp=bdmap()
mp.exportdata()
mp.exportjson()
print(mp.weekdata)
mp.makegraph()


