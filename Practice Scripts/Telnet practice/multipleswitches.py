import getpass
import telnetlib

user = input("Enter your Username: ")
password = getpass.getpass()

f = open ('myswitches')

for IP in f:
    IP=IP.strip()
    print ('Configuring Switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    for vlan in range (2,10):
        tn.write(b"vlan " + str(vlan).encode('ascii') + b"\n")
        tn.write(b"name Python_vlan_" + str(vlan).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"show vlan\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
