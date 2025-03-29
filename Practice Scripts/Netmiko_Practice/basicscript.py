from netmiko import ConnectHandler

S1 = {
    "device_type": "cisco_ios",
    "username": "Mukesh",
    "password": "Password",
    "host": "10.1.1.68"
}


net_connect = ConnectHandler(**S1)
output = net_connect.send_command("show ip int brief")
print(output)
net_connect.disconnect()
# This script connects to a Cisco IOS device using Netmiko, retrieves the output of the "show ip int brief" command, and prints it.
# It then disconnects from the device.
# Make sure to replace the device credentials with your own.
# Note: Ensure that you have the required libraries installed and the device is reachable.