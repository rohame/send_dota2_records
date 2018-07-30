from fundata.client import init_api_client
from fundata.client import get_api_client
from qqemail import send_email

init_api_client('2551d1621e7c487', '62ac8909a1ee4a4d8a124ef6a3bdf76')
client = get_api_client()
uri = '/data-service/dota2/analysis/player/180999306/basic_stats'
data = {}
res = client.api(uri, data)

for key in res['data'].keys():
	print(key)

if res['retcode']==200:
	print(res)
	res=str(res)
	#send_email(res)
else:
	print('api failed')
