from config import LOG, LOG_GROUP_ID
from StrangerMusic import app
from StrangerMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
 ━━━━━━━━━━━━━━━━━━━━━━━  
**LOVELY 𝐏𝐥𝐚𝐲 𝐋𝐨𝐠𝐠𝐞𝐫**

┏━━━━━━━━━━━━━━━━━┓
       ༺𝐂𝐡𝐚𝐭 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛      
┣★**𝐂𝐡𝐚𝐭:** {message.chat.title} [`{message.chat.id}`]
┣★**𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤:** {chatusername}
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐔𝐬𝐞𝐫:** {message.from_user.mention}

┣★**𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞:** @{message.from_user.username}
┣★**𝐈𝐝:** `{message.from_user.id}`
┏━━━━━━━━━━━━━━━━━┓
       ༺𝐏𝐥𝐚𝐲 𝐈𝐧𝐟𝐨༻
┗━━━━━━━━━━━━━━━━━┛ 
┣★**𝐒𝐞𝐚𝐫𝐜𝐡 𝐒𝐨𝐧𝐠:** {message.text}

┣★**𝐒𝐫𝐞𝐚𝐦 𝐓𝐲𝐩𝐞:** {streamtype}
━━━━━━━━━━━━━━━━━━━━━━━"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
