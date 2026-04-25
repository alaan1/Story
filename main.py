# -*- coding: utf-8 -*-
from pyrogram import Client ,idle,errors,enums
from pyrogram.filters import command,text,private,regex ; from logging import INFO , debug , error ; from re import findall
from random import choice
from pyrogram.errors import PeerIdInvalid
from pyrolistener import Listener, exceptions
from asyncio import create_task, get_event_loop
from pyrogram.errors import FloodWait 
from kvsqlite.sync import Client as Story
from telethon.sync import TelegramClient
import pytz
from telethon.sessions import StringSession
from pyrogram.types import (Message,CallbackQuery,ForceReply,InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button) 
from datetime import date
from pyrogram.raw.types import InputPeerUser,InputPeerChat
import logging , asyncio ,re, tempfile
from pyrogram import raw, types
from telethon import functions
from os import remove
from httpx import Timeout
db = Story("Story-Tele.Sqlite")

api_id = 7706053
api_hash = "a87b492b8fe379c5fd63793d29ca7a27"

alEx = Client(name="Story-Bot-Tlegram",api_id=7706053,api_hash="a87b492b8fe379c5fd63793d29ca7a27",bot_token="7559044920:AAESGsfymy5CkGpMhGE8bJeftcBLsBasrJ8")
            
session1_str = "1ApWapzMBu3rXajTaXD-x6dww1AsHW2zEFCmJd9T1RwkPGYi9KTHAPSR1ow5_B25Nx9wxdwSF3gML1N-sQ5yMJaydJSYBPGmq9_ieAVNeLZlWPaQmrQhj1yvbesYSvU-cEChq9QYaedM4wBGDY_ctTJSIfS1xgtzdAB4T0T3RibSxdgLCCuir4qMlqER6ONnovsYlUB-TNZ7wQzl-zf-9cPQ8rAKJ3ji2YKBtddkdHiUvD8vvvD0jMY-TmZFk5AZdTg30OWxzBvFkguBVy3HwXCbMbp30qt_EcAzqzoqo5lpEPVjt3mWSDo3yrgPKQnPUQYvi9ry4d6Q4twTr2Z8VHNZOzFBoEnE="
session2_str = "1ApWapzMBu2o6ERGlw1m5UMb-P5ne9xZhXMe-PKfmbuIKZd4AMPWrPrlJ-HvQ3nHhT9nTMi_iYQY8GNXYHzLNwBpjhv0wrdtHosDM5S8KBgXQf1iDqm_oCgzg8HqvIdXWPTAErXXMiTmBlMyJtU3rogp9Ilb66A1M2FBYJdWTReOAU7DW28hiF0aykd9-LG357TV3h2Rg-GxIz4-ZVb6Rqhl-JctE2kOvrmyexonDAXMsWSGVXTIP-qLlxzUIIAorqtb0662hCOteEUlTdsAIIKbyhpVTT-QUfu7MXrZjN4Vz-7FhUBu6LwQj5MTbvaF9t3EcnNAlmGEF6LrkBfuMwD_epNm8b7E="
session3_str = "1BJWap1sBu6sJtbvC1-KmC9Nw7YstOZk17DVeSgB7_lNmHOuTnMvgc5tVogDnIO0L6-fy98U3jL5YoohFWmF6PNyoVfzgbeH7QFwhGA1IHUtkwAS3zxSvJqEWYdKER8pyuv27_uqA_I6HoxzmoS84z53AzYV0ZVwlfEBEhGNzRqbe3dwwGCSK_H_vF_OYsCQTFae5yhLSgxa1oD5yhorHS_TO833OwlGNln16mn7jv5WqjENYajkAYaYq_wLs9ozDG_cB2i2XMgCUc0wptTdnjTVZFrmL2qnHPU_XwW-TrMt8yGpuQet5cQQDcGKRtO9QhOB3LdL8n9auSz7m3wuGrsyEJwzhsQI="
session4_str = "1AZWarzsBu6AOdKgpubNGVnUEXfltcfcatLOTI1MJiUeMGi38aeU1rJZQ_C0OrCWa8GKPAjxl8HxQTqJ7aFevBJ7v5yf2MZ8lH0Jc7wBITS9UftZypsq_SfSjFhKrxTybfl3-_TToAYix7kmaADU_heYo424UQRoIRr4H0YuPM6yTiQKy9sHDNVLOLO96cMJIb7JJauYQXR1KQ39PARSFbHvTiYjZuLkw1YbOVi9r0cDUjgKj62uWbKcbq_U-FDy0DuouXJhZlQH6xZ7-2-D1YriwXdvG3w4QGtPa1rE56DPNPw6izSwY35jB4D2PogFqZ4LDonWvoweUmpdRGePjP06Umy1Auts="
session5_str = "1AZWarzMBu1cCt4ExRO2d-Ud2klvkelO1C5B7UVB-ddndtK6PDoBZwRYk2BqnMo8ObwTX2jPaZ2bsoHiaWTU-hC6xB95zS2BtoHezMjJBYCTWtgeQbz0ii5BOLQ03rzdtYPdHQ2rSK-v77gRfuemQr4YNe_uqo9z3WeYvSS2H1xJusofIsLpDLYTvubAN5mrecgsplFkE7rAjrsqmC7Ksinka9dHEVFinbAJoSFZlTL6S9B0G3kWvXDWUnC88GrKZb96QguLngscxqPIDWUSIRDyM33gygrJ7AKytkXDHndte_7B-nWAuVnt0dH9PFvaFneRbUFBjS4uOc6wohe41518sGIDtvHU="
client1 = TelegramClient(StringSession(session1_str), api_id, api_hash)
client2 = TelegramClient(StringSession(session2_str), api_id, api_hash)
client3 = TelegramClient(StringSession(session3_str), api_id, api_hash)
client4= TelegramClient(StringSession(session4_str), api_id, api_hash)
client5= TelegramClient(StringSession(session5_str), api_id, api_hash)
#print(pick_session) 
if db.exists('USERS') == False:
	db.set('USERS',[])

