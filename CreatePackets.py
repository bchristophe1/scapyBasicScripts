#!/usr/bin/python3

from scapy.all import *

print("\nThis Script will create an Ethernet Frame")

# Creation of Ethernet Frame with scapy defaults parameters
MyFrame = Ether()

# Definition of Frame parameters
MyFrame.dst = '00:AA:BB:CC:DD:EE'
MyFrame.src = '01:0A:0B:0C:0D:0E'

# Call show scapy methods for see attributs of this Ethernet Frame (dst,src,type)
MyFrame.show()
