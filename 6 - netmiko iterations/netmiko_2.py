from netmiko import ConnectHandler

def main():
	with open('commands_file') as f:
		commands_to_send = f.read().splitlines()

	ios_devices = {
		'device_type': 'cisco_ios',
		'ip': '192.168.122.72',
		'username': 'david',
		'password': 'cisco',
	}

	all_devices = [ios_devices]

	for devices in all_devices:
		net_connect = ConnectHandler(**devices)
		output = net_connect.send_config_set(commands_to_send)
		print (output)



if __name__ == '__main__':
	main()
