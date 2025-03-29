import ipaddress

def subnet_calculator(ip_cidr):
    try:
        # Parse the input as an IPv4Network object
        network = ipaddress.IPv4Network(ip_cidr, strict=False)
        
        # Extract network details
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        subnet_mask = network.netmask
        wildcard_mask = network.hostmask
        num_hosts = network.num_addresses - 2  # Subtract network and broadcast addresses
        first_host = network_address + 1
        last_host = broadcast_address - 1
        
        # Print the results
        print(f"Network Address: {network_address}")
        print(f"Broadcast Address: {broadcast_address}")
        print(f"Subnet Mask: {subnet_mask}")
        print(f"Wildcard Mask: {wildcard_mask}")
        print(f"Number of Usable Hosts: {num_hosts}")
        print(f"First Usable Host: {first_host}")
        print(f"Last Usable Host: {last_host}")
        print(f"IP Range: {first_host} - {last_host}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example input: "192.168.1.0/24"
    ip_cidr = input("Enter IP address in CIDR notation (e.g., 192.168.1.0/24): ")
    subnet_calculator(ip_cidr)