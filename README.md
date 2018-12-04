# travel-time
    this project is to measure and collect the travel time from bmw rnd center to gateway, which you can edit to any other two points by editing the baidumap.html in the "transit.search("place one","place two")" 

    the baidumap.html should be better run on the server environment due to the limited protocal schemes to load your local .json file. Or maybe firefox can save this issue

    the data collection and visualization worked out by baidumap.py, the real time data saved in data.py while the average hourly timecosts everyday in baidumap.json
     
    it is recommended to add a crontab order to run baidumap.py every hour on your system
