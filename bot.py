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
          await app.update_profile(first_name="ᥲხ᥆᥆ძ ᥡᥲხɦ #1")
          await
app.update_profile(bio="α𝖻᥆᥆ძ - ᥒᥙ𝗆𝖻𝖾𝗋 1 , 𝗍h𝖾 𝗌𝗍𝗋᥆ᥒ𝗀 , @ToGoLang🐊 ,")
						qq+=1
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=𝑰𝒔 𝒂 𝑵𝒆𝒘 𝒖𝒔𝒆𝒓 𝑩𝒚 : 𝒂𝑩𝒐𝒐𝑫 𝒀𝒂𝑩𝒉 🐊,
এ〔 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆 〕: @{o}
এ〔 𝑪𝒍𝒊𝒄𝒌𝒔 〕: {qq}
এ〔 𝑺𝒂𝒗𝒆 〕: 𝑨𝒄𝒄𝒐𝒖𝒏𝒕
এ〔 𝑪𝒉 〕: @ToGoLang''')
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
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text= ~ 𝖿𝗅᥆᥆ძ〔 {qq} 〕
~ 𝗎𝗌𝖾𝗋 @{o}''')
					try:
						sleep(int(open("sleep.txt").read()))
					except:
						time.sleep(0.5)
			except:
				pass