channel , Owner = "@teAmrecode", 2067261869


# تم حذف الكود السابق لتشغيل الجلسات واستبداله بكود دائم

loop , listener = get_event_loop() , Listener(client = alEx)

import random
def pick_session(user_id=None):
    sessions = [client1, client2, client3,client4,client5]
    return random.choice(sessions)
async def start_telethon_sessions():
    active_clients = []

    try:
        await client1.connect()
        if await client1.is_user_authorized():
            print("✅ الجلسة 1 تعمل")
            active_clients.append(client1)
        else:
            print("⚠️ الجلسة 1 منتهية أو غير صالحة، تجاهل تشغيلها")
    except Exception as e:
        print(f"خطأ في الجلسة 1: {e}")

    try:
        await client2.connect()
        if await client2.is_user_authorized():
            print("✅ الجلسة 2 تعمل")
            active_clients.append(client2)
        else:
            print("⚠️ الجلسة 2 منتهية أو غير صالحة، تجاهل تشغيلها")
    except Exception as e:
        print(f"خطأ في الجلسة 2: {e}")
    try:
        await client3.connect()
        if await client3.is_user_authorized():
            print("✅ الجلسة 3تعمل")
            active_clients.append(client3)
        else:
            print("⚠️ الجلسة 1 منتهية أو غير صالحة، تجاهل تشغيلها")
    except Exception as e:
        print(f"خطأ في الجلسة 1: {e}")
    try:
        await client4.connect()
        if await client4.is_user_authorized():
            print("✅ الجلسة 4 تعمل")
            active_clients.append(client4)
        else:
            print("⚠️ الجلسة 4 منتهية أو غير صالحة، تجاهل تشغيلها")
    except Exception as e:
        print(f"خطأ في الجلسة 1: {e}")
    try:
        await client5.connect()
        if await client5.is_user_authorized():
            print("✅ الجلسة 4 تعمل")
            active_clients.append(client5)
        else:
            print("⚠️ الجلسة 4 منتهية أو غير صالحة، تجاهل تشغيلها")
    except Exception as e:
        print(f"خطأ في الجلسة 1: {e}")
    return active_clients   # ✅ يرجع list مو bool

