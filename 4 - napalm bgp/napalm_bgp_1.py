
import json
from napalm import get_network_driver


def main():
	driver = get_network_driver('ios')
	iosvl2 = driver('192.168.122.72', 'david', 'cisco')
	iosvl2.open()

	bgp_neighbors = iosvl2.get_bgp_neighbors()
	print (json.dumps(bgp_neighbors, indent=4))

	iosvl2.close()


if __name__ == '__main__':
	main()
