import config
from panos.pinger import ping_servers
from panos.hosts_generation import generate_hosts, randomize_hosts
from panos.protocol import ping

def scan_random_aternos(silent=False, filtering=None):
    print('Starting random scan...')
    hosts = randomize_hosts(config.IPS, config.PORTRANGE)
    results = ping_servers(hosts, silent=silent, filtering=filtering)
    if not results:
        return ['No results.']
    return results

def scan_full_aternos(silent=False, filtering=None):
    print('Starting full scan...')
    output = []
    for ip in config.IPS:
        hosts = generate_hosts(ip, config.PORTRANGE)
        results = ping_servers(hosts, silent=silent, filtering=filtering)
        output += [result for result in results if result]
    if not output:
        return ['No results.']
    return output

def scan_specific_aternos(ip, silent=False, filtering=None):
    print('Starting specific scan...')
    hosts = generate_hosts(ip, config.PORTRANGE)
    results = ping_servers(hosts, silent=silent, filtering=filtering)
    if not results:
        return ['No results.']
    return results
