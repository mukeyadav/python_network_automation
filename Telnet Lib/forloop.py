import getpass
import telnetlib

HOST = "10.1.1.69"
user = input("Enter your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
for vlan in range (2,5):
    tn.write(b"no vlan " + str(vlan).encode('ascii') + b"\n")
#    tn.write(b"name Python_vlan_" + str(vlan).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"show vlan\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
