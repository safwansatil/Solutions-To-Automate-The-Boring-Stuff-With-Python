#! python3
# pwEz.py - a very unsafe password locker program

PASSWORDS = {
    'admin' : 'swedeptcy<3',
    'wifi' : 'swe11923',
    '120' : 'boulagbe120e'
}

import sys, pyperclip

if(len(sys.argv)<2):
    print('Usage: py pwEz.py [room] - copy admin wifi password')
    sys.exit()

room = sys.argv[1] 

if room in PASSWORDS:
    pyperclip.copy(PASSWORDS[room])
    print(f'Password for room {room} copied to clipboard')
else:
    print(f"No room called {room}")
