from urllib.request import urlopen
import urllib
from scapy.all import *
__Author__="Aixic"
 
def get_title():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
              }
    c = open('yinhai.txt', 'r')
    List = c.readlines()
    c.close()
    for i in List:
        #print(i)
        i=i.replace("\n","")
        url = 'http://'+i
        try:
            # url ='http://10.1.1.215'
            #print(url)
            rp = urllib.request.Request(url, headers=header)
            respon = urllib.request.urlopen(rp,timeout=2)
            html = respon.read().decode('utf-8')
            pattern = re.findall(r'<title>(.*?)</title>', html, re.S)
            for pat in pattern:
                s=url + "  --->" + pat+"\n"
                print(s)
                f = open('yh_src.txt', 'a')
                List = f.write(s)
                f.close()
 
        except:
            continue
 
 
if __name__=="__main__":
    get_title()