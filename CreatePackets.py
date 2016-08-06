#!/usr/bin/python3

from scapy.all import *

print("\nThis Script will create an Ethernet Frame")

# Creation of Ethernet Frame with scapy defaults parameters
MyFrame = Ether()
# Call show scapy methods for see attributs of this Ethernet Frame (dst,src,type)
MyFrame.show()
