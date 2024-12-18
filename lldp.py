from scapy.all import *

#download your MAC address
iface = "Ethernet" #between "" write your interface name
my_mac = get_if_hwaddr(iface)

print(f"Using Source MAC: {my_mac}")  #checking you MAC address in terminal

#creating LLDP frame
lldp_frame = (
    Ether(dst="01:80:c2:00:00:0e", src=my_mac, type=0x88cc) /
    Raw(load=(
        b'\x02\x07\x04' + bytes.fromhex(my_mac.replace(":", "")) +  # Chassis ID TLV
        b'\x04\x09\x05Ethernet'                                     # Port ID TLV
        b'\x06\x02\x00\x78'                                         # TTL TLV
        b'\x00\x00'                                                 # End TLV
    ))
)

#sending LLDP frame
sendp(lldp_frame, iface=iface)
