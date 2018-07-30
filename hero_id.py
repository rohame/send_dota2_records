from fundata.client import init_api_client
from fundata.client import get_api_client

def hero_id(hero_id):

	init_api_client('2551d1621e7c487', '62ac8909a1ee4a4d8a124ef6a3bdf76')
	client = get_api_client()
	
	url = '/data-service/dota2/public/raw/heroes'
	data = {}
	res = client.api(url, data)
	heroes=res['data']
	for hero in heroes:
		if hero_id==hero['hero_id']:
			hero_name=hero['cn_name']
			en_name=hero['en_name']
	return hero_name
