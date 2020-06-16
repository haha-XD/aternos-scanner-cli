from panos.api_requests import get_cracked

def filter_cracked(result):
	if any([get_cracked(player.id, player.name) for player in result.players]):
		return result
	else:
		return None		

def filter_premium(result):
	if not any([get_cracked(player.id, player.name) for player in result.players]):
		return result
	else:
		return None		

def filter_version(result, version_filter):
	if version_filter in result.version:
		return result
	else:
		return None

def filter_populated(result):
	if result.players.online > 0:
		return result
	else:
		return None

def filter_empty(result):
	if result.players.online == 0:
		return result
	else:
		return None

def filter_result(result, filtering):
	result_modified = result
	filtering_string = filtering

	if '(cracked)' in filtering_string and result_modified:
		result_modified = filter_cracked(result_modified)
		filtering_string = filtering_string.replace('(cracked)', '')

	if '(premium)' in filtering_string and result_modified:
		result_modified = filter_premium(result_modified)
		filtering_string = filtering_string.replace('(premium)', '')

	if '(populated)' in filtering_string and result_modified:
		result_modified = filter_populated(result_modified)
		filtering_string = filtering_string.replace('(populated)', '')

	if '(empty)' in filtering_string and result_modified:
		result_modified = filter_empty(result_modified)
		filtering_string = filtering_string.replace('(empty)', '')

	if filtering_string and result_modified:
		result_modified = filter_version(result_modified, filtering_string)

	return result_modified
