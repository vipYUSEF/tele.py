from os import system, name, path
from time import sleep
from random import choice
from base64 import b64decode
try:
    from requests import get
except:
    
    from requests import get
try:
    from telethon import TelegramClient, sync, errors, functions, types
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
except:
    
    from telethon import TelegramClient, sync, errors, types, functions
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
try:
    from bs4 import BeautifulSoup as S
except:
    
    from bs4 import BeautifulSoup as S
try:
    from fake_useragent import UserAgent
except:
    
    from fake_useragent import UserAgent
try:
	from datetime import datetime
except:
	
	from datetime import datetime
def clear():
	system('cls' if name=='nt' else 'clear')
def channels2(client, username):
    di = client.get_dialogs()
    for chat in di:
        if chat.name == f'Updated!' and not chat.entity.username:
            client(functions.channels.DeleteChannelRequest(channel=chat.entity))
            return False
    return True
def fragment(username):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': UserAgent().random,
}
    response = get(f'https://fragment.com/username/{username}', headers=headers)
    soup = S(response.content, 'html.parser')
    ok = soup.find("meta", property="og:description").get("content")
    if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name with blockchain in an ecosystem of 700+ million users" in ok:return True
    elif "is taken" in ok:return "is taken"
    else:return False
def telegram(client,claim,username):
	if claim:
		text = f" A new username has been found - @{username} • Owner @ivvvivv \n"
		try:print("-")
		except:pass
	else:
		text = f"- @ivvvivv\n"
	client.send_message('me',text)
def climed(client,username):
    result = client(functions.channels.CreateChannelRequest(
		title=f'ثروڤس | Throofs',
        about=f'@{username} - Username for @ivvvivv',
        megagroup=False))
    try:
        client(functions.channels.UpdateUsernameRequest(
        channel=result.chats[0],
        username=username))
        client.send_message(username,f'Username for @ivvvivv \n')
        return True
    except Exception as e:client.send_message('');return False
# for checking username
def checker(username,client):
		try:
			check = client(CheckUsernameRequest(username=username))
			if check:
				print(' \033[2;32mavailable - '+username+' '+"")
				claimer = climed(client,username)
				if claimer and fragment(username) == "is taken":claim = True
				else:claim = False
				
				telegram(client,claim,username)
				flood = channels2(client,username)
				if not flood:
					with open('flood.txt', 'a') as floodX:
						floodX.write(username + "\n")
			else:
				print('• UserName ['+username+' .'+"] , Taken.")
		except errors.rpcbaseerrors.BadRequestError:
			print(' Forbidden - '+username+" ")
			open("banned4.txt","a").write(username+'\n')
		except errors.FloodWaitError as timer:
			print('• Flood ['+timer.second+' .'+"] , Taken")
		except errors.UsernameInvalidError:
			print('- Error UserName : '+username+' .')
# for generate username
def usernameG():
	q = ''.join(choice('zxcvnmasweruio') for i in range(1))
	w = ''.join(choice('oiurewaszxcvnm') for i in range(1))
	e = ''.join(choice('PItlKJHGFDSA') for i in range(1))
	r = ''.join(choice('qwertyuioplkjhgfdsazxcvbnm') for i in range(1))
	t = ''.join(choice('1234567890') for i in range(1))
	y = ''.join(choice('zxcvnmasweruio') for i in range(1))
	u = ''.join(choice('oiurewaszxcvnm') for i in range(1))
	v1 = y+y+y+y+y+u+u
	v2 = y+y+y+y+u+y+u
	v3 = y+y+y+u+y+y+u
	v4 = y+y+u+y+y+y+u
	v5 = y+u+y+y+y+y+u
	v6 = u+y+y+y+y+y+u
	v7 = y+y+y+y+u+u+y
	v8 = y+y+y+u+y+u+y
	v9 = y+y+u+y+y+u+y
	v10 = y+u+y+y+y+u+y
	v11 = u+y+y+y+y+u+y
	v12 = y+y+y+u+u+y+y
	v13 = y+y+u+y+u+y+y
	v14 = y+u+y+y+u+y+y
	v15 = u+y+y+y+u+y+y
	v16 = y+y+u+u+y+y+y
	v17 = y+u+y+u+y+y+y
	v18 = u+y+y+u+y+y+y
	v19 = y+u+u+y+y+y+y
	v20 = u+y+u+y+y+y+y
	v21 = u+u+y+y+y+y+y
	ls = (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21)
	u = choice(ls)
	return u
# start checking
def start(client,username):
	try:ok = fragment(username)
	except:return
	try:
		if not ok:
			checker(username,client)
		elif ok == "is taken":
			
			print(' \033[1;31mtaken - '+username+'')
		else:
			print(' \033[1;33mAuction - '+username+'')
	except Exception as e:print(e)
# get client
def clientX():
	client = TelegramClient("Client", b64decode("MjUzMjQ1ODE=").decode(),b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
	try:client.start()
	except:pass
	try:client(JoinChannelRequest("bobtools"))
	except:pass
	clear()
	return client
# start tool
def work():
	session = clientX()
	if not path.exists('banned4.txt'):
		with open('banned4.txt','w') as new:pass
	if not path.exists('flood.txt'):
		with open('flood.txt','w') as new:pass
	while True:
		username = usernameG()
		with open('banned4.txt', 'r') as file:
			check_username = file.read()
		if username in check_username:
			print('Forbidden - '+username+'')
			continue
		start(session,username)
work()