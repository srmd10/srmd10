import requests,threading,webbrowser
print("SARMAD @SRMD_TUBE")
print("🔥نورت اقوئ ادا رشق انستا")
webbrowser.open("https://t.me/srmd_tube")
class Hamody():
	def __init__(self):
		self.r = requests.session()
		self.file = input("[~] ادخل موقع ملف الحسابات الوهمية 👉 : ")
		for i in open(self.file,"r").read().splitlines():
			self.username = i.split(":")[0]
			self.password = i.split(":")[1]
			self.user = input("[~] ادخل يوزر حساب لترشقله 😶‍🌫️ : ")
			he = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar',
		'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
		'x-asbd-id': '198387',
		'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': '0',
		}
			urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={self.user}'
			try:
				re =requests.get(urlg,headers=he).json()
				self.id = re["data"]["user"]["id"]
				print("[~] Your ID : "+str(self.id))
				self.loo()
			except requests.exceptions.RequestException as e:
				print("error user")
				self.__init__()
	def loo(self):
		url = "https://takipcitime.com/login?"
		headers = {
    "Host": "takipcitime.com",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": "_ga=GA1.2.878189839.1656896217;_gid=GA1.2.522159309.1660122325;54a8ff51e6ec866f4f003daad04a4de5=3d94a12c8a90fd64e126b6e3461863e6;_gat=1"
		}
		data = {
"username":self.username,
"password":self.password
		}
		r = requests.post(url,headers=headers,data=data)
		if r.json()["status"]=="success":
			print("[√] Done Login ")
			self.lootoken = r.cookies["54a8ff51e6ec866f4f003daad04a4de5"]
			self.loo2()
		else:
			print("[×] Error Login")
			self.login()
	def loo2(self):
		url = "https://takipcitime.com/tools"
		headers = {
    "Host": "takipcitime.com",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"_ga=GA1.2.878189839.1656896217;_gid=GA1.2.522159309.1660122325;54a8ff51e6ec866f4f003daad04a4de5={self.lootoken};_gat=1"		
		}
		r = requests.get(url,headers=headers).cookies["54a8ff51e6ec866f4f003daad04a4de5"]
		self.took23=r
		self.rere()
	def rere(self):
		url = f"https://takipcitime.com/tools/send-follower/{self.id}?formType=send"
		headers = {
    "Host": "takipcitime.com",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"_ga=GA1.2.878189839.1656896217;_gid=GA1.2.522159309.1660122325;54a8ff51e6ec866f4f003daad04a4de5={self.took23};_gat=1"		
		}
		data = {
"adet":"600",
"userID":self.id,
"userName":self.user
		}
		re = requests.post(url,headers=headers,data=data).json()
		if re["status"]=="success":
			print("[√] Done Send Followers ")
			self.login()
		else:
			print("[×] Erro Send Followers")
			self.login()
	def login(self):
		url = "https://takipstar.com/giris"
		headers = {
    "Host": "takipstar.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": "990ac72515697fce0791b62e74db1e10=3029feef7d702c1f67a0e59478a2a3c6;_ga=GA1.2.792996682.1658649375;_gid=GA1.2.249833248.1658649375;_gat=1"
		}
		data = {
"username":self.username,
"password":self.password
}
		log = self.r.post(url,headers=headers,data=data)
		if log.json()["status"]=="success":
			print("[√] Done Login")
			self.token = log.cookies["990ac72515697fce0791b62e74db1e10"]
			self.user_id()
		else:
			print("[×] Error Login")
			self.token11()
	def user_id(self):
		self.id = self.id
		self.get_follow_token()
	def get_follow_token(self):
		url = "https://takipstar.com/tools/send-follower"
		headers = {
    "Host": "takipstar.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "accept": "*/*",
    "cookie": f"990ac72515697fce0791b62e74db1e10={self.token}"
		}
		self.token_follow = requests.get(url,headers=headers).cookies["990ac72515697fce0791b62e74db1e10"]
		self.follow()
	def follow(self):
		url = f"https://takipstar.com/tools/send-follower/{self.id}?formType=send"
		headers = {
    "Host": "takipstar.com",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"_ga=GA1.2.792996682.1658649375;_gid=GA1.2.249833248.1658649375;990ac72515697fce0791b62e74db1e10={self.token_follow};_gat=1"
		}
		data = {
"adet":"100",
"userID":self.id,
"userName":self.user
		}
		req = requests.post(url,headers=headers,data=data).json()
		if req["status"]=="error":
			print("[×] Error Send Followers")
			self.token11()
		else:
			print("[√] Done Send Followers")
			self.token11()
	def token11(self):
		url = "https://medyahizmeti.com/member"
		headers = {
	    "Host": "medyahizmeti.com",
	    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
	    "accept": "*/*",
	    "cookie": "_ga=GA1.2.966214335.1657335385;_gid=GA1.2.1907867909.1657335385;da7f4069884ff8bd7c4e6f3b1bed7640=2eee294a88fcc54b3a60aa29a5cff509;_gat=1"}
		data = {
	"username":self.username,
	"password":self.password
	}
		login = requests.post(url,headers=headers,data=data)
		check = login.text
		if login.json()["status"]=="success":
			print("[√] Done Login")
			self.ttoken = login.cookies["da7f4069884ff8bd7c4e6f3b1bed7640"]
			self.get_follow1()
		else:
			print("[×] Error Login")
			self.login3()
	def get_follow1(self):
		url2 = "https://medyahizmeti.com/tools"
		headers2 = {
		    "Host": "medyahizmeti.com",
		    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
		    "accept": "*/*",
		    "cookie": f"_ga=GA1.2.966214335.1657335385;_gid=GA1.2.1907867909.1657335385;da7f4069884ff8bd7c4e6f3b1bed7640={self.ttoken}"
		}
		self.token2 = requests.get(url2,headers=headers2).cookies["da7f4069884ff8bd7c4e6f3b1bed7640"]
		self.send_followers()
	def send_followers(self):
		url3 = f"https://medyahizmeti.com/tools/send-follower/{self.id}?formType=send"
		headers3 = {
		    "Host": "medyahizmeti.com",
		    "accept": "*/*",
		    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
		    "cookie": f"_ga=GA1.2.966214335.1657335385;_gid=GA1.2.1907867909.1657335385;da7f4069884ff8bd7c4e6f3b1bed7640={self.token2};_gat=1"
		}
		data3 = {
		"adet":"150",
		"userID":self.id,
		"userName":self.user
		}
		sendfollow = requests.post(url3,headers=headers3,data=data3).json()
		if sendfollow["status"]=="error":
			print("[×] Error Send Followers")
			self.login3()
		else:
			print("[√] Done Send Followers")
			self.login3()
	def login3(self):
		url = "https://www.instamoda.org/login?"
		headers = {
    "Host": "www.instamoda.org",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": "89cdd01f1f0b9572a53da81bfe4172b4=cd6862968380cd4e629bd9cc9c726e23;_ga=GA1.2.1318610592.1658715826;_gid=GA1.2.21006396.1658715826"
		}
		data = {
"username":self.username,
"password":self.password
		}
		req = requests.post(url,headers=headers,data=data)
		if req.json()["status"]=="success":
			print("[√] Done Login")
			self.mnt = req.cookies["89cdd01f1f0b9572a53da81bfe4172b4"]
			self.plpl()
		else:
			print("[×] Error Login")
			self.logins6()
	def plpl(self):
		url = "https://www.instamoda.org/tools"
		headers = {
    "Host": "www.instamoda.org",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "accept": "*/*",
    "cookie": f"89cdd01f1f0b9572a53da81bfe4172b4={self.mnt}"
		}
		self.res = requests.get(url,headers=headers).cookies["89cdd01f1f0b9572a53da81bfe4172b4"]
		self.sends()
	def sends(self):
		url = f"https://www.instamoda.org/tools/send-follower/{self.id}?formType=send"
		headers = {
    "Host": "www.instamoda.org",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"89cdd01f1f0b9572a53da81bfe4172b4={self.res}"
		}
		data = {
"adet":"25",
"userID":self.id,
"userName":self.user
		}
		logins = requests.post(url,headers=headers,data=data).json()
		if logins["status"]=="error":
			print("[×] Error Send Followers")
			self.logins6()
		else:
			print("[√] Done Send Followers")
			self.logins6()
	def logins6(self):
		url = "https://bayitakipci.com/memberlogin?"
		h = {
		    "Host": "bayitakipci.com",
		    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
		    "cookie": "_ga=GA1.2.413336954.1657374406;9db306b622cf2879e24263c572efb040=440f4f42dec4ec302171999605fde500;_gid=GA1.2.1860924705.1658811865"
		}
		d = {
		"username":self.username,
		"password":self.password
		}
		req = requests.post(url,headers=h,data=d)
		if req.json()["status"]=="success":
			print("[√] Done Login")
			self.t2 = req.cookies["9db306b622cf2879e24263c572efb040"]
			self.get_tt()
		else:
			print("[×] Error Login")
			self.login56()
	def get_tt(self):
		u = "https://bayitakipci.com/tools"
		he = {
    "Host": "bayitakipci.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "accept": "*/*",
    "cookie": f"_ga=GA1.2.413336954.1657374406;_gid=GA1.2.1860924705.1658811865;9db306b622cf2879e24263c572efb040={self.t2}"
}
		self.re3 = requests.get(u,headers=he).cookies["9db306b622cf2879e24263c572efb040"]
		self.qwe()
	def qwe(self):
		l = f"https://bayitakipci.com/tools/send-follower/{self.id}?formType=send"
		m = {
    "Host": "bayitakipci.com",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"_ga=GA1.2.413336954.1657374406;_gid=GA1.2.1860924705.1658811865;9db306b622cf2879e24263c572efb040={self.re3}"
}
		n = {
"adet":"100",
"userID":self.id,
"userName":self.user
}
		e = requests.post(l,headers=m,data=n).json()
		if e["status"]=="error":
			print("[×] Error Send Followers")
			self.login56()
		else:
			print("[√] Done Send Followers")
			self.login56()
	def login56(self):
		url = "https://seritakipci.com/member?"
		h = {
    "Host": "seritakipci.com",
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": "5aa121aa25e7d6d5edb088bd36123792=59743f7932a9375fd7896608816e1fe9;_ga=GA1.2.418785187.1658813716;_gid=GA1.2.377624107.1658813716;_gat=1"
}
		d = {
"username":self.username,
"password":self.password
}
		req = requests.post(url,headers=h,data=d)
		if req.json()["status"]=="success":
			self.toke = req.cookies["5aa121aa25e7d6d5edb088bd36123792"]
			print("[√] Done Login")
			self.token65()
		else:
			print("[×] Error Login")
			self.rash()
	def token65(self):
		url = "https://seritakipci.com/tools"
		he = {
    "Host": "seritakipci.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "accept": "*/*",
    "cookie": f"5aa121aa25e7d6d5edb088bd36123792={self.toke}"
	}
		self.tto = requests.get(url,headers=he).cookies["5aa121aa25e7d6d5edb088bd36123792"]
		self.ttok()
	def ttok(self):
		u = f"https://seritakipci.com/tools/send-follower/{self.id}?formType=send"
		h = {
    "Host": "seritakipci.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"5aa121aa25e7d6d5edb088bd36123792={self.tto}"
	}
		d = {
"adet":"80",
"userID":self.id,
"userName":self.user
	}
		r = requests.post(u,headers=h,data=d).json()
		print(r)
		if r["status"]=="error":
			print("[×] Error Send Followers")
			self.rash()
		else:
			print("[√] Done Send Followers")
			self.rash()
	def rash(self):
		url = "https://takipciking.com/member?"
		headers = {
    "Host": "takipciking.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": "95a6de0fa6551de723e602c2ff913007=55d4eb7a45b84013e305fda5656a2ced;_ga=GA1.2.758275655.1658891289;_gid=GA1.2.1729460594.1658891289"
		}
		data = {
"username":self.username,
"password":self.password
		}
		req = requests.post(url,headers=headers,data=data)
		if req.json()["status"]=="success":
			self.ttoo = req.cookies["95a6de0fa6551de723e602c2ff913007"]
			print("[√] Done Login")
			self.ttookk()
		else:
			print("[√] Error Login")
	def ttookk(self):
		url = "https://takipciking.com/tools"
		headers = {
    "Host": "takipciking.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"95a6de0fa6551de723e602c2ff913007={self.ttoo}"
		}
		self.ooee = requests.get(url,headers=headers).cookies["95a6de0fa6551de723e602c2ff913007"]
		self.rsh()
	def rsh(self):
		url = f"https://takipciking.com/tools/send-follower/{self.id}?formType=send"
		headers = {
    "Host": "takipciking.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36",
    "cookie": f"95a6de0fa6551de723e602c2ff913007={self.ooee}"}
		data = {
"adet":"100",
"userID":self.id,
"userName":self.user
		}
		r = requests.post(url,headers=headers,data=data).json()
		if r["status"]=="error":
			print("[×] Error Send Followers")
		else:
			print("[√] Done Send Followers")
srmd()
