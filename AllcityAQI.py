##Simon Kilshaw 2020 AQI Sonification Project
import urllib.request
import json
import socket
import time
import webbrowser
def do():
    HOST = "127.0.0.1"
    PORTA = 6255
    PORTB = 6256
    PORTC = 6257
    PORTD = 6258
    PORTE = 6259
    PORTF = 6260
    PORTG = 6261
    PORTH = 6262
    PORTI = 6263
    PORTJ = 6264
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    contents = urllib.request.urlopen("https://api.waqi.info/feed/" + (data.decode('utf-8')) + "/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
    varab = json.loads(contents)
    
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    print(varab['data']['city']['url'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['co']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]
    qw11 = varab['data']['city']['url'] 
    s.sendto(str(qw).encode('utf-8'),(HOST,PORTA))
    s.sendto(str(qw2).encode('utf-8'),(HOST,PORTB))
    s.sendto(str(qw3).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(qw4).encode('utf-8'),(HOST,PORTD))
    s.sendto(str(qw5).encode('utf-8'),(HOST,PORTE))
    s.sendto(str(qw6).encode('utf-8'),(HOST,PORTF))
    s.sendto(str(qw7).encode('utf-8'),(HOST,PORTG))
    s.sendto(str(qw8).encode('utf-8'),(HOST,PORTH))
    s.sendto(str(qw9).encode('utf-8'),(HOST,PORTI))
    s.sendto(str(qw10).encode('utf-8'),(HOST,PORTJ))
    print(qw)
    print(qw2)
    print(qw3)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    print(varab['data']['aqi'])
    webbrowser.open("https://www.openstreetmap.org/?mlat="+ str(qw9) +"&mlon=" + str(qw10) +"&zoom=3.5",new=1, autoraise=False)

    ##webbrowser.open(qw11)
    ##webbrowser.get("chrome").open("https://earth.google.com/web/search/" + qw4 +"",new=0, autoraise=True)
    webbrowser.get("chrome").open("https://earth.google.com/web/search/"+ str(qw9) + ","+ str(qw10) +"/data=KAI",new=0)
    ##webbrowser.get('chrome').open("https://www.google.com/maps/@" + str(qw9) + "," + str(qw10) +"m")
    return
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))
while True:
     data, addr = sock.recvfrom(1024) 
     print (data.decode('utf-8'))
     do()








     ##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid, yueyang, marseilles,Los Angeles, Noida, Navi Mumbai, Piraeus, Incheon, Puente Alto, Mexico 
