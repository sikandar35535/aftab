#!/usr/bin/python2#coding=utf-8 import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanizefrom multiprocessing.pool import ThreadPoolfrom requests.exceptions import ConnectionErrorfrom mechanize import Browser reload(sys)sys.setdefaultencoding('utf8')br = mechanize.Browser()br.set_handle_robots(False)br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')] def keluar():	print "\033[1;96m[!] \x1b[1;91mExit"	os.sys.exit() def acak(b): w = 'ahtdzjc' d = '' for i in x: d += '!'+w[random.randint(0,len(w)-1)]+i return cetak(d) def cetak(b): w = 'ahtdzjc' for i in w: j = w.index(i) x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j)) x += '\033[0m' x = x.replace('!0','\033[0m') sys.stdout.write(x+'\n') def jalan(z):	for e in z + '\n':		sys.stdout.write(e)		sys.stdout.flush()		time.sleep(00000.1) ##### LOGO #####logo = """ -----------------------------•◈•( __)\\ ____--------------_------------•◈•|__(~) •||•THE - SIKANDAR -OFFICAL------•◈•|__\~~) •||•SIKANDAR - KHAN---------------•◈•|__(-----\ •◈•------JOKER CREATION--------•◈•|__~~~\ •◈•-----█-------⑦-------█------•◈•|__~~~\ •◈•-----█-------⑧-------█------•◈•|__~~~\ •◈•-----█-------⑥-------█------•◈•\033[1;91m=======================================\033[1;96mAuthor \033[1;93m: \033[1;92SIKANDAR KHAN\033[1;96mInstagram \033[1;93m: \033[1;aftab_006\033[1;96mFacebook \033[1;93m: \033[1; sikandar khan\033[1;96mGithub \033[1;93m: \033[1;92mhttps://github.com/sikandar/joker\033[1;91m=======================================""" def tik():	titik = ['. ','.. ','... ']	for o in titik:		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1) back = 0berhasil = []cekpoint = []oks = []id = []listgrup = []vulnot = "\033[31mNot Vuln"vuln = "\033[32mVuln" os.system("clear")print "\033[1;96m ============================================================="print """\033[1;91m=======================================\033[1;96mAuthor \033[1;93m: \033[1;92mRana Aahil\033[1;96mInstagram \033[1;93m: \033[1;92mFlowRana\033[1;96mFacebook \033[1;93m: \033[1;92m Aahilrana4072\033[1;96mGithub \033[1;93m: \033[1;92mhttps://Github.com/Therana/zero\033[1;91m======================================="""print " \x1b[1;93m=============================================================" CorrectUsername = "joker"CorrectPassword = "joker" loop = 'true'while (loop == 'true'): username = raw_input("\033[1;96m[☆] \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ") if (username == CorrectUsername): 	password = raw_input("\033[1;96m[☆] \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ") if (password == CorrectPassword): print "Logged in successfully as " + username loop = 'false' else: print "Wrong Password" os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA') else: print "Wrong Username" os.system('xdg-open https://www.Youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA') def login():	os.system('clear')	try:		toket = open('login.txt','r')		menu() 	except (KeyError,IOError):		os.system('clear')		print logo		print 42*"\033[1;96m="		print('\033[1;96m[☆] \x1b[1;93mLOGIN WITH FACEBOOK \x1b[1;96m[☆]' )		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')		tik()		try:			


