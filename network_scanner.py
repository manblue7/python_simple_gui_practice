import optparse
import scapy.all as scapy

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='target', help='Target IP address / IP range')
    (options, arguments) = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    clients_list = []
    for ele in answered:
        client_dict = {'ip': ele[1].psrc, 'mac': ele[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
    
def print_result(results):
    print('IP\t\tMAC Address')
    for i in results:
        print(i['ip'] + "\t\t" + i['mac'])

options = getArgs()
scan_result = scan(options.target)
print_result(scan_result)