async def keep_telethon_alive():
    await asyncio.gather(
        client1.run_until_disconnected(),
        client2.run_until_disconnected(),
        client3.run_until_disconnected(),
        client4.run_until_disconnected(),
        client5.run_until_disconnected()
        
    )
listener = Listener(client = alEx)

async def CheckSubscibe(message):
    try:
        msg_id = message.message.id
    except AttributeError:
        msg_id = message.id

    user_id = message.from_user.id
    name = message.from_user.first_name

    # القناة الأساسية
    main_channel = "@TeamRecode"

    # جلب القنوات من قاعدة البيانات
    channels = db.get("channels") or []
    if main_channel not in channels:
        channels.append(main_channel)

    not_subscribed = []
    for ch in channels:
        try:
            await alEx.get_chat_member(ch, user_id)
        except:
            not_subscribed.append(ch)

    if not not_subscribed:
        return True

    # إذا مو مشترك في بعض القنوات ❌
    buttons = [
        [Button(ch, url=f"https://t.me/{ch.strip('@')}")]
        for ch in not_subscribed
    ]

    return await alEx.send_message(
        user_id,
        f"• أهلين [{name}](tg://settings)\n\n~ لازم تشترك بهالقنوات حتى تكدر تكمل 👇",
        reply_markup=Markup(buttons)
    )
	
@alEx.on_message(command('start') & private)
async def StartBot(_:Client,message:Message):
		if str(message.chat.id) not in str(db.get('USERS')):
			try:
				await alEx.send_message(Owner,f'''
	**
	- تم دخول شخص جديد 🪔 .
	```
	~_~_~_~_~_~_~_~_~_~_~```
	- أسم المستخدم : **[ {message.from_user.mention} ]** .
	- يوزر المستخدم : **{"@"+message.from_user.username if message.from_user.username else "None"}** .
	- تاريخ : **{date.today()}** .
	
	''',reply_markup=Markup([[Button(message.from_user.first_name,user_id=message.from_user.id)]]))
			except:
				await alEx.send_message(Owner,f'''
	**
	- تم دخول شخص جديد 🪔 .
	```
	~_~_~_~_~_~_~_~_~_~_~```
	- أسم المستخدم : **[ {message.from_user.mention} ]** .
	- يوزر المستخدم : **{"@"+message.from_user.username if message.from_user.username else "None"}** .
	- تاريخ : **{date.today()}** .''')
			Users = db.get('USERS')
			Users.append(message.chat.id)
			db.set('USERS',Users)
		if message.chat.id == Owner:
			await alEx.send_message(message.chat.id,'''
	~ اهلا ( alEx ) يمكنك التحكم بأعدادات البوت من هنا !
	
	- من خلال الأزرار ادناه ↓ .
	
	```
	- Join ...```
	''',reply_markup=Markup([[Button('( جلب التخزين )',callback_data='GetFileBot')],[Button('( وضع سيشن 1 )',callback_data='InterSession1'),Button('( وضع سيشن 2 )',callback_data='InterSession2')],[Button('( إذاعه )',callback_data='SendMessages')],[Button("( إضافة قناة اشتراك )",callback_data='AddChannel'),Button("( حذف قناة إشتراك إجباري )",callback_data="deleteChannel")],[Button("( قنوت الاشتراك )",callback_data="Channels")]]))
		
		if message.chat.id == Owner or await CheckSubscibe(message) == True:
			await alEx.send_photo(chat_id=message.chat.id,photo='https://h.top4top.io/p_3214anj060.jpg',caption='''
			↯︙بوت اختصاصي تحميل ( قصص ) حسابات التليكرام .
	↯︙يمكنك ايضا تحميل الميديا وسحب النصوص من القنوات العامه المُقيده !
	↯︙فقط قم بأرسال معرف الحساب أو ايدي الحساب .
	- Join -_- 
	''',reply_markup=Markup([[Button('( قناة السورس )',url='http://t.me/TeamReCode')]]),reply_to_message_id=message.id)
