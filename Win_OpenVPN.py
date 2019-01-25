'''
Created on 2019年1月25日
@author: danny
@note: this API should put in openvpn-gui direction
'''
import threading
import os

#a class to handle thread
class VPNConnect(): 
    def __init__(self, ovpn_name):
        self.ovpn_name = ovpn_name
       
    def NewVPN(self):
        t = threading.Thread(target = self.connect)
        t.start()
    
    #try to connect, cause it won't return any value, just call this function will make the whole program stop
    def connect(self):
        os.system('.\openvpn-gui.exe --connect ' + self.ovpn_name)
        

class OpenVPN():
    def __init__(self):
        self.ConnectList = list()
        self.ovpn = list()
        #for all ovpn file
        dirlist = os.listdir('../config')
        for file in dirlist:
            if file.find('ovpn') != -1:
                self.ovpn.append(file)
    
    #only when OpenVPN-GUI is closed can use
    def connect(self, index = 0):
        self.ConnectList.append(VPNConnect(self.ovpn[index]))
        self.ConnectList[0].NewVPN()
        
    #actually, what this function do is closing openvpn-gui, and then you are able to call connect again
    def disconnect(self):
        #close openvpn
        os.system('taskkill /F /IM  openvpn-gui.exe')
        os.system('taskkill /F /IM  openvpn.exe')
        #delete the thread
        del self.ConnectList[0]

        
O = OpenVPN()
print(O.ovpn)
O.connect(2)
print('connect success')
import time
time.sleep(10)
O.disconnect()
time.sleep(10)
O.connect()