import urllib.request
import json
import socket
import time

city = "cardiff"

def cardiff():



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
    PORTK = 6265
    
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    contents = urllib.request.urlopen("https://api.waqi.info/feed/"+ city +"/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
    
    ###print(contents)
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]
    qw11 = varab['data']['city']['url']

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
    s.sendto(str(qw11).encode('utf-8'),(HOST,PORTK))
    
    print(qw)
    print(qw2)
    print(qw3)
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def wrexham():



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
    PORTK = 6265
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    contents = urllib.request.urlopen("https://api.waqi.info/feed/wrexham/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
    print(varab['data']['city']['name'])
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]
   
##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def penarth():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/penarth/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def swansea():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/swansea/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return


def wigan():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/wigan/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def bristol():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/bristol/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def leeds():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/leeds/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def hull():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/hull/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def derby():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/derby/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def cambridge():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/cambridge/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def southampton():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/southampton/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def nottingham():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/nottingham/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def manchester():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/manchester/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def leicester():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/leicester/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def london():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/london/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def dublin():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/dublin/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def belfast():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/belfast/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return


def liverpool():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/liverpool/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return


def sheffield():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/sheffield/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def york():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/york/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
    s.sendto(str(qw).encode('utf-8'),(HOST,PORTA))
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def manchester():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/manchester/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def wrexham():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/wrexham/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def leeds():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/leeds/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def hull():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/hull/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def edinburgh():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/edinburgh/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def glasgow():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/glasgow/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return


def inverness():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/inverness/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def sunderland():

    


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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/" + city + "/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return

def bournemouth():



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
    contents = urllib.request.urlopen("https://api.waqi.info/feed/bournemouth/?token=ad7f50bdd369214453d37081c50222ed932f1215").read()
##penarth, wrexham, london, dublin, israel, jerusalem, sydney,shanghai,  istanbul, swansea, toronto,beijing, adelaide, melbourne, paris, philadelphia, bristol, glasgow, lisbon, tokyo, amsterdam, leeds, bogota, moscow, copenhagen, madrid

    varab = json.loads(contents)
##print(varab.keys())
    print(varab['data']['city']['name'])
    print(varab['data']['city']['geo'][0])
    print(varab['data']['city']['geo'][1])
    print(varab['data']['time']['s'])
    qw = varab['data']['iaqi']['so2']
    qw2 = varab['data']['iaqi']['o3']
    qw3 = varab['data']['iaqi']['no2']
    qw4 = varab['data']['city']['name']
    qw5 = varab['data']['iaqi']['pm10']
    qw6 = varab['data']['iaqi']['pm25']
    qw7 = varab['data']['time']['s']
    qw8 = varab['data']['dominentpol']
    qw9 = varab['data']['city']['geo'][0]
    qw10 = varab['data']['city']['geo'][1]

##carbon monoxide, nitrogen dioxide, ozone, particlatematter 10, particulate matter 25, sulphur dioxide, toxicity?
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
##print(qw4)
    print(varab['data']['iaqi'])
    print(varab['data']['dominentpol'])
    return






###########


UDP_IP = "127.0.0.1"
UDP_PORT = 5005



###########


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
     print (data.decode('utf-8'))
     
     if data.decode('utf-8') == "d":
        
            cardiff()

     if data.decode('utf-8') == "b":
        
            penarth()

     if data.decode('utf-8') == "c":
        
            wrexham()

     if data.decode('utf-8') == "a":
        
            wigan()
            
     if data.decode('utf-8') == "e":
        
            swansea()

     if data.decode('utf-8') == "f":
        
            bristol()

     if data.decode('utf-8') == "g":
        
            leeds()
            
     if data.decode('utf-8') == "h":
        
            hull()

     if data.decode('utf-8') == "i":
        
            london()
            
     if data.decode('utf-8') == "j":
        
            cambridge()

     if data.decode('utf-8') == "k":
        
            southampton()

     if data.decode('utf-8') == "l":
        
            manchester()

     if data.decode('utf-8') == "m":
        
            leicester()

     if data.decode('utf-8') == "n":
        
            nottingham()

     if data.decode('utf-8') == "o":
        
            dublin() 

     if data.decode('utf-8') == "p":
        
            belfast() 

     if data.decode('utf-8') == "q":
        
            liverpool()

     if data.decode('utf-8') == "r":
        
            sheffield() 

     if data.decode('utf-8') == "s":
        
            york()

     if data.decode('utf-8') == "t":
        
            edinburgh()

     if data.decode('utf-8') == "u":
        
            glasgow()

     if data.decode('utf-8') == "v":
        
            inverness()

     if data.decode('utf-8') == "w":
        
            bournemouth()

     if data.decode('utf-8') == "x":
        
            sunderland()