@alEx.on_callback_query(regex(r"^(Channels)$"))
async def Channels(_: Client, callback: CallbackQuery):
	    user_id = callback.from_user.id
	    reply = await alEx.send_message(text="هذه قنوات الاشتراك الاجباري :",chat_id=user_id)
	    channels = db.get("channels")
	    channels.append("@TeamRecode")
	    Mark = []
	    for _ in channels:
	    	Mark.append([Button(text=_,url=f"https://t.me/{_.strip('@')}")])
	    	await alEx.edit_message_reply_markup(chat_id=callback.message.chat.id,message_id=reply.id,reply_markup=Markup(Mark))
	    	

@alEx.on_callback_query(regex(r"^(deleteChannel)$"))
async def DeleteChannel(_: Client, callback: CallbackQuery):
	    user_id = callback.from_user.id
	    lmsg = await callback.message.reply(text=f'''
	```
	- أرسل القناه بهذا الشكل ( @TeamReCode ) .```
	**- ( /cancel )**
	''',reply_to_message_id=callback.message.id)
	    try:
		        ask = await listener.listen(
		        from_id=user_id,
		        chat_id=user_id,
		        reply_markup=ForceReply(selective=True, placeholder="[ Channel ]"),
		        timeout=50)
	    except exceptions.TimeOut:
	         return await lmsg.edit_text('''
	```
	- انتهى وقت الاستلام .```
	 ''' ,reply_markup=Markup([[Button("• باك •",callback_data="BackAd")]]))
	    await callback.message.delete()
	    if ask.text == "/cancel":
	        return await  ask.reply('''
	🧚
	''', reply_to_message_id=ask.id,reply_markup = Markup([[Button("باك", callback_data="BackAd")]]))
	    else:
	    	db.set("channels",[]) if db.exists("channels") == False else ""
	    	channels = db.get("channels")
	    	print(channels)
	    	channels.remove(ask.text)
	    	db.set("channels",channels)	
	    	reply = await ask.reply("- تم حذف قناة الاشتراك الاجباري !",quote=True)
	    	

@alEx.on_callback_query(regex(r"^(AddChannel)$"))
async def AddChannel(_: Client, callback: CallbackQuery):
	    user_id = callback.from_user.id
	    lmsg = await callback.message.reply(text=f'''
	```
	- أرسل القناه بهذا الشكل ( @TeamReCode ) .```
	**- ( /cancel )**
	''',reply_to_message_id=callback.message.id)
	    try:
		        ask = await listener.listen(
		        from_id=user_id,
		        chat_id=user_id,
		        reply_markup=ForceReply(selective=True, placeholder="[ Channel ]"),
		        timeout=50)
	    except exceptions.TimeOut:
	         return await lmsg.edit_text('''
	```
	- انتهى وقت الاستلام .```
	 ''' ,reply_markup=Markup([[Button("• باك •",callback_data="BackAd")]]))
	    await callback.message.delete()
	    if ask.text == "/cancel":
	        return await  ask.reply('''
	🧚
	''', reply_to_message_id=ask.id,reply_markup = Markup([[Button("باك", callback_data="BackAd")]]))
	    else:
	    	db.set("channels",[]) if db.exists("channels") == False else ""
	    	channels = db.get("channels")
	    	print(channels)
	    	channels.append(ask.text)
	    	db.set("channels",channels)
	    	
	    	reply = await ask.reply("- تم إضافة قناة اشتراك الاجباري !",quote=True)

