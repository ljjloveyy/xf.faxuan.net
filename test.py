#-*-coding:utf-8-*-

import os
import requests
if os.path.exists("ssid.txt"):  
   	os.remove("ssid.txt")
	os.remove("acc.txt")
s = requests.Session()
a = open("acc.txt",'w')
ssid = open("ssid.txt",'w')
u = open("user.txt",'r')
for line in u.readlines():
	line = line.replace("\n","").split(" ")
	user = line[0]
	password = line[1]
	a.write(user+'\n')
	r = s.get('http://xf.faxuan.net/useris/service/getusersidByUserAccount?userAccount='+user+'&password='+password)
	sid = r.text[0:32]
	ssid.write(sid+'\n')
	print sid

u.close()
ssid.close()
a.close()

