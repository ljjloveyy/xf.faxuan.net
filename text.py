#coding=utf-8
import urllib2
import cookielib
import requests

code = ''
rid = ''
user = ''
password = ''
head = {'Host': 'xf.faxuan.net','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
'Accept': '*/*',
'Accept-Language': 'zh-CN,en-US;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://xf.faxuan.net/bps/frame/t/frame.html?loginUserAccount=1508010480168',
'X-Requested-With': 'XMLHttpRequest'}

#声明一个CookieJar对象实例来保存cookie
#cookie = cookielib.CookieJar()
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#从文件中读取cookie
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://xf.faxuan.net')
for item in cookie:
    	print item
	rid=item.value
    #print 'Value = '+item.value
response = opener.open('http://xf.faxuan.net/service/gc.html')
res=response.read()
fi=open('code.jpg','wb')
fi.write(res)
fi.close()

code = raw_input("输入验证码:")
user = raw_input("帐号：")
password = raw_input("密码：")
response = opener.open("http://xf.faxuan.net//bss/service/userService!doUserLogin.do?userAccount="+user+"&userPassword="+password+"&code="+code+"&rid="+rid)
if '登录成功' in response.read():
	print "登录成功"
else:
	print "登录失败"
response = opener.open('http://xf.faxuan.net/useris/service/getusersidByUserAccount?userAccount='+user+'&password='+password)
res=response.read()
ssid = res[0:32]

s = requests.Session()
r = s.get('http://xf.faxuan.net/pss/service/postPoint?operateType=lpoint&userAccount='+user+'&domainCode=100002009002048&ssid='+ssid,cookies=cookie)
print r.text

#response = opener.open('http://xf.faxuan.net/pss/service/postPoint?operateType=lpoint&userAccount='+user+'&domainCode=100002009002048&ssid='+ssid)
#print response.read()

#response = opener.open('http://xf.faxuan.net/pss/service/postPoint?operateType=spoint&userAccount='+user+'&domainCode=100002009002048&ssid='+ssid+'&stime=14')
#print response.read()
print ssid

response = opener.open('http://xf.faxuan.net/pss/service/getpoint?type=mypoint&userAccount='+user)
print response.read()
for item in cookie:
    	print item

