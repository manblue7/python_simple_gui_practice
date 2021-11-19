import time
import random
import PySimpleGUI as sg
from network_scanner import scan


menu = [[sg.Text('Python hacking tools', auto_size_text=True)], 
[sg.DropDown(['MAC changer', 'ARP Spoofer', 'Network Scanner', 'Packet Sniffer'], key='tools')], 
[sg.Button('lets get started', key='start')]]

mac_changer = [[sg.Text('MAC changer')], 
[sg.R('Random', group_id='idk')], 
[sg.R('Input', group_id='idk')], 
[sg.In('MAC to change to...')], 
[sg.Button('Change MAC')],
[sg.Button('Go back', key='back')]]

arp_spoofer = [[sg.Text('ARP Spoof')],
[sg.Text('Target IP')],
[sg.In()],
[sg.Button('Go back', key='back2')]]

net_scan = [[sg.Text('Network Scanner')],
[sg.Text('Ip Range')],
[sg.In(key='routerip')],
[sg.Button('Scan')],
[sg.Text('', key='results', size=(37, 20), background_color='black')],
[sg.Button('Go back', key='back3')]]

packet_sniff = [[sg.Text('Packet Scanner')],
[sg.Button('Sniff')],
[sg.Text('', key='sniffresults', size=(37, 20), background_color='black')],
[sg.Button('Go back', key='back4')]]

layout = [[sg.Column(menu, key='-COL1-'), 
sg.Column(mac_changer, visible=False, key='-COL2-'),
sg.Column(arp_spoofer, visible=False, key='-COL3-'),
sg.Column(net_scan, visible=False, key='-COL4-'),
sg.Column(packet_sniff, visible=False, key='-COL5-')]]

font=('Arial', 20)

window = sg.Window('Python Hacks', layout, resizable=True, finalize=True, font=font, element_justification='c')
window.TKroot.minsize(500, 200)


laynum = 1
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'start':
        if values['tools'] == 'MAC changer':
            window[f'-COL{laynum}-'].update(visible=False)
            laynum = 2
            window[f'-COL{laynum}-'].update(visible=True)
        if values['tools'] == 'ARP Spoofer':
            window[f'-COL{laynum}-'].update(visible=False)
            laynum = 3
            window[f'-COL{laynum}-'].update(visible=True)
        if values['tools'] == 'Network Scanner':
            window[f'-COL{laynum}-'].update(visible=False)
            laynum = 4
            window[f'-COL{laynum}-'].update(visible=True)
        if values['tools'] == 'Packet Sniffer':
            window[f'-COL{laynum}-'].update(visible=False)
            laynum = 5
            window[f'-COL{laynum}-'].update(visible=True)     
    if event == 'back' or event == 'back2' or event == 'back3' or event == 'back4':
        window[f'-COL{laynum}-'].update(visible=False)
        laynum = 1
        window[f'-COL{laynum}-'].update(visible=True)
    if event == 'Scan':
        results = scan(values['routerip'])
        window['results'].update(results)
window.close()
