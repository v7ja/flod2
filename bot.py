import pyrogram
import random
from pyrogram import client
from pyrogram import *
from pyrogram.types import *
import requests,re,tgcrypto 
from time import sleep
from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
r = open("ID.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
	print("No")
	v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used')
	exit("The user is used")
while True:
	for session in open("Number.txt","r").read().split("\n"):
		if session != "":
			try:
				if session != " ":
					app = Client("ACC",api_id=27979886,api_hash="16ccb052c45daecef4ef44870eb6deb5",session_string=session)
					app.connect()
					try:
						app.set_username(o)
						qq+=1
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=
𝙵𝙸𝙶𝙷𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄𝚁 𝙳𝚁𝙴𝙰𝙼 
----------------♡ -•
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{o}
𝙲𝙻𝙸𝙲𝙺𝚂 : {qq}
𝚂𝙰𝚅𝙴 : 𝙰𝙲𝙲𝙾𝚄𝙽𝚃''')
						app.update_profile(first_name="Hi ?.")
						se = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=
•- Account Session : ❲ {session} ❳‌‌''')
					except FloodWait as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text= 〔 {qq} 〕
Wrong : {e}''')
						pass
					except BadRequest as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text= ~ ғʟᴏᴏᴅ〔 {qq} 〕
~ 𝚄𝚂𝙴𝚁 @{o}''')
					try:
						sleep(int(open("sleep.txt").read()))
					except:
						time.sleep(0.5)
			except:
				pass