from requests import get

def get_cracked(uuid, name):
	resp = get(f'https://api.mojang.com/users/profiles/minecraft/{name}')
	try:
		json_resp = resp.json()
		return json_resp['id'] != uuid.replace('-', '')
	except Exception as e:
		return True