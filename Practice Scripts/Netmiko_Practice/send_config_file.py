from netmiko import ConnectHandler

# Define the device
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
# open the file
with open('config_file.txt', 'r') as file:
    config_commands = file.read().splitlines()
# read the file and split it into lines
print(config_commands)

# List of devices
devices = [S1, S2]
# Loop through each device and connect
for device in devices:
    net_connect = ConnectHandler(**device)
    # Send configuration commands
    net_connect.send_config_set(config_commands)
    # Send command to check the configuration
    output = net_connect.send_command("show vlan brief")
    # Print the output
    print(f"Output from {device['host']}:\n{output}\n")
    # Disconnect from the device
    net_connect.disconnect()