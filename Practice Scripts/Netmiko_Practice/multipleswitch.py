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
for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip int brief")
    print(f"Output from {device['host']}:\n{output}\n")
    net_connect.disconnect()

# This script connects to multiple Cisco IOS devices using Netmiko, retrieves the output of the "show ip int brief" command from each device, and prints it.
# It then disconnects from each device.