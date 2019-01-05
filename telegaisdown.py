from telethon import TelegramClient, events, sync
from telethon.tl.types import InputMessagesFilterDocument
from telethon.tl.types import DocumentAttributeFilename
from telethon.tl.types import MessageMediaDocument
from telethon.errors import FloodWaitError
import os.path
import socks
import sys

v = """\


                  _           _     _                             
                 | |         | |   | |                            
  _ __   ___   __| |_   _ ___| |__ | | ____ _                     
 | '_ \ / _ \ / _` | | | / __| '_ \| |/ / _` |                    
 | |_) | (_) | (_| | |_| \__ \ | | |   < (_| |                    
 | .__/ \___/ \__,_|\__,_|___/_| |_|_|\_\__,_|                    
 | |                                                              
 |_|_           _                                                 
  / _|         | |                                                
 | |_ ___  __ _| |_                                               
 |  _/ _ \/ _` | __|                                              
 | ||  __/ (_| | |_                                               
 |_|_\___|\__,_|\__|            _____          _     _        _   
 |  __ \                       |  __ \        | |   | |      | |  
 | |  | |_   _ _ __ _____   __ | |__) |_ _ ___| |__ | | _____| |_ 
 | |  | | | | | '__/ _ \ \ / / |  ___/ _` / __| '_ \| |/ / _ \ __|
 | |__| | |_| | | | (_) \ V /  | |  | (_| \__ \ | | |   <  __/ |_ 
 |_____/ \__,_|_|  \___/ \_/   |_|   \__,_|___/_| |_|_|\_\___|\__|
                                                                  
                                                                  
                                                               

"""
print(v)

if len(sys.argv) < 2:
    sys.exit("Type channel name as arg, example: \npython3 telegaisdown.py HackingBr4sil") 

#логирование
#logging.basicConfig(level=logging.DEBUG)

# сюда перешел, свои вводные получил https://my.telegram.org
api_id = 77777777 # свой получай
api_hash = 'durovpriexalnasadovod'  #тоже свой получай

#укажи прокси, я поднял ssh туннель через putty
client = TelegramClient('session_name', api_id, api_hash, proxy=(socks.SOCKS5, 'localhost', 5555))

phone_number = '+777777777777' #свой телефон вбивай
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

channel_username = sys.argv[1] # чат\канал
# загружаем косарь сообщений. Можно увеличить/уменьшить
msgs = client.get_messages(channel_username, 1000, filter=InputMessagesFilterDocument)
for msg in msgs:
    if msg.media is not None:        
        if os.path.exists('./'+channel_username+'/'+msg.media.document.attributes[0].file_name) and os.path.getsize('./'+channel_username+'/'+msg.media.document.attributes[0].file_name) == msg.media.document.size:
            print('File: '+ msg.media.document.attributes[0].file_name + ' exists and size is ok, skipping...')
            continue
        else:
            try:
                fn = msg.media.document.attributes[0].file_name.replace('\n',' ').replace('\r', '').replace('\\', ' ')
                client.download_media(msg,file='./'+channel_username+'/'+fn)
            except FloodWaitError as e:
                print('Flood waited for', e.seconds)
                quit(1)
        print('Downloaded file: '+ msg.media.document.attributes[0].file_name)
print('Downloading complete')