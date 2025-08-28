# by: t.me/Mikthon

import random
import requests
import telethon
from telethon.sync import functions
from user_agent import generate_user_agent
from threading import Thread
import threading
import asyncio
from telethon import events
import queue

# استيراد المتغيرات الأساسية من config و help
from config import eighthon, ownersaif_id, ispay2
from help import tele_checker

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

banned = []
try:
    with open("banned.txt", "r") as f:
        f = f.read().split()
        banned.extend(f)
except FileNotFoundError:
    print("banned.txt not found. Continuing without it.")
    pass

trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]
que = queue.Queue()


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    try:
        response = requests.get(url, headers=headers)
        if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False


def gen_user(choice):
    username = ""
    if choice == "رباعي":
        c = random.choices(e)
        d = random.choices(e)
        f = [c[0], "_", d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "رباعي1":
        c = random.choices(a)
        d = random.choices(a)
        f = [c[0], "_", d[0], d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "رباعي2":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "رباعي3":
         c = random.choices(e)
         d = random.choices(e)
         f = [c[0], c[0], "_", d[0], d[0]]
         random.shuffle(f)
         username = "".join(f)
    elif choice == "رباعي4":
         c = random.choices(a)
         d = random.choices(a)
         f = [c[0], c[0], "_", d[0], d[0]]
         random.shuffle(f)
         username = "".join(f)
    elif choice == "رباعي5":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], "_", d[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    elif choice == "ثلاثي2":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    else:
        return "error"
    return username


@eighthon.on(events.NewMessage(outgoing=False, pattern=r"\.الصيد"))
async def _(event):
    sender = await event.get_sender()
    if sender.id == ownersaif_id:
        await event.reply(
        '''
**-- -- -- -- -- -- -- -- --
رباعي { s_xxx - عشوائي }
رباعي1 { s_xxx - حروف }
رباعي2 { s7_77 - ارقام }
رباعي3  { ss_77 - عشوائي }
رباعي4 { ss_xx - حروف }
رباعي5 { ss_88 - ارقام }
ثلاثي { s_c_i - عشوائي }
ثلاثي2 { s_x_7 - s_8_x }

طريقه الصيد هيه كالتالي
- .صيد + نوع الصيد تكتب الاسم 
هوه ينشأ قناة تلقائي ويفحص بيها
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
مثال: .صيد ثلاثي
---------------------------------------------------------------------- — — — —
الامر:  `.صيد` + النوع
- يقوم بصيد معرفات عشوائية حسب النوع

ٴ— — — — — — — — — —
الامر:   `.حالة الصيد`
• لمعرفة عدد المحاولات للصيد

@fcf30 

'''
    )

@eighthon.on(events.NewMessage(outgoing=False, pattern=r"\.الانواع"))
async def _(event):
    sender = await event.get_sender()
    if sender.id == ownersaif_id:
        if ispay2[0] == "yes":
            await event.reply(tele_checker)
        else:
            await event.reply("يجب الدفع لاستعمال هذا الامر !")

@eighthon.on(events.NewMessage(outgoing=False, pattern=r"\.صيد"))
async def hunterusername(event):
    sender = await event.get_sender()
    if sender.id == ownersaif_id:
        msg = event.text.split()
        choice = str(msg[1])
        try:
            ch = str(msg[2])
            if "@" in ch:
                ch = ch.replace("@", "")
            await event.reply(f"حسناً سيتم بدء الصيد في @{ch} .")
        except IndexError:
            try:
                ch = await eighthon(
                    functions.channels.CreateChannelRequest(
                        title="Prime",
                        about="Successfully arrested ✅",
                    )
                )
                ch = ch.updates[1].channel_id
                await event.reply(f"**تم انشاء القناة بنجاح .. سيتم صيد نوع {choice} !**")
            except Exception as e:
                await eighthon.send_message(
                    event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
                )
        
        isclaim.clear()
        isclaim.append("on")
        for i in range(19000000):
            username = gen_user(choice)
            if username == "error":
                await event.reply("** يرجى وضع النوع بشكل صحيح**.")
                break
            isav = check_user(username)
            if isav == True:
                try:
                    await eighthon(
                        functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username
                        )
                    )
                    await event.client.send_message(
                        event.chat_id,
                        f"⌯ تم الصيد اليوزر @{username} بالعافيه ",
                    )
                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    pass
                except Exception as baned:
                    if "(caused by UpdateUsernameRequest)" in str(baned):
                        pass
                except telethon.errors.FloodError as e:
                    await eighthon.send_message(
                        event.chat_id,
                        f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                    )
                    break
                except Exception as eee:
                    if "the username is already" in str(eee):
                        pass
                    else:
                        await eighthon.send_message(
                            event.chat_id,
                            f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                        )
                        break
            else:
                pass
            trys[0] += 1
        
        isclaim.clear()
        isclaim.append("off")
        await event.client.send_message(event.chat_id, "تم الصيد بنجاح ✅")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت"))
async def _(event):
    msg = event.text.split()
    try:
        username = str(msg[1])
        ch = str(msg[2])
        await event.reply(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except IndexError:
        try:
            username = str(msg[1])
            ch = await eighthon(
                functions.channels.CreateChannelRequest(
                    title="Prime - صيد اندرو",
                    about="Successfully arrested ✅",
                )
            )
            ch = ch.updates[1].channel_id
            await event.reply(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await eighthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    
    isauto.clear()
    isauto.append("on")
    
    for i in range(1000000000000):
        isav = check_user(username)
        if isav == True:
            try:
                await eighthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n- By : @none !\n- Hunting Log {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                break
            except telethon.errors.FloodError as e:
                await eighthon.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await eighthon.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                break
        else:
            pass
        trys2[0] += 1
        await asyncio.sleep(1.3)
    
    isclaim.clear()
    isclaim.append("off")
    await eighthon.send_message(event.chat_id, "**- تم الانتهاء من التثبيت بنجاح**")


@eighthon.on(events.NewMessage(outgoing=False, pattern=r"\.حالة الصيد"))
async def _(event):
    sender = await event.get_sender()
    if sender.id == ownersaif_id:
        if "on" in isclaim:
            await event.reply(f"** الصيد وصل لـ({trys[0]}) من المحاولات**")
        elif "off" in isclaim:
            await event.reply("** الصيد  لا يعمل .**")
        else:
            await event.reply("- لقد حدث خطأ ما وتوقف الامر لديك")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isauto:
        await event.reply(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.reply("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.reply("-لقد حدث خطأ ما وتوقف الامر لديك")

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.ت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        trys_local = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.reply(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

            @eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة ت "))
            async def _(event):
                if "on" in isauto:
                    await event.reply(f"التثبيت وصل لـ({trys_local}) من المحاولات")
                elif "off" in isauto:
                    await event.reply("لايوجد تثبيت شغال !")
                else:
                    await event.reply("خطأ")
            
            for i in range(int(msg[0])):
                if ispay2[0] == 'no':
                    break
                
                t = Thread(target=lambda q, arg1: q.put(check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()

                if "Available" in isav:
                    try:
                        await eighthon(functions.channels.UpdateUsernameRequest(channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''** ⌯ We are the strongest !'
⎱ UserName: ↣ (@{username}❳!
⎱ by : @none **
''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:
                        await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
الخطأ :
{str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                
                trys_local += 1
                await asyncio.sleep(0.1)
            
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await eighthon.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        
        if msg[0] == "يدوي":
            username = str(msg[0])
            ch = str(msg[1])
            await event.reply(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            try:
                await eighthon(functions.channels.UpdateUsernameRequest(channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''**
⌯ We are the strongest !'
⎱ UserName: ↣ (@{username}❳!
⎱ by : @none
-- -- -- -- -- -- -- -- -- -- -- -- -- **
''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
الخطأ :
{str(eee)}''')