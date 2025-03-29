from pysnmp.hlapi import *

def snmp_v2c_get(ip, community, oid):
    """
    SNMPv2c GET request to read an OID.
    """
    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),  # SNMPv2c community string
               UdpTransportTarget((ip, 161)),  # SNMP agent IP and port
               ContextData(),
               ObjectType(ObjectIdentity(oid)))  # OID to query

    if error_indication:
        print(f"SNMPv2c Error: {error_indication}")
    elif error_status:
        print(f"SNMPv2c Error: {error_status.prettyPrint()}")
    else:
        for var_bind in var_binds:
            print(f"SNMPv2c Result: {var_bind.prettyPrint()}")

def snmp_v3_get(ip, user, auth_key, priv_key, oid):
    """
    SNMPv3 GET request to read an OID.
    """
    error_indication, error_status, error_index, var_binds = next(
        getCmd(SnmpEngine(),
               UsmUserData(user, auth_key, priv_key,
                           authProtocol=usmHMACSHAAuthProtocol,
                           privProtocol=usmAesCfb128Protocol),  # SNMPv3 user and keys
               UdpTransportTarget((ip, 161)),  # SNMP agent IP and port
               ContextData(),
               ObjectType(ObjectIdentity(oid))))  # OID to query

    if error_indication:
        print(f"SNMPv3 Error: {error_indication}")
    elif error_status:
        print(f"SNMPv3 Error: {error_status.prettyPrint()}")
    else:
        for var_bind in var_binds:
            print(f"SNMPv3 Result: {var_bind.prettyPrint()}")

if _name_ == "_main_":
    # Example OID for system description (1.3.6.1.2.1.1.1.0)
    oid = "1.3.6.1.2.1.1.1.0"

    # SNMPv2c example
    print("SNMPv2c Example:")
    snmp_v2c_get("192.168.1.1", "public", oid)  # Replace with your SNMP agent IP and community string

    # SNMPv3 example
    print("\nSNMPv3 Example:")
    snmp_v3_get("192.168.1.1", "snmpuser", "authkey123", "privkey123", oid)  # Replace with your SNMPv3 credentials

#     # Note: Ensure you have the required SNMP libraries installed.
#     ### Explanation of the Script:
# 1. *SNMPv2c*:
#    - Uses a community string (e.g., public) for authentication.
#    - The getCmd function sends an SNMP GET request to the specified OID.

# 2. *SNMPv3*:
#    - Uses a username, authentication key, and encryption key for secure communication.
#    - The UsmUserData object configures the SNMPv3 user with authentication and privacy protocols (e.g., SHA for authentication and AES for encryption).

# 3. *OID*:
#    - The Object Identifier (OID) specifies the SNMP object to query. For example, 1.3.6.1.2.1.1.1.0 corresponds to the system description.

# 4. *Error Handling*:
#    - The script checks for errors in the SNMP response and prints them if any.

# ---
# ### Example Output:
# #### SNMPv2c:

# SNMPv2c Example:
# SNMPv2c Result: SNMPv2-SMI::mib-2.1.1.1.0 = STRING: "Cisco IOS Software, C2960 Software (C2960-LANBASE-M), Version 15.0(2)SE7, RELEASE SOFTWARE (fc1)"


# #### SNMPv3:

# # SNMPv3 Example:
# SNMPv3 Result: SNMPv2-SMI::mib-2.1.1.1.0 = STRING: "Cisco IOS Software, C2960 Software (C2960-LANBASE-M), Version 15.0(2)SE7, RELEASE SOFTWARE (fc1)"




# ### Notes:
# - Replace the IP address, community string, and SNMPv3 credentials with your device's details.
# - Ensure the SNMP agent on the device is configured to allow access from your script's IP address.
# - For SNMPv3, the authentication and privacy protocols must match the configuration on the SNMP agent.

# This script provides a basic framework for reading SNMP objects using Python. You can extend it to handle multiple OIDs, perform SNMP walks, or integrate it into a larger network monitoring system.