@alEx.on_callback_query(regex(r"^(SendMessages)$"))
async def Stats(_: Client, callback: CallbackQuery):
	    user_id = callback.from_user.id
	    lmsg = await callback.message.reply(text=f'''
	```
	- أرسل النص او الصوره او فيديو او اي شيء  :```
	**- ( /cancel )**
	''',reply_to_message_id=callback.message.id,reply_markup=Markup([[Button('🧚',url="https://t.me/M_L_F")]]))
	    try:
		        ask = await listener.listen(
		        from_id=user_id,
		        chat_id=user_id,
		        reply_markup=ForceReply(selective=True, placeholder="[ ID ]"),
		        timeout=50)
	    except exceptions.TimeOut:
	         return await lmsg.edit_text('''
	```
	- انتهى وقت الاستلام .```
	 ''' ,reply_markup=Markup([[Button("• باك •",callback_data="BackAd")]]))
	    await callback.message.delete()
	    if ask.text == "/cancel":
	        return await  ask.reply('''
	🧚
	''', reply_to_message_id=ask.id,reply_markup = Markup([[Button("باك", callback_data="BackAd")]]))
	    else:
	        text = "**— جاري إرسال الإذاعة إلى المستخدمين**\n"
	        reply = await ask.reply(text,quote=True)
	        count = 0
	        for H in db.get('USERS'):
	                try:          
	                    count +=1
	                    await ask.copy(H)
	                    await reply.edit(text+f"**— تم ارسال الإذاعة الى [ {count}/{len(db.get('USERS'))} ] مستخدم**")
	                    await asyncio.sleep(2)
	                except FloodWait as x:
	                    await asyncio.sleep(x.value)
	                except:
	                    pass
	                    
	
@alEx.on_message(private & text & regex(r"t.me\/([^\/]+)\/(\d+)"))
async def GetPostChannel(client, message):
		Match = re.search(r"t.me\/([^\/]+)\/(\d+)", message.text)
		channel_username, message_id = Match.groups()
		try:
		    await alEx.get_chat(channel_username)
		    Get_Message = await alEx.get_messages(channel_username,int(message_id))
		    Send = await alEx.send_photo(message.chat.id,Get_Message.photo.file_id,caption=Get_Message.caption if Get_Message.caption else "" ) if Get_Message.photo else ""
		except :
		    pass
		    
		if Send:
			Wait = await alEx.send_message(message.chat.id,'[•]  سيتم حذفه تلقائيا بعد ٥٠ ثانيه !',reply_to_message_id=Send.id)
			await asyncio.sleep(49)
			await alEx.delete_messages(message.chat.id,[Send.id,Wait.id])
		Send = await alEx.send_audio(message.chat.id,Get_Message.audio.file_id,caption=Get_Message.caption if Get_Message.caption else "") if Get_Message.audio else ""
		if Send:
			Wait = await alEx.send_message(message.chat.id,'[•]  سيتم حذفه تلقائيا بعد ٥٠ ثانيه !',reply_to_message_id=Send.id)
			await asyncio.sleep(49)
			await alEx.delete_messages(message.chat.id,[Send.id,Wait.id])
		Send = await alEx.send_voice(message.chat.id,Get_Message.voice.file_id,caption=Get_Message.caption if Get_Message else "") if Get_Message.voice else ""
		if Send:
			Wait = await alEx.send_message(message.chat.id,'[•]  سيتم حذفه تلقائيا بعد ٥٠ ثانيه !',reply_to_message_id=Send.id)
			await asyncio.sleep(49)
			await alEx.delete_messages(message.chat.id,[Send.id,Wait.id])
		Send = await alEx.send_video(message.chat.id,Get_Message.video.file_id,caption=Get_Message.caption if Get_Message.caption else "") if Get_Message.video else ""
		if Send:
			Wait = await alEx.send_message(message.chat.id,'[•]  سيتم حذفه تلقائيا بعد ٥٠ ثانيه !',reply_to_message_id=Send.id)
			await asyncio.sleep(49)
			await alEx.delete_messages(message.chat.id,[Send.id,Wait.id])
		Send = await alEx.send_document(message.chat.id,Get_Message.document.file_id,caption=Get_Message.caption if Get_Message.caption else "") if Get_Message.document else ""
		if Send:
			Wait = await alEx.send_message(message.chat.id,'[•]  سيتم حذفه تلقائيا بعد ٥٠ ثانيه !',reply_to_message_id=Send.id)
			await asyncio.sleep(49)
			await alEx.delete_messages(message.chat.id,[Send.id,Wait.id])
		Send = await alEx.send_animation(message.chat.id,Get_Message.animation.file_id,caption=Get_Message.caption if Get_Message.caption else "") if Get_Message.animation else ""
		if Send:
			Wait = await alEx.send_message(message.chat.id,'[•]  سيتم حذفه تلقائيا بعد ٥٠ ثانيه !',reply_to_message_id=Send.id)
			await asyncio.sleep(49)
			await alEx.delete_messages(message.chat.id,[Send.id,Wait.id])
		Send = await alEx.send_message(message.chat.id,Get_Message.text) if Get_Message.text else ""
		if Send:
			Wait = await alEx.send_message(message.chat.id,'[•]  سيتم حذفه تلقائيا بعد ٥٠ ثانيه !',reply_to_message_id=Send.id)
			await asyncio.sleep(49)
			await alEx.delete_messages(message.chat.id,[Send.id,Wait.id])
			
