from netmiko import ConnectHandler

def main():
	iosv_l2_s1 = {
		'device_type': 'cisco_ios',
		'ip': '192.168.122.72',
		'username': 'david',
		'password': 'cisco',
	}

	net_connect = ConnectHandler(**iosv_l2_s1)
	output = net_connect.send_command('show ip int brief')
	print(output)



if __name__ == '__main__':
	main()
