from threading import Lock
from functools import partial
from concurrent.futures import ThreadPoolExecutor

from panos.protocol import ping
from panos.filters import filter_result

lock = Lock()

def is_minecraft(host, silent=False, filtering=None):
	result = ping(host)
	if filtering and result:
		result = filter_result(result, filtering)
		
	if not silent:
		lock.acquire()
		try:
			print(f'Finished scan on {host}.')
		finally:
			lock.release()
	return result

def ping_servers(hosts, silent=False, filtering=None, max_workers=800):
	with ThreadPoolExecutor(max_workers = max_workers) as executor:
		results = executor.map(partial(is_minecraft, silent=silent, filtering=filtering), hosts)

	return [result for result in results if result]