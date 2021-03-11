from urllib.request import urlopen
import json
import socket

# 获取公网ip地址
def GetIP():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    return str(my_ip.decode())

# 获取内网ip地址
def GetLocalIP():
    try: 
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
        s.connect(('8.8.8.8',80)) 
        ip = s.getsockname()[0] 
    except Exception:
        return None
    finally: 
        s.close() 
    return ip

# 获取当前位置经纬度（基于IP地址的粗略定位，仅定位到城市）
# 返回数据：（经度， 纬度）
def GetLocationByIP():
    response = urlopen("https://restapi.amap.com/v3/ip?key=24c1ffc0a6c3d2f1d06570335356875d&ip=" + GetIP())
    js = json.load(response)
    status = js['status']
    if not status == '1':
        print("error")
    rect = js['rectangle']
    cord_list = rect.split(';')
    cord1_long = float(cord_list[0].split(',')[0])
    cord1_lan = float(cord_list[0].split(',')[1])
    cord2_long = float(cord_list[1].split(',')[0])
    cord2_lan = float(cord_list[1].split(',')[1])
    cord_cen_long = (cord1_long + cord2_long) / 2
    cord_cen_lan = (cord1_lan + cord2_lan) / 2
    return cord_cen_long, cord_cen_lan