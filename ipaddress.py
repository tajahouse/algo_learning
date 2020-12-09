#An ip addres is a numerical label assigned to each device participating in a computer etwork tha tuses the internet protocol for communication. There are two versions of the internet protocol and thys tow versions of address. Given a string, find out if it satisfies the IPv4 address namng rules
import ipaddress

def isIPv4Address(inputString):
    ipAdd = inputString.split(".")

    return len(ipAdd) == 4 and all(n.isdigit() and 0 <= int(n)< 256 for n in ipAdd)