@alEx.on_message(private & text & regex(r"^(@[a-zA-Z0-9_]+|\d+)$"))
async def GetStoryAccount(client, message):
		if await CheckSubscibe(message) == True:
		    pass
		else:
		    return
		db.set(f"{message.chat.id}-Story",message.text)
		try:	
			Chat = await alEx.get_chat(message.text)
			if Chat.photo:
				d = await client.download_media(Chat.photo.big_file_id,in_memory=True)
				return await alEx.send_photo(message.chat.id,d,caption='Story Tele ! \n**~ أختر ماتريد تحميله ...'+f'''
	~ ألبايو : 
	```
	{Chat.bio}```''' if Chat.bio else "",reply_markup=Markup([[Button('( الستوريات الحديثه )',callback_data='StoryNow'),Button('( الستوريات المثبته )',callback_data='StoryPin')]]));db.set(f"{message.chat.id}-Story",message.text)
			else:
				return await alEx.send_message(message.chat.id,f'''
	Story Tele !
	
	~ أختر ماتريد تحميله ...
	~ ألبايو : 
	```
	{Chat.bio}```''' if Chat.bio else '''
	Story Tele !
	
	~ أختر ماتريد تحميله ...
	''',reply_markup=Markup([[Button('( الستوريات الحديثه )',callback_data='StoryNow'),Button('( الستوريات المثبته )',callback_data='StoryPin')]]));db.set(f"{message.chat.id}-Story",message.text)
		except PeerIdInvalid:
			return await alEx.send_message(message.chat.id,'- يجب ان يكون المستخدم في البوت لكي اجد معلوماته عبر الادي .\n- أرسل المعرف المستخدم بدلا من الايدي ❗',reply_to_message_id=message.id)
		except:
				alExRandomSession = pick_session(message.chat.id)
				user = await alExRandomSession.get_entity(message.text)
				if user.photo :
					d = await alExRandomSession.download_profile_photo(user)
					await alEx.send_photo(message.chat.id,d,caption='Story Tele ! \n**~ أختر ماتريد تحميله ...',reply_markup=Markup([[Button('( الستوريات الحديثه )',callback_data='StoryNow'),Button('( الستوريات المثبته )',callback_data='StoryPin')]]));db.set(f"{message.chat.id}-Story",message.text);db.set(f"{message.chat.id}-Story",message.text)
					remove(d)
					
				else:
					return await alEx.send_message(message.chat.id,f'''
	Story Tele !
	
	~ أختر ماتريد تحميله ...
	''',reply_markup=Markup([[Button('( الستوريات الحديثه )',callback_data='StoryNow'),Button('( الستوريات المثبته )',callback_data='StoryPin')]]));db.set(f"{message.chat.id}-Story",message.text)
			
