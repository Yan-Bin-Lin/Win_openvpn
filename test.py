import time
from Win_OpenVPN import OpenVPN

O = OpenVPN()
print(O.ovpn)

O.connect(2)
print('connect success')
time.sleep(10)
O.disconnect()
time.sleep(10)
O.connect()