from netmiko import ConnectHandler

S1 = {
    "device_type": "cisco_ios",
    "username": "Mukesh",
    "password": "Password",
    "host": "10.1.1.68"
}

S2 = {
    "device_type": "cisco_ios",
    "username": "Mukesh",
    "password": "Password",
    "host": "10.1.1.69"
}

# List of devices
devices = [S1, S2]
# Loop through each device and connect
config_commands = [ 'logging buffered 20000',
                    'logging buffered 20010',
                    'no logging console' ]
for device in devices:
    net_connect = ConnectHandler(**device)
    # Send configuration commands
    net_connect.send_config_set(config_commands)
    # Send command to check the configuration
    output = net_connect.send_command("show run | include logging")
    print(f"Output from {device['host']}:\n{output}\n")
    # Disconnect from the device
    net_connect.disconnect()