@alEx.on_callback_query(regex(r"^(StoryNow)$"))
async def StoryNow(_: Client, callback: CallbackQuery):
		if await CheckSubscibe(callback) == True:
			alExRandomSession = pick_session(callback.from_user.id)
			try:
					Check = await alExRandomSession(functions.stories.GetPeerStoriesRequest(db.get(f"{callback.from_user.id}-Story")))
			except Exception as e:
					return await alEx.send_message(callback.from_user.id,'- يجب ان يكون المستخدم في البوت لكي اجد معلوماته عبر الادي .\n- أرسل المعرف المستخدم بدلا من الايدي ❗',reply_to_message_id=callback.message.id)
			if Check.stories.stories == []:
					return await alEx.send_message(callback.from_user.id,f'↯︙الحساب لم يضع ستوريات حديثه او قد تكون خاصه ❗ .',reply_markup=Markup([[Button('( قناة السورس )',url='http://t.me/TeamReCode')]]),reply_to_message_id=callback.message.id)
			else:
						await callback.answer("- أنتضر ..", show_alert=True)
					
						create_task(Upload1(Client,callback.from_user.id,db.get(f"{callback.from_user.id}-Story"),alExRandomSession))
	
@alEx.on_callback_query(regex(r"^(StoryPin)$"))
async def StoryPin(_: Client, callback: CallbackQuery):
		if await CheckSubscibe(callback) == True:
			alExRandomSession = pick_session(callback.from_user.id)
			try:
					Check = await alExRandomSession(functions.stories.GetPinnedStoriesRequest(db.get(f"{callback.from_user.id}-Story"),offset_id=42,limit=20))
			except Exception as e:
					print(e)
					return await alEx.send_message(callback.from_user.id,'- يجب ان يكون المستخدم في البوت لكي اجد معلوماته عبر الادي .\n- أرسل المعرف المستخدم بدلا من الايدي ❗',reply_to_message_id=callback.message.id)
			if Check.count == 0:
					return await alEx.send_message(callback.from_user.id,f'↯︙الحساب لم يضع ستوريات او قد تكون خاصه ❗ .',reply_markup=Markup([[Button('( قناة السورس )',url='http://t.me/TeamReCode')]]),reply_to_message_id=callback.message.id)
					
			else :
					await callback.answer("- أنتضر ..", show_alert=True)
					return create_task(Upload2(Client,callback.from_user.id,db.get(f"{callback.from_user.id}-Story"),alExRandomSession))				
					
async def Upload2(client,user_id,ID,alExRandomSession):
		
			Check = await alExRandomSession(functions.stories.GetPinnedStoriesRequest(ID,offset_id=42,limit=20))
			print(Check.stories)
			for Pin in Check.stories:
				S = await alExRandomSession.download_media(Pin.media)
				await alEx.send_document(chat_id=user_id,document=S)
				remove(S)
				await asyncio.sleep(int(choice([1,3])))
				
async def Upload1(client,user_id,ID,alExRandomSession):
		
			Check = await alExRandomSession(functions.stories.GetPeerStoriesRequest(ID))
			for Story in Check.stories.stories:
				S = await alExRandomSession.download_media(Story.media)
				await alEx.send_document(chat_id=user_id,document=S)
				remove(S)
				await asyncio.sleep(int(choice([1,3])))
				
