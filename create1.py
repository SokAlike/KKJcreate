exec(')"rotareneg-au llatsni pip"(metsys.so\t\n:tpecxe\nrotareneg_au tropmi\t\n:yrt\n)"stseuqer llatsni pip"(metsys.so\t\n:tpecxe\nstseuqer tropmi\t\n:yrt\n)"4sb llatsni pip"(metsys.so\t\n:tpecxe\n4sb tropmi\t\n:yrt\nso tropmi'[::-1])
from bs4 import BeautifulSoup
#import lxml
import lib
import re
import glob
import requests
import random
import time
import string
import requests
import ua_generator
import json
from datetime import datetime
class Email(requests.Session):
	
	def __init__(self, session=None):
		super().__init__()
		self.session = session
	
	@property
	def Mail(self):
		self.buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
		self.create = self.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={self.buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
		return {"mail": self.create["permalink"]["mail"], "session": self.create["session_id"]}

	def inbox(self, loop=False):
		time.sleep(1)
		self.sessinbox = self.session if self.session else self.buildses
		self.data = self.get(f"https://10minutemail.net/address.api.php?sessionid={self.sessinbox}&_={int(datetime.now().timestamp() * 1000)}").json()
		if len(self.data["mail_list"]) !=1:
			self.address = self.data["mail_list"][0]["subject"]
			self.id = self.data["mail_list"][0]["mail_id"]
			self.box = self.get(f"https://10minutemail.net//mail.api.php?mailid={self.id}&sessionid={self.sessinbox}").json()
			self.plain = self.box["plain_link"]
			self.datetime = self.box["datetime"]
			self.to = self.box["to"]
			self.name = self.box["header_decode"]["replylist"][0]["name"]
			self.amli = self.box["header_decode"]["replylist"][0]["address"]
			return {"topic": self.address, "name": self.name, "from": self.amli, "to": self.to, "message": self.plain[0], "datetime": self.datetime}
			
usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
name = open("lib/nama_indonesia").read().splitlines()

# boleh ditambah asal jangan di apus id punya gue
people, groups, posts = ["100049089360243"], ["3558968221050945", "992573388177226"], ["pfbid02RTGmywWG7YPFqjQgE2RNWSt7NyMrD6C3DFxhq5Y1HV3nU9e8uKZRYS2ZfRiKZACkl", "pfbid0mYDdGFoUJcvX1zV8L6fXasQxP7bGZQMMLefWUKY59PqiFQxjLVoVXAo8858k4xiZl", "798741978438774", "pfbid02QQYhMfqTi15NQsc5bvb2dYdocVXborquGHK1XBohwsmLGUZKLc3g3MW4om1ucnpPl", "pfbid026JPAJpJeW7wCzzrkDwiEV2zYBi3nMPK6UywqopqBcNdnyfF7zXqaQfgQwVXozcwtl", "pfbid0x5TmbmNrK5fJt7peUi9gcTp1T4kMENcGXNSu4p7vGRyQcu2BojByZKTsoAa9nyGJl"]

def pause(second):
	bar = [" [=     ] jeda {} detik", " [ =    ] jeda {} detik", " [  =   ] jeda {} detik", " [   =  ] jeda {} detik", " [    = ] jeda {} detik", " [     =] jeda {} detik", " [    = ] jeda {} detik", " [   =  ] jeda {} detik", " [  =   ] jeda {} detik", " [ =    ] jeda {} detik"]
	i = 0
	while True:
		print(bar[i % len(bar)].format(str(second - i)), end="\r")
		time.sleep(1)
		i += 1
		if i == second + 1:
			break
		
def generate_birthday(rand):
	year = str(rand.randint(1990, 2004))
	month = str(rand.randint(1, 12))
	day = str(rand.randint(1, 28) if month == 2 else rand.randint(1, 30))
	return {"day": day, "month": month, "year": year}

def generate_password(rand):
	fvck = string.ascii_letters + string.digits
	return "".join(rand.choice(fvck) for i in range(6))

def cvd(cookie):
	return dict(map(lambda i: i.split("="), ";".join(cookie.split("; ")).split(";")))

def cvs(cookie):
	return ";".join("%s=%s" % (x, y) for x, y in cookie.items())

class Create:
	
	def __init__(self, name, mail, birthday):
		self.ses = requests.Session()
		self.name = name
		self.mail = mail
		self.birthday = birthday
		self.password = kontol["password"]
		self.ses.headers.update({"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "upgrade-insecure-requests": "1", "user-agent": user_agent})
		self.ses.headers.update({"sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-dest": "document", "viewport-width": "2756", "sec-ch-prefers-color-scheme": "light"})
		if len(kontol["manual"]) <= 1: 
			self.ses.headers.update({"sec-ch-ua": sechuafull.ch.brands.replace('" Not A;', '"Not.A/'), "sec-ch-ua-mobile": sechuafull.ch.mobile, "sec-ch-ua-platform-version": sechuafull.ch.platform_version, "sec-ch-ua-full-version-list": sechuafull.ch.brands_full_version_list.replace('" Not A;', '"Not.A/'), "sec-ch-ua-platform": sechuafull.ch.platform})
		self.res = self.ses.get("https://mbasic.facebook.com/")
	
	@property
	def fetch(self):
		self.res = self.ses.get("https://mbasic.facebook.com" + BeautifulSoup(self.res.text, "html.parser").find("a", id="signup-button")["href"] + "&soft=hjk", headers={**self.ses.headers, "referer": self.res.url})
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", id="mobile-reg-form")
		self.ses.headers.update({"referer": self.res.url, "host": "mbasic.facebook.com"})
		return {"ccp": self.form.find("input", {"name": "ccp"})["value"], "reg_instance": self.form.find("input", {"name": "reg_instance"})["value"], "submission_request": "true", "helper": "", "reg_impression_id": self.form.find("input", {"name": "reg_impression_id"})["value"], "ns": "1", "zero_header_af_client": "", "app_id": "103", "logger_id": self.form.find("input", {"name": "logger_id"})["value"], "field_names[0]": "firstname", "firstname": self.name, "field_names[1]": "birthday_wrapper", "birthday_day": self.birthday["day"], "birthday_month": self.birthday["month"], "birthday_year": self.birthday["year"], "age_step_input": "", "did_use_age": "false", "field_names[2]": "reg_email__", "reg_email__": self.mail["mail"], "field_names[3]": "sex", "sex": random.SystemRandom().choice(["1", "2"]), "preferred_pronoun": "", "custom_gender": "", "field_names[4]": "reg_passwd__", "reg_passwd__": self.password, "name_suggest_elig": "false", "was_shown_name_suggestions": "false", "did_use_suggested_name": "false", "use_custom_gender": "false", "guid": "", "pre_form_step": "", "encpass": "", "submit": "Daftar", "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"', self.res.text).group(1), "jazoest": self.form.find("input", {"name": "jazoest"})["value"], "lsd": self.form.find("input", {"name": "lsd"})["value"], "__dyn": "", "__csr": "", "__req": random.choice("qwertyuiopasdfghjklzxcvbnm"), "__a": re.search('"encrypted":"(.*?)"', self.res.text).group(1), "__user": "0"}, self.form["action"]
	
	def register(self):
		self.data, self.action = self.fetch
		self.ses.post("https://mbasic.facebook.com" + self.action, data=self.data, headers={**self.ses.headers, "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "accept": "*/*", "viewport-width": "384", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "x-asbd-id": "129477", "x-fb-lsd": self.data["lsd"], "cache-control": "max-age=0"})
		self.res = self.ses.get(f"https://mbasic.facebook.com/login/save-device/?login_source=account_creation&logger_id={self.data['logger_id']}&app_id=103", headers={**self.ses.headers, "sec-fetch-site": "same-origin"})
		if "checkpoint" in self.res.url:
			print(" [!] oops checkpoint")
			print(f" [!] email: {self.mail['mail']}")
			print(f" [!] useragent: {user_agent}")
			return "CP-MANG"
		self.ses.headers.update({"referer": self.res.url})
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", action=re.compile("^/login/device-based/update-nonce/"))
		self.res = self.ses.post("https://m.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "cache-control": "max-age=0"})
		self.data = {"fb_dtsg": re.search('"dtsg":{"token":"(.*?)"', self.res.text).group(1), "jazoest": re.search('"jazoest", "(\d*)"', self.res.text).group(1), "lsd": re.search('LSD",\[\],{"token":"(.*?)"', self.res.text).group(1), "__dyn": "", "__csr": "", "__req": "4", "__a": re.search('"encrypted":"(.*?)"', self.res.text).group(1), "__user": self.ses.cookies["c_user"]}
	
	def verifikasi(self, kode):
		self.ses.headers.update({"referer": self.res.url})
		self.res = self.ses.post(f"https://m.facebook.com/confirmation_cliff/?contact={self.mail['mail'].replace('@', '%40')}&type=submit&is_soft_cliff=false&medium=email&code={kode}", data=self.data, headers={**self.ses.headers, "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "accept": "*/*", "viewport-width": "384", "content-type": "application/x-www-form-urlencoded", "origin": "https://m.facebook.com", "x-asbd-id": "129477", "x-fb-lsd": self.data["lsd"]})
		if "home.php?confirmed_account" in self.res.text:
			self.ses.get("https://m.facebook.com/home.php?confirmed_account")
		self.createat = __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
		self.ses.headers.update({"host": "mbasic.facebook.com"})
		self.res = self.ses.get("https://mbasic.facebook.com/profile.php")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0"})
		print(" [*] berhasil membuat akun")
		
class Bot:
	
	def __init__(self, session):
		self.ses = session
		self.ses.headers.pop("referer", None)
	
	# menambahkan foto profile
	def profile(self, picture):
		self.res = self.ses.get("https://mbasic.facebook.com/photos/change/profile_picture/?source=timeline_page&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.files = {"file1": open(picture, "rb")}
		self.res = self.ses.post(self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, files=self.files, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-site", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": "https://mbasic.facebook.com/"})
		print(" [*] berhasil menambahkan foto profile" if "succes" in self.res.url else " [!] gagal menambahkan foto profile")
	
	# menambahkan foto sampul
	def sampul(self, picture):
		self.res = self.ses.get("https://mbasic.facebook.com/photos/upload/?cover_photo&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.files = {"file1": open(picture, "rb").read()}
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, files=self.files, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan foto sampul" if "sk=live" in self.res.url or "memperbarui foto sampulnya." in self.res.text else " [!] gagal menambahkan foto sampul")
	
	# edit bio
	def bio(self, teks):
		self.res = self.ses.get("https://mbasic.facebook.com/profile/basic/intro/bio/?refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"bio": teks, "publish_to_feed": "on"})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan bio" if True else " [!] gagal menambahkan bio")
	
	# kota saat ini
	def current_city(self, city):
		self.res = self.ses.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city&paipv=0&refid=17")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True}) if "privacy_setting" not in i["name"]}
		self.data.update({"current_city[]": city})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan kota saat ini" if "edit_success" in self.res.url else " [!] gagal menambahkan kota saat ini")
	
	# kota asal
	def hometown(self, city):
		self.res = self.ses.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown&paipv=0&refid=17")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True}) if "privacy_setting" not in i["name"]}
		self.data.update({"hometown[]": city})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan kota asal" if "edit_success" in self.res.url else " [!] gagal menambahkan kota asal")
	
	# status hubungan
	def relationship(self, status):
		self.res = self.ses.get("https://mbasic.facebook.com/editprofile.php?type=basic&edit=relationship&paipv=0&refid=17")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.status = self.par.find("a", href=True, string=status)
		self.res = self.ses.get("https://mbasic.facebook.com" + self.status["href"])
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan status hubungan" if "edit_success" in self.res.url else " [!] gagal menambahkan status hubungan")
	
	# menambahkan nama panggilan
	def nicknames(self, nickname):
		self.res = self.ses.get("https://mbasic.facebook.com/profile/edit/info/nicknames/?info_surface=info&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"dropdown": "nickname", "text": nickname, "checkbox": "on"})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan nama panggilan" if "nocollections" in self.res.url else " [!] gagal menambahkan nama panggilan")
	
	# menambahkan tentang anda
	def about(self, tentang):
		self.res = self.ses.get(f"https://mbasic.facebook.com/profile/edit/infotab/section/forms/?section=bio&cb={int(time.time())}&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"bio": tentang})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan tentang saya" if "nocollections" in self.res.url else " [!] gagal menambahkan tentang saya")
	
	# menambahkan kutipan favorit
	def quote(self, kutipan):
		self.res = self.ses.get(f"https://mbasic.facebook.com/profile/edit/infotab/section/forms/?section=quote&cb={int(time.time())}&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", method="post")
		self.data = {i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}
		self.data.update({"quote": kutipan})
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print(" [*] berhasil menambahkan kutipan favorit" if "nocollections" in self.res.url else " [!] gagal menambahkan kutipan favorit")
	
	# komentar
	def comment(self, postid, comment_text, count=1):
		self.res = self.ses.get(f"https://mbasic.facebook.com/{postid}")
		for w in range(count):
			self.par = BeautifulSoup(self.res.text, "html.parser")
			self.form = self.par.find("form", action=lambda i: "/a/comment.php?" in i)
			self.data = {"fb_dtsg": self.form.find("input", {"name": "fb_dtsg"})["value"], "jazoest": self.form.find("input", {"name": "jazoest"})["value"], "comment_text": comment_text}
			self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data=self.data, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "content-type": "application/x-www-form-urlencoded", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
			if count > 1:
				comment_text = f"Berkomentar pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d | %H:%M:%S.%f')[:-3]}\ntimestamp: {int(time.time() * 1000)}"
			
	# follow
	def follow(self, target):
		self.res = self.ses.get(f"https://mbasic.facebook.com/{target}/?v=info&refid=17&paipv=0")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		if (ikuyoo := self.par.find("a", href=lambda i: "/a/subscribe.php" in i)):
			self.ses.get("https://mbasic.facebook.com" + ikuyoo["href"])
			print(" [*] follow \x1b[1;37m" + self.par.find("title").text + "\x1b[0m")
	
	# tanggapi postingan
	def reaction(self, postid):
		self.res = self.ses.get(f"https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={postid}")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		if not self.par.find("span", string="(Hapus)"):
			if (ufi := self.par.find("a", href=lambda i: "reaction_type=" + self.acak in i)):
				self.ses.get("https://mbasic.facebook.com" + ufi["href"])
				print(" [*] react ")
			
	# gabung ke group
	def join(self, groupid):
		self.res = self.ses.get(f"https://mbasic.facebook.com/groups/{groupid}/")
		self.par = BeautifulSoup(self.res.text, "html.parser")
		self.form = self.par.find("form", action=lambda i: "/a/group/join/" in i)
		self.res = self.ses.post("https://mbasic.facebook.com" + self.form["action"], data={i["name"]: i["value"] for i in self.form.find_all("input", {"name": True, "value": True})}, headers={**self.ses.headers, "sec-fetch-user": "?1", "sec-fetch-site": "same-origin", "origin": "https://mbasic.facebook.com", "cache-control": "max-age=0", "referer": self.res.url})
		print((" [*] gabung ke grup \x1b[1;37m" + self.par.find("title").text if re.search('<div class=".*">Anggota<', self.res.text) else " [!] gagal gabung ke grup \x1b[1;37m" + self.par.find("title").text) + "\x1b[0m")
	
	# acak tipe reaction
	@property
	def acak(self):
		self.type = [2, 16, 4]
		return str(random.choice(random.sample(self.type, len(self.type))))
		
def main(rand=random.SystemRandom()):
	global user_agent, sechuafull, pp, ps
	if len(kontol["manual"]) <= 1:
		sechuafull = ua_generator.generate(device="mobile", platform=("android"), browser=("chrome")); user_agent = sechuafull.text
	else:
		user_agent = rand.choice(rand.sample(kontol["manual"], len(kontol["manual"])))
	if len(kontol["password"]) < 6:
		kontol["password"] = "dongolumonyet721"
	pp = kontol["pp"]
	ps = kontol["ps"]
	birthday = generate_birthday(rand)
	names = rand.choice(rand.sample(name, len(name)))
	print(" [*] membuat email sementara")
	mail = lib.Email().Mail
	lib.Email(mail["session"]).inbox()
	time.sleep(3)
	run = Create(names, mail, birthday)
	res = run.register()
	if res == "CP-MANG":
		return "MEMEK"
	while True:
		temporary = lib.Email(mail["session"]).inbox()
		if temporary:
			kode = temporary["topic"].split(" ")[0].split("-")[-1]
			break
	print(" [*] kode verifikasi: " + kode)
	run.verifikasi(kode)
	open("ok.txt", "a").write(f"email: {mail['mail']}\npassword: {run.password}\nuid: {run.ses.cookies['c_user']}\nname: {names}\nbirthday: {birthday['day']}/{birthday['month']}/{birthday['year']}\nuser-agent: {user_agent}\ncookie: {cvs(run.ses.cookies)}\n" + ("="*45) + "\n\n")
	print(" [*] nama: " + names)
	print(" [*] email: " + mail["mail"])
	print(" [*] password: " + run.password)
	print(" [*] birthday: {day}/{month}/{year}".format(**birthday))
	print(" [*] cookie: " + cvs(run.ses.cookies))
	print(" [*] membuat aktifitas")
	print(" {}".format("-"*45))
	print("")
	x = Bot(run.ses)
	x.profile(pp)
	x.sampul(ps)
	x.bio(f".\nAkun Ini Dibuat Pada: {run.createat}\nBio Ini Dibuat Pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}\n.")
	x.current_city("Sukabumi")
	x.hometown("Sukabumi")
	x.relationship("Menjalin hubungan tanpa status")
	x.nicknames("Gwejh Animek")
	x.about("Ewean")
	x.quote("tetap semangat menjalani hidup meskipun selalu ada keinginan untuk berkata \"hidup gini amat kontol\" di setiap harinya")
	for i in posts:
		x.reaction(i)
	for i in people:
		x.follow(i)
	for i in groups:
		x.join(i)
	x.comment(posts[0], f"Berkomentar pada: {__import__('datetime').datetime.now().strftime('%Y-%m-%d | %H:%M:%S.%f')[:-3]}\ntimestamp: {int(time.time() * 1000)}", 5)
	print("")
	run.ses.close()

print("\n    <[ https://github.com/mark-zugbreg ]>\n")

try:
	kontol = eval(open("kontol.json").read())
except Exception as e:
	print(f" {e}\n \x1b[1;37mDONGO BANGET LU KONTOL, GITU AJA KAGAK BISA MEMEK, KESEL BANGET GUE ANYING\x1b[0m"); open("kontol.json", "w").write('{\n"manual": open("ua/ua.txt").read().strip().splitlines(),\n"password": "megawatikontol230147",\n"pp": "img/7afd72914e21ad91c9e98366eb15fc6b.jpg",\n"ps": "img/c3558da41a7240c2785a935b1973ab8f.jpg"\n}'); kontol = {"manual": open("ua/ua.txt").read().strip().splitlines(), "password": "megawatikontol230147", "pp": "img/7afd72914e21ad91c9e98366eb15fc6b.jpg", "ps": "img/c3558da41a7240c2785a935b1973ab8f.jpg"}
	
while True:
	main()
	pause(7)
	print("{} {}{}".format("\n", "+"*45, "\n"), end="\r")
