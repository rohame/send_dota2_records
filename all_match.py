from fundata.client import init_api_client
from fundata.client import get_api_client
from qqemail import send_email
from hero_id import hero_id as h_i
import time

init_api_client('2551d1621e7c487', '62ac8909a1ee4a4d8a124ef6a3bdf76')
client = get_api_client()

player_name=input("Please input the player's name:")
steam_id=input('Please input Steam ID(185735256):')
url = '/data-service/dota2/public/player/'+steam_id+'/match_ids'
data = {}
res = client.api(url, data)
#print(res)

new_ids=res['data']
new_ids=str(new_ids)
latest_id=new_ids[-11:-1]

#filename=steam_id+".txt"
#with open(filename,'w') as match_ids:
#	match_ids.write(new_ids)

url = '/data-service/dota2/public/match/'+latest_id+'/general_info'
data = {}
res = client.api(url, data)
#print(res)
#print('\n\n\n\n')
radiant_win=res['data']['radiant_win']
print(str(radiant_win))
players=res['data']['players']

start_time=res['data']['start_time']
start_time=int(start_time)
ending_time=start_time+res['data']['duration']
time_now=time.time()
time_now=int(time_now)
time_interval=time_now-ending_time
time_interval=round(time_interval/60)
time_interval=str(time_interval)

num_of_players=len(players)
for i in range(num_of_players):
	account_id=players[i]['account_id']
	account_id=str(account_id)
	#print(account_id)
	if account_id==steam_id:
		hero_id=players[i]['hero_id']
		kills=players[i]['kills']
		deaths=players[i]['deaths']
		gold_per_min=players[i]['gold_per_min']
		hero_damage=players[i]['hero_damage']
		tower_damage=players[i]['tower_damage']
		#print(str(i))
		if i<=4:
			radiant=True
			win=radiant_win
			#print(str(win))
		else:
			radiant=False
			win=not(radiant_win)
if win is True:
	win_text='赢了。'
else:
	win_text='输了。'

hero_name=h_i(hero_id)
kills=str(kills)
deaths=str(deaths)
gold_per_min=str(gold_per_min)
hero_damage=str(hero_damage)
tower_damage=str(tower_damage)

print('邮件正文：')
text=time_interval+'分钟前，'+player_name+'玩了一盘DOTA，'+win_text+'用的是'+hero_name+'，杀了'+kills+'个人，死了'+deaths
text+='次，每分钟金钱'+gold_per_min+'，造成英雄伤害'+hero_damage+'点，对防御塔伤害'+tower_damage+'点。'
print(text)
if res['retcode']==200:
	send_or_not=input("Send or not?(Y/N):")
	if send_or_not=="Y" or send_or_not=="y":
		send_email(text)
	else:
		print("Canceled")
else:
	print('api failed')