@alEx.on_callback_query(regex(r"^(InterSession1)$"))
async def InterSession1(_: Client, callback: CallbackQuery):
	    if callback.from_user.id == Owner:
	    	user_id = callback.from_user.id
	    	await callback.message.delete()
	    	try:	        
		        ask = await listener.listen(
		        from_id=user_id,
		        chat_id=user_id,
		        text="أرسل الجلسه الآن ( تليثون ) .",
		        reply_markup=ForceReply(selective=True, placeholder=" ضع الجلسه هنا وأرسل .."),
		        timeout=60)
	    	except exceptions.TimeOut:
		        
		        return await callback.message.reply(
		        text = "- نفد وقت استلام الجلسه .",
		        reply_markup = Markup([[Button("باك", callback_data="Back")]])
		    )
	    	if ask.text == "/cancel":
		    	return await ask.reply("🧚", reply_to_message_id=ask.id,reply_markup = Markup([[Button("• باك •", callback_data="Back")]]))
	    	create_task(AddSession1(ask))
	
async def AddSession1(message:Message):
		await message.reply("- تم حفظ الجلسه الأولى !",reply_to_message_id=message.id)if len(message.text) > 20 else await message.reply("- تأكد من الجلسه اولا !، يجب ان تكون بايروكرام ..",reply_to_message_id=message.id) 	
		db.set("Session1",message.text) if len(message.text) > 20 else ""
	
@alEx.on_callback_query(regex(r"^(InterSession2)$"))
async def InterSession2(_: Client, callback: CallbackQuery):
	    if callback.from_user.id == Owner:
	    	user_id = callback.from_user.id
	    	await callback.message.delete()
	    	try:	        
		        ask = await listener.listen(
		        from_id=user_id,
		        chat_id=user_id,
		        text="أرسل الجلسه الآن ( تليثون ) .",
		        reply_markup=ForceReply(selective=True, placeholder=" ضع الجلسه هنا وأرسل .."),
		        timeout=60)
	    	except exceptions.TimeOut:
		        
		        return await callback.message.reply(
		        text = "- نفد وقت استلام الجلسه .",
		        reply_markup = Markup([[Button("باك", callback_data="Back")]])
		    )
	    	if ask.text == "/cancel":
		    	return await ask.reply("🧚", reply_to_message_id=ask.id,reply_markup = Markup([[Button("• باك •", callback_data="Back")]]))
	    	create_task(AddSession2(ask))
	
async def AddSession2(message:Message):
		await message.reply("- تم حفظ الجلسه الثانيه !",reply_to_message_id=message.id)if len(message.text) > 20 else await message.reply("- تأكد من الجلسه اولا !، يجب ان تكون بايروكرام ..",reply_to_message_id=message.id) 	
		db.set("Session2",message.text) if len(message.text) > 20 else ""
		
@alEx.on_callback_query(regex(r"^(GetFileBot)$"))
async def TrueGetMoney(_: Client, callback: CallbackQuery):
		await callback.answer("- أنتضر ..", show_alert=True)
		await alEx.send_document(chat_id=Owner,document=open('Story-Tele.Sqlite','rb'),caption='- ملف تخزين البوت .')




import asyncio, os, traceback
from pyrogram import Client, idle
import random

async def pyrogram_runner():
    while True:
        try:
            if not alEx.is_connected:   # ✅ تأكد أنه غير متصل
                await alEx.start()
                print("✅ Bot Started")

            await idle()   # ينتظر الأحداث
        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            try:
                if alEx.is_connected:   # ✅ أوقفه فقط إذا كان شغال
                    await alEx.stop()
                    print("🛑 Bot Stopped")
            except:
                pass

            print("♻️ Restarting Pyrogram Bot after 5s...")
            await asyncio.sleep(5)  
async def telethon_runner():
    while True:
        try:
            active_clients = await start_telethon_sessions()
            if not active_clients:
                print("❌ ماكو أي جلسة صالحة، انتظر 60 ثانية وحاول مرة ثانية")
                await asyncio.sleep(60)
                continue

            await asyncio.gather(*[c.run_until_disconnected() for c in active_clients])
        except Exception as e:
            traceback.print_exc()
            await asyncio.sleep(5)

async def main():
    pyrogram_task = asyncio.create_task(pyrogram_runner())
    telethon_task = asyncio.create_task(telethon_runner())

    await pyrogram_task
    await telethon_task


if __name__ == "__main__":
    loop.run_until_complete(main())
